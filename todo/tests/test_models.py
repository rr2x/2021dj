from todo.models import Todo
from utils.setup_test import TestSetup


class TestModel(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()
        todo = Todo(owner=user, title='NewTodo222', description='wowowowow')
        todo.save()

        self.assertEqual(str(todo), todo.title)
