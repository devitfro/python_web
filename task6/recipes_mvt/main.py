from model.recipe import Recipe
from model.repository import RecipeRepository
from view.views import RecipeViews

repo = RecipeRepository()
view = RecipeViews()

repo.add(Recipe(1, "Pasta", "Easy pasta", ["pasta", "tomato"], "boil and mix"))
repo.add(Recipe(2, "Salad", "Fresh salad", ["cucumber", "tomato"], "cut and mix"))

view.show_all()
view.show_one(1)
repo.update(1, {"title": "Spaghetti"})

view.show_all()