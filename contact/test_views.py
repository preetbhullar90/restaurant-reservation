from django.test import SimpleTestCase, Client
from django.urls import reverse
from django.core import mail


class TestContactViews(SimpleTestCase):
    def setUp(self):
        self.client = Client()
        self.contact_page_url = reverse('contact:send_email')

    def test_contact_page_GET(self):
        response = self.client.get(self.contact_page_url)
        self.assertEqual(response.status_code, 200)

    def test_contact_page_POST_sends_email(self):
        response = self.client.post(self.contact_page_url)

        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       )

        self.assertEquals(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
