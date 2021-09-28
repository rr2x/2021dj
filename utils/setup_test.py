from django.test import TestCase
from authentication.models import User
from faker import Faker


class TestSetup(TestCase):

    def setUp(self):

        self.faker = Faker()
        self.password = self.faker.paragraph(nb_sentences=5)

        self.user_signup = {
            'username': self.faker.name().split(' ')[0],
            'email': self.faker.email(),
            'password': self.password,
            'password2': self.password
        }

        self.user_taken_username = {
            'username': 'username-test',
            'email': 'email@email2.com',
            'password': '111111',
            'password2': '111111'
        }

        self.user1_taken_email = {
            'username': 'username-test-1',
            'email': 'email@email-test.com',
            'password': '111111',
            'password2': '111111'
        }

        self.user2_taken_email = {
            'username': 'username-test-2',
            'email': 'email@email-test.com',
            'password': '111111',
            'password2': '111111'
        }

    def create_test_user(self):
        user = User.objects.create_user(
            username='username', email='email@email.com')
        user.set_password('passsssssss')
        user.is_email_verified = True
        user.save()

        return user

    def tearDown(self):
        return super().tearDown()
