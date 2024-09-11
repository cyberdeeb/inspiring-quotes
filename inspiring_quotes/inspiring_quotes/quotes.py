import json
import random

def get_random_quote():
     with open('inspiring_quotes/inspiring_quotes/quotes_list.json', 'r') as file:
        quotes = json.load(file)
        return random.choice(quotes)
