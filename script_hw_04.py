# homework 4
# task 1
from sys import argv

def is_digit(string):
    if string.isdigit():
       return float(string)
    else:
        try:
            return float(string)
        except ValueError:
            return -1

if len(argv) != 4:
    print("Введено не правильное количество параметров (введите параметры через пробел: отработано часов (N), ставка в час (H), премия в процентах (P))")
else:
    n, h, p = map(is_digit, argv[1:])

    if n == -1 or h == -1 or p == -1:
        print("Параметры должны быть числовыми")
    else:
        amount = n * h
        amount = amount + amount * p / 100
        print(amount)
