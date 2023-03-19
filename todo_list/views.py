from msilib.schema import ListView
from django.shortcuts import render
from .models import *

class ListTodo(ListView):
    model = ToDoList
    template_name = 'todo_list/List.html'