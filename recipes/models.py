from django.db import models


class Recipe(models.Model):
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

    def __str__(self):
        return str(self.name)
