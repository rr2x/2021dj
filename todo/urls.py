from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home44'),
    path('create/', views.create_todo, name='create-todo55'),
    path('todo/<id>/', views.todo_detail, name='todo66'),
]
