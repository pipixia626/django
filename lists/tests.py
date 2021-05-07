from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        #resolve是Django用来解析URL的function
        #当调用'/'时，网站的根目录找到一个名为home_page的function

        found = resolve('/')
        self.assertEqual(found.func,home_page)
    

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))