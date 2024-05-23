import shutil
import tempfile
from django.test import TestCase, Client
from django.contrib.auth.models import User
from post_project.models import Project
from freelance_webpage.models import UserProfile
from django.urls import reverse
from justajob.settings import *
import os

class ProjectViewTestCase(TestCase):
    """
    Test suite for the client projects view.

    Attributes:
        client (Client): The test client for simulating HTTP requests.
        user (User): The user created for the test cases.
        user_profile (UserProfile): The user profile associated with the created user.
        url (str): The URL for the client projects view.
        test_image_path (str): The path to a test image used in the tests.
        temp_dir (str): The path to a temporary directory created for the tests.
        temp_image_path (str): The path to a copied test image in the temporary directory.
        project (Project): A project associated with the user created for the tests.
    """

    def setUp(self):
        """
        Set up the test environment.

        :return: None
        """
        # Create a user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser@email.com', password='testpassword')
        # Log in the user
        self.client.login(username='testuser@email.com', password='testpassword')
        self.url = reverse('clientprojects')
        self.test_image_path = os.path.join(BASE_DIR, 'client_pics', 'ab1.png')

        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()

        # Copy the test image to the temporary directory
        self.temp_image_path = os.path.join(self.temp_dir, 'ab1.png')
        shutil.copyfile(self.test_image_path, self.temp_image_path)

        # Create a user profile associated with the user
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            role='employer',
            country='Test Country',
            client_pic='client_pics/ab1.png'
        )

        # Create a project associated with the user
        self.project = Project.objects.create(
            user=self.user,
            project_name='Test Project',
            category='Test Category',
            project_description='Test Description',
            min_bid_price=100,
            max_bid_price=200
        )

    def tearDown(self):
        """
        Clean up after tests by removing any temporary directories and files created.

        :return: None
        """
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    def test_project_view_authenticated_with_projects(self):
        """
        Test accessing the client projects view while logged in with existing projects.

        :return: None
        :raises AssertionError: If the response status code is not 200, the correct template is not used, 
                               or the expected project details and user profile information are not rendered.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'post_project/clientprojects.html')
        # Check if project details are rendered correctly
        self.assertContains(response, 'Test Project')
        self.assertContains(response, 'Test Category')
        self.assertContains(response, 'Test Description')
        self.assertContains(response, '$100-200')
        # Check if user profile information is rendered correctly
        self.assertContains(response, 'Test Country')  # Check for country
        self.assertContains(response, '<img src="client_pics/ab1.png"')
