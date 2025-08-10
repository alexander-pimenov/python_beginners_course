person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# если итерироваться по словарю в лоб, то возвращаются ключи:
for p in person:
    print(p)
    print(person[p])

# items() итерируемся по парам из словаря - возвращаются кортежи:
for item in person.items():
    print(item)
    print(type(item)) # <class 'tuple'> - кортеж
    key, value = item
    print(key)
    print(value)

for key, value in person.items():  # ('name', 'John')
    print(key)
    print(value)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

person_ext = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "emails": ['asd@asd.ty', 'qwe@zxc.vb'],
    "phones": ['123-45-67', '987-45-65'],
    "address": {
        "street": "Gogol st",
        "apartment": 55,
        "post_code": 123456
    }
}

for i in person_ext.items():
    print(i)

for value in person_ext.values():
    print(value)

person_ext["age"] = '123'
print(person_ext["age"])
print(type(person_ext["age"]))