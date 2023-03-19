from django.contrib import admin
from django.urls import path
from todo_list.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListTodo.as_view(), name='index')
]
