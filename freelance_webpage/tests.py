from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from freelance_webpage.models import UserProfile

class TemplateTestCase(TestCase):
    """Test case for template rendering.

    Args:
        TestCase (class): Django's built-in test case class.
    """
    def test_index_template(self):
        """Test index template rendering.

        This method tests whether the index template is being used
        when accessing the index page.

        :return: None
        :rtype: NoneType
        """
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_register_template(self):
        """Test register template rendering.

        This method tests whether the register template is being used
        when accessing the register page.

        :return: None
        :rtype: NoneType
        """
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'register.html')

    def test_login_template(self):
        """Test login template rendering.

        This method tests whether the login template is being used
        when accessing the login page.

        :return: None
        :rtype: NoneType
        """
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
        'fname': 'Test',
        'lname': 'User',
        'email': 'test@example.com',
        'phone_number': '1234567890',
        'pass1': 'testpass',
        'pass2': 'testpass',
        'role': 'freelancer'
    })
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful registration
    
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'email': 'invalid@test.com', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid credentials')
    
    def test_login_no_data(self):
        response = self.client.post(reverse('login'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please fill out all fields')

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_POST_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please fill out all fields")

    def test_register_POST_passwords_do_not_match(self):
        response = self.client.post(self.register_url, {
            'fname': 'Test',
            'lname': 'User',
            'email': 'testuser@gmail.com',
            'phone_number': '1234567890',
            'pass1': 'password1',
            'pass2': 'password2',
            'role': 'freelancer'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Passwords do not match")

    def test_register_POST_email_already_registered(self):
        User.objects.create_user(username='testuser@gmail.com', email='testuser@gmail.com', password='password')
        response = self.client.post(self.register_url, {
            'fname': 'Test',
            'lname': 'User',
            'email': 'testuser@gmail.com',
            'phone_number': '1234567890',
            'pass1': 'password',
            'pass2': 'password',
            'role': 'freelancer'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email already registered")

    def test_register_POST_success(self):
        response = self.client.post(self.register_url, {
            'fname': 'Test',
            'lname': 'User',
            'email': 'testuser2@gmail.com',
            'phone_number': '1234567890',
            'pass1': 'password',
            'pass2': 'password',
            'role': 'freelancer'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('freelancer_dashboard'))
        user = User.objects.get(email='testuser2@gmail.com')
        self.assertIsNotNone(user)
        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(user_profile.role, 'freelancer')

