from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'tags']

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.order_by('name')


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        exclude = ["user"]

class RegisterForm(UserCreationForm):
    class Meta :
        model = User 
        fields = ['username' , 'password1' , 'password2'  ]
