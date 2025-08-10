year = 2000

if year % 4 == 0 and year % 100 != 0:
    print("Year is leap")
elif year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")


# if not year % 4 and year % 100:
#     print("Year is leap")
# elif not year % 400:
#     print("Year is leap")
# else:
#     print("Year is not leap")


# Функция определения позиции квартиры относительно подъезда и этажа
def super_count(flat_number):
    entrance_number = (flat_number - 1) // 20 + 1
    floor_number = (flat_number - 1) % 20 // 4 + 1
    print(f"Квартира номер={flat_number} находится в {entrance_number} подъезде на {floor_number} этаже")


# Функция определения високостности года
def is_year_leap2(current_year):
    if current_year % 4 == 0 and current_year % 100 != 0:
        print(f'{current_year} year is leap')
    elif year % 400 == 0:
        print(f'{current_year} year is leap')
    else:
        print(f'{current_year} year is not leap')


def is_year_leap3(current_year):
    if not current_year % 4 and current_year % 100:
        print(f'{current_year} year is leap')
    elif not current_year % 400:
        print(f'{current_year} year is leap')
    else:
        print(f'{current_year} year is not leap')


def input_your_data():
    again_name = True
    again_age = True
    base_name = ""
    base_age = 0
    while again_name:
        name = input('Enter your name: ')
        if name:
            print(name)
            base_name = name
            again_name = False
        else:
            print(f"Your name {name} is empty.")

    while again_age:
        str_age = input('Enter your age: ')
        if str_age.isdigit():
            age = int(str_age)
            print(age)
            base_age = age
            again_age = False
        else:
            print(f"Your age {str_age} is not number.")
    print(f"Hello! You are {base_name} and you are {base_age} years old.")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Привет, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#      print_hi('PyCharm')
#      # input_your_data()
#      # super_count(20)
#      # is_year_leap2(1978)
#      # is_year_leap3(1978)