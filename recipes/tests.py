from django.test import TestCase
from .models import Recipe
from http import HTTPStatus
from .forms import RecipesSearchForm


class RecipeTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name="Salad",
            ingredients="Lettuce, tomato, dressing, onion, crackers",
            cooking_time=5,
            difficulty="easy",
        )

    def test_recipe_name(self):
        book = Recipe.objects.get(id=1)
        field_label = book._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_ingredients_max_length(self):
        book = Recipe.objects.get(id=1)
        max_length = book._meta.get_field("ingredients").max_length
        self.assertEqual(max_length, 255)

    def test_get_absolute_url(self):
        book = Recipe.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), "/recipes/1")


class RecipeFormTest(TestCase):
    def test_form(self):
        form_data = {"ingredient": "water", "chart_type": "#1"}
        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
