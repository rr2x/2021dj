from .models import Todo
from .forms import TodoForm
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(request, 'todo/index.html', context)


def create_todo(request):
    form = TodoForm()
    context = {'form': form}

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False)

        todo = Todo()
        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed == "on" else False

        todo.save()

        return HttpResponseRedirect(reverse('todo66', kwargs={'id': todo.pk}))

    return render(request, 'todo/create-todo.html', context)


def todo_detail(request, id):
    return render(request, 'todo/todo-detail.html', {})
