import spoonacular as sp
import re
import config

api = sp.API(config.api_key)

num_recipes = 25 

response = api.get_random_recipes(number=num_recipes)
data = response.json()

titles = open("data/titles.txt", "a+")
instructions = open("data/instructions.txt", "a+")
titles_and_instructions = open("data/titles_and_instructions.txt", "a+")

for i in range(num_recipes):
    title = data['recipes'][i]['title']
    steps = data['recipes'][i]['instructions']

    # remove extra whitespace
    steps = re.sub('\s+', ' ', steps).strip()

    # TODO: consider issue of adding spaces to floating point numbers
    # add spaces after periods
    steps = re.sub(r'\.(?! )', '. ', steps)

    print(title)
    print(steps)

    titles.write(title+'\n')
    instructions.write(steps+'\n')
    titles_and_instructions.write(title+'\n\n')
    titles_and_instructions.write(steps+'\n\n\n')

titles.close()
instructions.close()
titles_and_instructions.close()

instructions = open("data/instructions.txt", "r")
instructions_spaced = open("data/instructions_spaced.txt", "a+")

instructions_spaced.write(re.sub(r'([0-9]+)\.\n', r'\1.', re.sub('\.\s', '.\n', instructions.read())))


