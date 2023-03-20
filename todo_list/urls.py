from django.urls import path
from .views import *

urlpatterns = [
    path('list/<int:list_id>/', ItemListView.as_view(), name='list')
]
