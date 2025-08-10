file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
for file_name in file_names:
    print(file_name)

# если в цикл положить сроку, то она автоматически преобразуется в список символов (чар):
greeting = 'Hello, World!' # -> ['H', 'e', 'l', 'l', . . . . . ]
for char in greeting:
    print(char)


greeting = 'Hello, World!'
count_o = 0
for char in greeting:
    if char == 'o':
        # count_o = count_o + 1
        count_o += 1
print(count_o)


students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
    print(student)
    for char in student:
        print(char)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    # Skip odd numbers
    if num % 2 != 0:
        continue
    elif num % 3 == 0:
        continue
    print(num) # 2 4 8 10 14


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in numbers:
    # Break the loop if the number is 10
    if num == 10:
        break
    print(num)
