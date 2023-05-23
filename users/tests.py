from django.test import TestCase
from .models import User


class UserTest(TestCase):
    def setUpTestData():
        User.objects.create(name="John Doe")

    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")
