from django.urls import path
from .views import home, RecipeDetailView, RecipeListView, records


app_name = "recipes"

urlpatterns = [
    path("", home),
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("records/", records, name="records"),
]
