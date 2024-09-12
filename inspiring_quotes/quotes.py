import json
import random
import importlib.resources as pkg_resources  # Importlib resources

def get_random_quote():
    try:
        # Using importlib.resources.files to get the file
        with pkg_resources.files(__package__).joinpath('quotes_list.json').open('r') as file:
            quotes = json.load(file)
            return random.choice(quotes)
    except FileNotFoundError:
        print("The file 'quotes_list.json' does not exist.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
        return None

