my_int = 1

print(globals().keys())  # find my_int

# globals() содержит все переменные, функции, классы, которые мы можем использовать в нашем коде.

# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'my_int'])

print(globals().get('my_int'))
print(globals().get('__name__')) # __main__
print(globals().get('__doc__')) # None
print(globals().get('__file__')) # ...\python_beginners_course-main\_17_import\_1_standard_library.py

# import нужен для того, чтобы завести в локальное пространство нашего файла (модуля) другие библиотеки или другие файлы.
import random

my_list = [1, 2, 3]
print(random.choice(my_list))
print(globals().keys())

# чтобы посмотреть все функции/методы из импортированного модуля, можно использовать встроенную функцию dir(...)
print(dir(random))

import builtins

print(dir(builtins))  # find print, range, dict, list, etc.


