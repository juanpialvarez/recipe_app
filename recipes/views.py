from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/main.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail.html"


def home(request):
    return render(request, "home/recipes_home.html")


@login_required
def records(request):
    form = RecipesSearchForm(request.POST or None)
    ingredient_df = None
    chart = None
    if request.method == "POST":
        ingredient = request.POST.get("ingredient")
        chart_type = request.POST.get("chart_type")
        print(ingredient, chart_type)
        objects_all = Recipe.objects.all()
        objects_ingredient = Recipe.objects.filter(ingredients__icontains=ingredient)
        if objects_ingredient:
            ingredient_df = pd.DataFrame(objects_ingredient.values())
            for a, ingredient in enumerate(ingredient_df["ingredients"]):
                ingredient_count = len(ingredient.split(", "))
                ingredient_df.loc[a, "ingredient_count"] = int(ingredient_count)
            ingredient_df = ingredient_df.drop("image", axis=1)
            objects_df = pd.DataFrame(objects_all.values())
            total_recipes = len(objects_df.index)
            chart = get_chart(chart_type, ingredient_df, total_recipes)
            ingredient_df = ingredient_df.to_html()
    context = {"form": form, "ingredient_df": ingredient_df, "chart": chart}
    return render(request, "records/records.html", context)
