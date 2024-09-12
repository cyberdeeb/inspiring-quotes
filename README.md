# inspiring_quotes

A simple Python package that provides random inspirational quotes. With a collection of 300 quotes, this library is perfect for adding a touch of motivation to your projects.

## Features

- Retrieve a random inspirational quote from a JSON file.
- Simple and easy to retrieve quote and author
- Over 300 inspiring quotes available

## Import the Library

```python
from inspiring_quotes1.quotes import get_random_quote
```

## Get a Random Quote

```python
quote = get_random_quote()
if quote:
    print(f"Quote: {quote['quote']}\nAuthor: {quote['author']}")
else:
    print("No quotes available.")
```
