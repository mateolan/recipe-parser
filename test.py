import json

with open('recipes.json') as file:
    data = json.load(file)
    print(data)
