# homework 3
# task 1
print("task 1")
def input_num(text):
    while True:
        s = input(text)
        if s.isdigit():
            return int(s)

def my_division(p1, p2):
    try:
        res1 = p1 / p2
    except ZeroDivisionError:
        res1 = None
    try:
        res2 = p2 / p1
    except ZeroDivisionError:
        res2 = None
    return res1, res2

n1 = input_num("Введите первое число: ")
n2 = input_num("Введите второе число: ")
print(my_division(n1, n2))

# task 2
print("task 2")
def input_user_data(name="None", surname="None", year_of_birth=None, сurrent_city="None", email="None",
                    telephone="None"):
    print(f"Имя: {name}; Фамилия: {surname}; Год рождения: {year_of_birth}; Город проживания: {сurrent_city}; Адрес электронной почты: {email}; Телефон: {telephone}")

input_user_data(name="Александр", surname="Осотов", year_of_birth=1987, сurrent_city="Ижевск", telephone="+7(XXX)XXXXXXX")

# task 3
print("task 3")
def my_func(p1, p2, p3):
    li = [p1, p2, p3]
    li.sort()
    return sum(li[-2:])

print(my_func(1, 2, 3))
print(my_func(2, 1, 3))
print(my_func(2, 3, 1))
print(my_func(3, 2, 1))
print(my_func(3, 1, 2))
print(my_func(1, 3, 2))

# task 4
print("task 4")
def my_func1(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res

def my_func2(x, y):
    return x ** y

print(my_func1(2, -2))
print(my_func2(2, -2))

# task 5
print("task 5")
summa = 0
need_continue = True
while need_continue:
    for el in input("Введите список чисел через пробел ('/' - завершение): ").split():
        if el.isdigit():
            summa += int(el)
        elif el == "/":
            need_continue = False
            break
    print(summa)

# task 6
print("task 6")
def int_func(p_str):
    return p_str.capitalize()

res = ""
for el in input("Введите строку: ").split():
    s = int_func(el)
    res += s + " "
print(res[:len(res) - 1])
