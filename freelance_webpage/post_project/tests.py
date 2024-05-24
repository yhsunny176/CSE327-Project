from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from freelance_webpage.models import UserProfile
from .views import post_project
from .models import Project
from django.core.files.uploadedfile import SimpleUploadedFile
from justajob.settings import *
import os

class PostProjectViewTest(TestCase):
    """
    Test suite for the post_project view.

    Attributes:
        client (Client): The test client for simulating HTTP requests.
        user (User): The user created for the test cases.
        user_profile (UserProfile): The user profile associated with the created user.
        url (str): The URL for the post_project view.
        test_file_path (str): The path to a test file used in the tests.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser@email.com', password='testpassword')
        self.client.login(username='testuser@email.com', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.url = reverse('postproject')
        self.test_file_path = os.path.join(BASE_DIR, 'uploaded_docs', 'testfile.txt')

    def test_post_project_login(self):
        """
        Test accessing the post_project view while logged in.

        Asserts that the response status code is 200 and the correct template is used.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_project/postproject.html')

    def test_post_project_logout(self):
        """
        Test accessing the post_project view while logged out.

        Asserts that the response is a redirect to the login page.
        """
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, f"{reverse('login')}?next={self.url}")

    def tearDown(self):
        """
        Clean up after tests by removing any test files created.

        Removes files in the uploaded_docs directory that start with 'testfile_'.
        """
        # Get the list of files in the uploaded_docs directory
        files_in_dir = os.listdir(os.path.join(BASE_DIR, 'uploaded_docs'))
        
        # Execute the tearDown method from the parent class to clean up the database
        super().tearDown()
    
        # Remove files with names starting with 'testfile_'
        for file_name in files_in_dir:
            if file_name.startswith('testfile_'):
                file_path = os.path.join(BASE_DIR, 'uploaded_docs', file_name)
                if os.path.exists(file_path):
                    os.remove(file_path)

    def test_post_project_post_success(self):
        """
        Test posting a project successfully.

        Asserts that a project is created, file is uploaded, and response is a redirect.
        """
        with open(self.test_file_path, 'rb') as test_file:
            attached_file = SimpleUploadedFile('testfile.txt', test_file.read())

        data = {
            'name': 'Test Project',
            'category': 'Test Category',
            'description': 'Test Description',
            'min_price': 100,
            'max_price': 200,
            'attached_file': attached_file
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(Project.objects.count(), 1)
        project = Project.objects.first()
        self.assertEqual(project.project_name, 'Test Project')
        self.assertEqual(project.category, 'Test Category')
        self.assertEqual(project.project_description, 'Test Description')
        self.assertEqual(project.min_bid_price, 100)
        self.assertEqual(project.max_bid_price, 200)
        actual_file_name = os.path.basename(project.file_doc.name)
        self.assertIn('testfile', actual_file_name)
        self.assertRedirects(response, reverse('clientprojects'))

    def test_post_project_post_non_numeric_prices(self):
        """
        Test posting a project with non-numeric prices.

        Asserts that no project is created and the correct template is used.
        """
        with open(self.test_file_path, 'rb') as test_file:
            attached_file = SimpleUploadedFile('testfile.txt', test_file.read())

        data = {
            'name': 'Test Project',
            'category': 'Test Category',
            'description': 'Test Description',
            'min_price': 'abc',
            'max_price': 'xyz',
            'attached_file': attached_file
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(Project.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_project/postproject.html')

    def test_post_project_post_negative_prices(self):
        """
        Test posting a project with negative prices.

        Asserts that no project is created and the correct template is used.
        """
        with open(self.test_file_path, 'rb') as test_file:
            attached_file = SimpleUploadedFile('testfile.txt', test_file.read())

        data = {
            'name': 'Test Project',
            'category': 'Test Category',
            'description': 'Test Description',
            'min_price': -100,
            'max_price': -200,
            'attached_file': attached_file
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(Project.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_project/postproject.html')

    def test_post_project_post_max_less_than_min(self):
        """
        Test posting a project with max price less than min price.

        Asserts that no project is created and the correct template is used.
        """
        with open(self.test_file_path, 'rb') as test_file:
            attached_file = SimpleUploadedFile('testfile.txt', test_file.read())

        data = {
            'name': 'Test Project',
            'category': 'Test Category',
            'description': 'Test Description',
            'min_price': 200,
            'max_price': 100,
            'attached_file': attached_file
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(Project.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_project/postproject.html')

    def test_post_project_post_missing_file(self):
        """
        Test posting a project with missing file.

        Asserts that no project is created and the correct template is used.
        """
        data = {
            'name': 'Test Project',
            'category': 'Test Category',
            'description': 'Test Description',
            'min_price': 100,
            'max_price': 200
        }

        response = self.client.post(self.url, data=data)
        self.assertEqual(Project.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_project/postproject.html')

    def test_post_project_post_not_authenticated(self):
        """
        Test posting a project when user is not authenticated.

        Asserts that the response is a redirect to the login page.
        """
        self.client.logout()
        with open(self.test_file_path, 'rb') as test_file:
            attached_file = SimpleUploadedFile('testfile.txt', test_file.read())

        data = {
            'name': 'Test Project',
            'category': 'Test Category',
            'description': 'Test Description',
            'min_price': 100,
            'max_price': 200,
            'attached_file': attached_file
        }

        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, f"{reverse('login')}?next={self.url}")

    def test_postproject_url_resolves(self):
        """
        Test that the 'postproject' URL resolves to the correct view.

        Asserts that the resolved view function is post_project.
        """
        url = reverse('postproject')
        self.assertEqual(resolve(url).func, post_project)
