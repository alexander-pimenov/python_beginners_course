person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_married": True
}
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}

# Добавляем новый ключ-значение в словарь:
person["job"] = "Engineer"
print(person)  # Outputs: {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}

# Создаем пустой словарь и потом наполняем его:
person = {}  # or person = dict()
person["name"] = "John"
person["age"] = 30
person["city"] = "New York"
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # Outputs: 'John'
print(person.get("name"))  # Outputs: 'John'
# Если ключа нет, то вернется - None
print(person.get("country"))  # Outputs: None
# Так можно передавать дефолтное значение и если такого ключа нет, то вернется
# дефолтное значение, а если ключ есть, то вернется имеющееся значение, а не дефолтное:
print(person.get("country", "USA"))  # Outputs: USA
print(person.get("name", "Vasya"))  # Outputs: John
print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
