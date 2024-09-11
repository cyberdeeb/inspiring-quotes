import json
import random

def get_random_quote():
     with open('inspiring_quotes/quotes.json', 'r') as file:
        quotes = json.load(file)
        return random.choice(quotes)

print(get_random_quote())
