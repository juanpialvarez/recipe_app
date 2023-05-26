from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    cooking_time = models.IntegerField()
    difficulty_choices = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("intermediate", "Intermediate"),
        ("hard", "Hard"),
    )
    difficulty = models.CharField(max_length=20, choices=difficulty_choices)
    image = models.ImageField(upload_to="recipes", default="no_picture.png")

    def __str__(self):
        return str(self.name)
