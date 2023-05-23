from django.test import TestCase
from .models import Recipe

class RecipeTest(TestCase):
    def setUpTestData():
       Recipe.objects.create(name='Salad', ingredients='Lettuce, tomato, dressing, onion, crackers', cooking_time=5, difficulty='easy')
    def test_recipe_name(self):
       book = Recipe.objects.get(id=1)
       field_label = book._meta.get_field('name').verbose_name
       self.assertEqual(field_label, 'name')
    def test_ingredients_max_length(self):
       book = Recipe.objects.get(id=1)
       max_length = book._meta.get_field('ingredients').max_length
       self.assertEqual(max_length, 255)