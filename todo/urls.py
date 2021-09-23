from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home44'),
    path('', views.create_todo, name='create-todo55'),
]
