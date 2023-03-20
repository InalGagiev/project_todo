from django.contrib import admin
from django.urls import path, include
from todo_list.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListTodo.as_view()),
    path('todo/', include('todo_list.urls'))
]
