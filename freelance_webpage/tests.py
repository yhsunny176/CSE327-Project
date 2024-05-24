from django.test import TestCase
from django.urls import reverse

class TemplateTestCase(TestCase):
    def test_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_register_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'register.html')

    def test_login_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')
