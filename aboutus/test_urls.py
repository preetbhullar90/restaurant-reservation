from django.test import SimpleTestCase
from django.urls import reverse, resolve
from aboutus.views import aboutus_list


class TestAboutusUrls(SimpleTestCase):
    def test_aboutus_list_url_is_resolved(self):
        url = reverse('aboutus:aboutus_list')
        self.assertEquals(resolve(url).func, aboutus_list)
