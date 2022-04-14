from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contact.views import send_email


class TestContactUrls(SimpleTestCase):
    def test_send_email_url_is_resolved(self):
        url = reverse('contact:send_email')
        self.assertEquals(resolve(url).func, send_email)
