from django.test import TestCase
from django.urls import reverse

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
