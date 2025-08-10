# функционал, когда функция возвращает несколько значений

# функция возвращает первым аргументом модифицированный словарь, а вторым параметр говорящий был ли словарь модифицирован:
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False
    print(f"dict={old_dict}")
    print(f"kwargs={kwargs}")
    for key, value in kwargs.items():
        print(f"key={key} value={value}")
        if old_dict.get(key) != value:
            # если в старом словаре нет того ключа, который приходит из kwargs, то этот ключ
            # будет добавлен в словарь, и как следствие, старый словарь модифицируется
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified


product = {"id": 1, "name": "Laptop", 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)
print(type(structure)) # <class 'tuple'>
print(structure) # {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}


# т.к. функция возвращает в кортеже два значения, то её возвращаемое значение
# можно сразу распаковать в две переменные:
product, was_modified = modify_dict(old_dict=product, in_stock=True)
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: True


product, was_modified = modify_dict(old_dict=product, id=1, name="Laptop")
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: False
