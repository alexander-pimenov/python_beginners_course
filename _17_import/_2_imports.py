#


# так импортируются методы из других модулей:

#  1) конкретные функции
from _17_import.math_operations import add, subtract

print(add(1, 2))
print(subtract(2, 1))

#  2) такой вариант импорта лучший - весь модуль math_operations и вызывать методы через имя модуля
from _17_import import math_operations

print(math_operations.add(1, 2))

# 3) если делать так, то можно получить конфликт переменных/методов
from _17_import.math_operations import *  # don't do this

print(add(4, 5))
print(subtract(4, 5))

# в таком случае мы можем использовать функцию из другого модуля без конфликтов имен, т.к. мы переопределяем
# название импортируемой функции add в addition
from _17_import.math_operations import add as addition

print(addition(4, 5))

#
from math_operations import add, subtract  # possible, but not recommended
print(add(4, 5))
print(subtract(4, 5))

from .._15_function_advanced._2_return_mutiple_values import modify_dict  # possible, but not recommended

# file init.py говорит о том что вся папка является питоновским пакетом и её можно импортировать.

