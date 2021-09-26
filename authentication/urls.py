from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login11'),
    path('register', views.register, name='register22'),
    path('logout', views.logout, name='logout00'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate121')
]
