from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # find appropriate view function
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)


# decode converts response bytes into unicode string, previously we compared bytes
# self.assertIn(b'<title>To-Do lists</title>', response.content)
# self.assertTrue(response.content.endswith(b'</html>'))
# self.assertTrue(response.content.strip().endswith(b'</html>')) (if problem with

def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST["item_text"] = 'A new list item'

    response = home_page(request)

    self.assertIn('A new list item', response.content.decode())  # setup, exercise, assert

# class Smoke(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)
