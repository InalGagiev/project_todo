from django.contrib import admin
from .models import *

admin.site.register(ToDoItem)
admin.site.register(ToDoList)