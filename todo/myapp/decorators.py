from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

def NotAllowed_on_login(view_func):
    def wrapper(request , *args , **keyargs):
        if request.user.is_authenticated == False : 
            return view_func(request , *args , **keyargs)
        else:
            return redirect('/')
    return wrapper