from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

# Create your tests here.


class SmokeTest(TestCase):

    def test_bad(self):
        self.assertEqual(1, 1)


class HomePageTest(TestCase):
    """docstring for HomePageTest"""

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

        
