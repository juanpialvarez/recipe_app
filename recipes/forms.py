from django import forms

CHART__CHOICES = (
    ("#1", "Cooking Time"),
    ("#2", "Recipes with Ingredient"),
    ("#3", "Total ingredients"),
)


class RecipesSearchForm(forms.Form):
    ingredient = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
