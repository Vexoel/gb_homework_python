# homework 1
# task 1
print("task 1")
int_1 = 1
int_2 = 2
str_1 = "str_1"
str_2 = "str_2"

print(f"int_1 = {int_1}")
print(f"int_2 = {int_2}")
print(f"str_1 = '{str_1}'")
print(f"str_2 = '{str_2}'")

int_1 = int(input("Введите число: "))
int_2 = int(input("Введите число: "))
str_1 = input("Введите строку: ")
str_2 = input("Введите строку: ")

print(f"int_1 = {int_1}")
print(f"int_2 = {int_2}")
print(f"str_1 = '{str_1}'")
print(f"str_2 = '{str_2}'")

# task 2
print("task 2")
s = int(input("Введите кол-во секунд: "))
h = s // 3600
m = s % 3600 // 60
s = s % 3600 % 60

print("{:02}:{:02}:{:02}" .format(h, m, s))

# task 3
print("task 3")
int_1 = int(input("Введите число: "))

int_2 = 123 * int_1
print(int_2)

int_2 = 0
const = 3
i = const
while i > 0:
    int_2 = int_2 + 10 ** (const - i) * int_1 * i
    i -= 1
print(int_2)

# task 4
print("task 4")
max_num = 0

user_num = int(input("Введите положительное целочисленное число: "))
print("user_num = ", user_num)

iter = user_num // 10
while iter != 0:
    if user_num % 10 > max_num:
        max_num = user_num % 10
    user_num = iter
    iter = user_num // 10

if user_num % 10 > max_num:
    max_num = user_num % 10

print("max = ", max_num)

# task 5
print("task 5")
proceeds = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержек: "))
if proceeds > costs:
    print("Прибыль")
    profitability = (proceeds - costs) / proceeds
    print("Рентабельность выручки = ", profitability)
    cnt_employee = int(input("Кол-во сотрудников: "))
    profit_per_employee = (proceeds - costs) / cnt_employee
    print("Прибыль в расчете на одного сотрудника = ", profit_per_employee)
elif proceeds < costs:
    print("Убыток")
else:
    print("Ровно")

# task 6
print("task 6")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
cnt_day = 1
while a < b:
    a += a * 0.1
    cnt_day += 1
print(cnt_day)