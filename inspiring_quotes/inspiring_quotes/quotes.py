import json
import random

def get_random_quote():
    try:
        with open('inspiring_quotes/inspiring_quotes/quotes_list.json', 'r') as file:
            quotes = json.load(file)
            return random.choice(quotes)
    except FileNotFoundError:
        print("The file 'quotes.json' does not exist.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
        return None