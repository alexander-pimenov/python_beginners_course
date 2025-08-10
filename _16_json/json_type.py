import json

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
}

# convert into JSON:
json_string = json.dumps(book)
print(type(json_string))
print(json_string)  # Outputs: {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}



# так можно создавать строки вида JSON:
json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}'

json_str = """
    {
        "title": "1984", 
        "author": "George Orwell", 
        "isbn": "978-0451524935", 
        "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    }
"""



book = json.loads(json_string)
print(type(book))
print(book)  # Outputs: {'title': '1984', 'author': 'George Orwell', 'isbn': '978-0451524935', 'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'}


book_2 = json.loads(json_str)
print(type(book_2))
print(book_2)  # Outputs: {'title': '1984', 'author': 'George Orwell', 'isbn': '978-0451524935', 'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'}


book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
    'count': 30,
    'genres': ['dystopia', 'foo']
}

json_string = json.dumps(book)
print(type(json_string))
print(json_string)  # Outputs: {"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "count": 30, "genres": ["dystopia"]}