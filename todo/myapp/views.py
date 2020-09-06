from django.shortcuts import render, redirect
from django.http import HttpResponse
import django.utils.timezone as tz
from .models import *
from .forms import *
import json
from .decorators import *
from django.contrib import messages
from .filters import FinishTodoFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate , login , logout

# Create your views here.
@login_required(login_url='login')
def home(request):
    todoForm = TodoForm()
    tagForm = TagForm()
    filterBy = request.GET.get('filter')
    todos = Todo.objects.filter(finish=False , user = request.user ).order_by('createdAt')
    if filterBy:
        todos = todos.filter(finish=False  , tags__name=filterBy , user = request.user)
        print(request.user.id)
        print(todos)
    tags = Tag.objects.filter(user = request.user).order_by('name')
    context = {"tags": tags,
               'todos': todos,
               'filter': filterBy,
               'todoForm': todoForm , 
               'tagForm' : tagForm
               }
    return render(request, 'myapp/home.html', context)

@login_required(login_url='login')
def finishTodo(request):
    if request.method == "POST":
        todoId = request.POST.get('id')
        todo = Todo.objects.get(id=todoId)
        if todo:
            todo.finish = True
            todo.endAt = tz.localtime()
            todo.save()
        return redirect("/?filter=""")
    else:
        todos = Todo.objects.filter(finish=True,user = request.user).order_by('createdAt')

        finishTodoFilter = FinishTodoFilter(request.GET , queryset=todos)
        todos = finishTodoFilter.qs

        paginator = Paginator(todos , 3)
        page_number = request.GET.get('page')
        todos = paginator.get_page(page_number)

        tags = request.GET.get("tags")

        context = {"finishTodos" : todos , "filterTabel" : finishTodoFilter , "tags" : tags}
        return render(request, 'myapp/finish_todo.html', context)

@login_required(login_url='login')
def postTodo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo =form.save()
            todo.user = request.user
            todo.save()
            messages.success(request, "New Todo been add")
        else:
            messages.error(request, "Error in save todo")
        return redirect("/")

@login_required(login_url='login')
def postTag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        print(request.POST)
        if form.is_valid():
            tag =form.save()
            tag.user = request.user
            tag.save()
            messages.success(request, "New Tag been add")
        else:
            messages.error(request, "Error in save tag")
        return redirect("/")

@NotAllowed_on_login
def registerPage(request):
    form = RegisterForm()
    errors = None
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("/")
        else :
            errors = form.errors.values()
    context = {"form" : form , "errors" : errors}
    return render(request , 'myapp/register.html' , context)

@NotAllowed_on_login
def loginPage(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect("/")
    return render(request , 'myapp/login.html')

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect("/")

@login_required(login_url='login')
def updateTodo(request , id):
    todo = Todo.objects.get(id = id , user = request.user)
    if todo :
        if request.method == "POST" :
            form = TodoForm(request.POST , instance=todo )
            if form.is_valid():
                form.save()
                return redirect("/")
        else :
            form = TodoForm(instance=todo)
            context = {"form" : form}
            return render(request , "myapp/updateTodo.html" , context)

@login_required(login_url='login')
def deleteTodo(request , id):
    todo = Todo.objects.get(id = id , user = request.user)
    if todo :
        if request.method == "POST" :
            todo.delete()
            return redirect("/")  
        else :
            form = TodoForm(instance=todo)
            context = {"todo" : todo}
            return render(request , "myapp/deleteTodo.html" , context)