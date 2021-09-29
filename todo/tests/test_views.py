from utils.setup_test import TestSetup
from authentication.models import User
from todo.models import Todo
from django.urls import reverse


class TestViews(TestSetup):

    def test_should_create_a_todo(self):

        user = self.create_test_user()

        self.client.post(reverse('login11'), {
            'username': user.username,
            'password': 'passsssssss'
        })

        todos = Todo.objects.all()

        self.assertEqual(todos.count(), 0)

        response = self.client.post(reverse('create-todo55'), {
            'owner': user,
            'title': 'hey do this',
            'description': 'remember to do this'
        })

        updated_todos = Todo.objects.all()

        # more than 1 assertion needed
        self.assertEqual(updated_todos.count(), 1)

        self.assertEqual(response.status_code, 302)  # not enough
