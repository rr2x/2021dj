from django.test import TestCase
from authentication.models import User


class TestModel(TestCase):

    def test_should_create_user(self):
        user = User.objects.create_user(
            username='username', email='email@email.com')
        user.set_password('passsssssss')
        user.save()

        self.assertEqual(str(user), 'email@email.com')
