from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages


class TestViews(TestCase):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register22'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login11'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_should_signup_user(self):
        self.user = {
            'username': 'username-test',
            'email': 'email@email1.com',
            'password': '111111',
            'password2': '111111'
        }

        response = self.client.post(reverse('register22'), self.user)
        # redirect status code is 302
        self.assertEquals(response.status_code, 302)

    def test_should_not_signup_user_with_taken_username(self):
        self.user = {
            'username': 'username-test',
            'email': 'email@email2.com',
            'password': '111111',
            'password2': '111111'
        }

        self.client.post(reverse('register22'), self.user)
        response = self.client.post(reverse('register22'), self.user)
        self.assertEquals(response.status_code, 409)

        storage = get_messages(response.wsgi_request)

        # errors = []

        # for message in storage:
        #     # print(message)
        #     errors.append(message.message)

        self.assertIn('Username taken, choose another one',
                      list(map(lambda x: x.message, storage)))

        # import pdb  # python debugger
        # pdb.set_trace()  # enter 'c' on command line to continue

    def test_should_not_signup_user_with_taken_email(self):
        self.user1 = {
            'username': 'username-test-1',
            'email': 'email@email-test.com',
            'password': '111111',
            'password2': '111111'
        }

        self.user2 = {
            'username': 'username-test-2',
            'email': 'email@email-test.com',
            'password': '111111',
            'password2': '111111'
        }

        self.client.post(reverse('register22'), self.user1)
        response = self.client.post(reverse('register22'), self.user2)
        self.assertEquals(response.status_code, 409)
