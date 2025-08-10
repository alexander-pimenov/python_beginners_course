range_object = range(10)
print(range_object)
numbers = list(range_object)
print(numbers)  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


my_range = range(1, 10)
print(list(my_range))  # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]


my_range = range(1, 10, 2)
print(list(my_range))  # Outputs: [1, 3, 5, 7, 9]


my_range = range(10, 1, -1)
print(list(my_range))  # Outputs: [10, 9, 8, 7, 6, 5, 4, 3, 2]
my_range2 = range(10, 1, -3)
print(list(my_range2))  # Outputs: [10, 7, 4]


numbers = [11, 21, 31, 41, 51, 61, 71, 81, 91]
for number in numbers:
    number = number + 1
    print(f"updated number: {number}")
# но целое число в индексе не изменится!!!:
print(numbers)  # Outputs: [11, 21, 31, 41, 51, 61, 71, 81, 91] It doesn't work!


numbers = [18, 28, 38, 48, 58, 68, 78, 88, 98]
for i in range(len(numbers)):
    # выведем индексы элементов массива:
    numbers[i] += 1
    print(f"под индексом {i} теперь стоит элемент массива {numbers[i]}")
print(numbers) # [19, 29, 39, 49, 59, 69, 79, 89, 99]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
    numbers[i] += 1
print(numbers)


greeting = 'Hello, World!'
indexes = []
letter = 'o'
count = 0
for i in range(len(greeting)):
    if greeting[i] == letter:
        indexes.append(i)
        count += 1
print(count)  # Outputs: 2
print(indexes)  # Outputs: [4, 8]
