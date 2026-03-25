from model.repository import RecipeRepository
from templates.list_template import render_list
from templates.detail_template import render_detail

class RecipeViews:
    def __init__(self):
        self.repo = RecipeRepository()

    def show_all(self):
        render_list(self.repo.get_all())

    def show_one(self, id):
        recipe = self.repo.get_one(id)
        render_detail(recipe)