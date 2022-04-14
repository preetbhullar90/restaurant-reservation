from django.test import TestCase
from menu.models import Meals, Category


class TestMenuModels(TestCase):

    def setUp(self):
        self.meals = Meals(name='name', description='description',
                           people='1', price='2', slug=True)
        self.category = Category(name='Test 1234')

    def test_create_slug_on(self):
        self.assertEquals(self.meals.slug, True)

    def test_create_meals(self):
        self.assertEquals(self.meals.name, 'name')
        self.assertEquals(self.meals.description, 'description')
        self.assertEquals(self.meals.people, '1')
        self.assertEquals(self.meals.price, '2')
        self.assertEquals(self.meals.slug, True)

    def test_create_category(self):
        self.assertEquals(self.category.name, 'Test 1234')

    def test_customer_save_works(self):
        category = self.category
        category.save()
        meals = len(Meals.objects.all())
        self.assertEquals(meals, 0)

    def test_category_works(self):
        category = len(Category.objects.all())
        self.assertEquals(category, 0)
