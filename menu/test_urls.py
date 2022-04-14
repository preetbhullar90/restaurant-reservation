from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import meal_list, meal_detail


class TestMenusUrls(SimpleTestCase):
    def test_meal_list_url_is_resolved(self):
        url = reverse('menu:meal_list')
        self.assertEquals(resolve(url).func, meal_list)

    def test_meal_detail_url_is_resolved(self):
        url = reverse('menu:meal_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, meal_detail)
