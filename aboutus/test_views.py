from django.test import TestCase, Client
from django.urls import reverse


class TestAboutusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.menus_url = reverse('aboutus:aboutus_list')

    def test_aboutus_GET(self):
        response = self.client.get(self.menus_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus/about.html')
