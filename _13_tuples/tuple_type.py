# Tuple /ТАПЛ/ или кортежи - это неизменяемые списки.
# Они применяются только тогда, когда мы знаем что они не будут изменяться
# и они часто применяются с функциями.

user_roles = ("admin", "editor", "viewer")
print(user_roles)  # Outputs: ("admin", "editor", "viewer")

user_roles = ("admin", "editor", "viewer")
print(len(user_roles))  # Outputs: 3

for role in user_roles:
    print(role)

print("admin" in user_roles)  # Outputs: True
print("writer" in user_roles)  # Outputs: False

print(user_roles[1])  # Outputs: "admin"
# user_roles[1] = "author"  # TypeError: 'tuple' object does not support item assignment

# это ошибочное объявление кортежа, это просто строка:
not_tuple = ("apple")
print(type(not_tuple))  # Outputs: <class 'str'>

# кортеж из одного элемента объявляется с обязательной запятой в конце:
my_tuple = ("admin",)
print(type(my_tuple))  # Outputs: <class 'tuple'>

# деструктивное присваивание - распаковка кортежа, это когда каждый элемент кортежа "ложится" на указанную переменную:
user_roles = ("admin", "editor", "viewer")
role_1, role_2, role_3 = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
print(role_3)  # Outputs: "viewer"

# role_1, role_2 = user_roles  # ValueError: too many values to unpack (expected 2)
# role_1, role_2, role_3, role_4 = user_roles  # ValueError: not enough values to unpack (expected 4, got 3)


# Также, как и кортеж, можно распаковать и список!!!
user_roles = ["admin", "editor", "viewer"]  # with lists it works too
role_1, role_2, role_3 = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
print(role_3)  # Outputs: "viewer"

# _ - так мы просто пропускаем присваивание значение из кортежа третей переменной:
role_1, role_2, _ = user_roles
print(role_1)  # Outputs: "admin"
print(role_2)  # Outputs: "editor"
