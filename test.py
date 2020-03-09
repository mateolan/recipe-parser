import json

with open('recipes.json') as file:
    all_data = json.load(file)
    for recipe in all_data:
        print(json.dumps(recipe['servings'], indent=5))
