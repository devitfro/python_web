import json
import os
from model.recipe import Recipe

class RecipeRepository:
    def __init__(self, filename="data/recipes.json"):
        self.filename = filename
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def add(self, recipe: Recipe):
        data = self._load()
        data.append(recipe.to_dict())
        self._save(data)

    def delete(self, recipe_id):
        data = self._load()
        data = [r for r in data if r["id"] != recipe_id]
        self._save(data)

    def update(self, recipe_id, new_data):
        data = self._load()
        for r in data:
            if r["id"] == recipe_id:
                r.update(new_data)
        self._save(data)

    def get_all(self):
        return self._load()

    def get_one(self, recipe_id):
        for r in self._load():
            if r["id"] == recipe_id:
                return r