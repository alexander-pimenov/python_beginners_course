# это используется, когда нужно передать список элементов, но мы не знаем какое их количество
# точно передадут
# 1,2,3; 1,1,1,22,3,5;
def add_all(*args):
    print(args)
    print(type(args))  # <class 'tuple'> - кортеж
    summary = 0
    for num in args:
        summary += num
    return summary


print(add_all(1, 2, 3))  # Outputs: 6
print(add_all(1, 2, 3, 4, 5))  # Outputs: 15

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

# используем символ * для передачи массивов чисел (списков) в функцию, которая принимает args:
print(add_all(*values))  # Outputs: 15
print(add_all(*values, *other_values))  # Outputs: 55


# передача в функцию именованных аргументов:
def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(f"key={key} value={value}")


# в эту функцию можно передать любое количество именованных аргументов и еще можно и разных типов:
introduce(name="John", age=30, city="New York")
# {'city': 'New York', 'age': 30, 'name': 'John'}
# <class 'dict'>

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

# так передаем с помощью ** в функцию с kwargs словарь:
introduce(**person)


def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)


func_with_all_arguments(3, 4, 5, 6, 7, 8, 9, **person)
# 3 4
# (5, 6, 7, 8, 9)
# 6
# {'city': 'New York', 'age': 30, 'name': 'John'}


func_with_all_arguments(x=1, y=2, *[3, 4, 5, 6, 7, 8, 9], **person)
