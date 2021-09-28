from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup


class TestViews(TestSetup):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register22'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login11'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_should_signup_user(self):
        response = self.client.post(reverse('register22'), self.user_signup)
        # redirect status code is 302
        self.assertEquals(response.status_code, 302)

    def test_should_not_signup_user_with_taken_username(self):
        self.client.post(reverse('register22'), self.user_taken_username)
        response = self.client.post(
            reverse('register22'), self.user_taken_username)
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

        self.client.post(reverse('register22'), self.user1_taken_email)
        response = self.client.post(
            reverse('register22'), self.user2_taken_email)
        self.assertEquals(response.status_code, 409)

    def test_should_login_successfully(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login11"), {
            'username': user.username,
            'password': 'passsssssss'
        })
        self.assertEquals(response.status_code, 302)  # 302 = redirect

        storage = get_messages(response.wsgi_request)

        self.assertIn(f"Welcome {user.username}",
                      list(map(lambda x: x.message, storage)))

    def test_should_not_login_with_invalid_password(self):
        user = self.create_test_user()
        response = self.client.post(reverse("login11"), {
            'username': user.username,
            'password': 'passsssssss2'
        })
        self.assertEquals(response.status_code, 401)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Invalid credentials",
                      list(map(lambda x: x.message, storage)))
