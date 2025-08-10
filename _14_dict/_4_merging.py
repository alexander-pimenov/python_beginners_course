# объединение словарей:

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

# объединяем словари через метод update:
# если ключа нет, то он просто добавляется в обновленный словарь
# если ключ уже есть, то перезаписывается его значение.
person.update(additional_person_info)
print(person)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

# объединяем словари через символ пайп - | (это то же что и update()):
person_2 = person | additional_person_info
print(person_2)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
print(person)  # Outputs: {'city': 'New York', 'age': 30, 'name': 'John'}

person_3 = additional_person_info | person
print(person_3)  # Outputs: {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
