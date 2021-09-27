from django.test import TestCase
from authentication.models import User
from todo.models import Todo


class TestModel(TestCase):

    def test_should_create_todo(self):
        user = User.objects.create_user(
            username='username', email='email@email.com')
        user.set_password('passsssssss')
        user.save()

        todo = Todo(owner=user, title='NewTodo222', description='wowowowow')
        todo.save()

        self.assertEqual(str(todo), 'NewTodo222')
