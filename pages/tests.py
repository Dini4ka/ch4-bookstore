from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageTest(SimpleTestCase):
    def SetUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'not home')

    def test_homepage_resolves_home_page_view(self):
        view = resolve('/')
        self.assertEqual(view.func, HomePageView.as_view())


class AboutPageTest(SimpleTestCase):
    def SetUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'not about')

    def test_aboutpage_resolves_about_page_view(self):
        view = resolve('/about')
        self.assertEqual(view.func, AboutPageView.as_view())

