import json
from bs4 import BeautifulSoup
import requests

def main():
    # with open('recipes.json') as file:
        # all_data = json.load(file)
        # for recipe in all_data:
            # print(json.dumps(recipe['calories'], indent=5))

    for i in range(6663, 27000):
        recipeId = i
        try:
            # url = "http://allrecipes.com/recipe/{}".format(recipeId)
            url = f'http://allrecipes.com/recipe/{recipeId}'
            page = requests.get(url)
            nutrition_page = requests.get(page.url + 'fullrecipenutrition/')
            nutrition_soup = BeautifulSoup(nutrition_page.content, "html.parser")
            nutrition_body = nutrition_soup.find('div', class_='nutrition-body')
            nutrition_rows = nutrition_body.find_all(class_='nutrition-row')

            for row in nutrition_rows:
                words = row.find(class_='nutrient-name').text.split(':')
                print(words)

            return

        except Exception as e:
            print(e)
        return



main()
