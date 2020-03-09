import json
from bs4 import BeautifulSoup
import requests

# with open('recipes.json') as file:
    # all_data = json.load(file)
    # for recipe in all_data:
        # print(json.dumps(recipe['servings'], indent=5))

for i in range(6660, 27000):
    recipeId = i
    try:
        url = "http://allrecipes.com/recipe/{}".format(recipeId)
        page = requests.get(url)
        # print(page.status_code)
        soup = BeautifulSoup(page.content, "html.parser")
        servingspan = soup.find("span", class_="recipe-ingredients__header__toggles")
        # print(servingspan.prettify())
        metaElement = servingspan.find(id='metaRecipeServings')
        # print(metaElement)
        print(metaElement['content'])

    except Exception as e:
        print(e)



