from django.urls import path
from .views import * 

urlpatterns = [
    path("" , home , name="home"),
    path("finishTodo" , finishTodo , name="finish"),


    path("postTodo" , postTodo , name="postTodo"),
    path("postTag" , postTag , name="postTag"),

    path("updateTodo/<int:id>" , updateTodo , name="updateTodo"),
    path("deleteTodo/<int:id>" , deleteTodo , name="deleteTodo"),
    


    path("register" , registerPage , name="register"),
    path("login" , loginPage , name="login"),
    path("logout" , logoutPage , name="logout"),
]