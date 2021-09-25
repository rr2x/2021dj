from helpers.decorators import auth_user_should_not_access
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User
# to prevent collision
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse


@auth_user_should_not_access
def register(request):
    if request.method == 'POST':
        context = {'has_error': False, 'data': request.POST}

        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Enter a valid email address')
            context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR,
                                 'Username required')
            context['has_error'] = True

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username taken, choose another one')
            context['has_error'] = True

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email taken, choose another one')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'authentication/register.html', context)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Account created, you can now login')

        return redirect('login11')

    return render(request, 'authentication/register.html')


@auth_user_should_not_access
def login(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid credentials')
            return render(request, 'authentication/login.html', context)

        auth_login(request, user)

        messages.add_message(request, messages.SUCCESS,
                             f'Welcome {user.username}')

        return redirect(reverse('home44'))

    return render(request, 'authentication/login.html')


def logout(request):

    auth_logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Sucessfully loggedout')

    return redirect(reverse('login11'))
