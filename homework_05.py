# homework 5
# task 1
print("Task 1")
print()
try:
    with open("homework_05_task_1.txt", "w", encoding="UTF-8") as f:
        while True:
            s = input("Введите строку для записи в файл (нажмите Enter без ввода для выхода): ")
            if s == "":
                break

            print(s, file=f)
except IOError:
    print("Произошла ошибка ввода-вывода!")

# task 2
print()
print("Task 2")
print()
try:
    with open("homework_05_task_2.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        print(f"Всего строк в файле {len(lines)}")
        for i, s in enumerate(lines):
            li = s.split()
            print(f"строка {i+1} слов {len(li)}")
except IOError:
    print("Произошла ошибка ввода-вывода!")

# task 3
print()
print("Task 3")
print()

# from functools import reduce

def get_employer(s):
    li = s.split()
    if len(li) != 2:
        surname = None
        salary = None
    else:
        surname = li[0]
        try:
            salary = float(li[1])
        except ValueError:
            salary = 0
    return {"surname": surname, "salary": salary}

# def sum_salary(a, b):
#     try:
#         salary_a = a["salary"]
#     except TypeError:
#         salary_a = a
#     salary_b = b["salary"]
#
#     return salary_a + salary_b

try:
    with open("homework_05_task_3.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        li = []

        print("Список сотрудников:")
        for i, s in enumerate(lines):
            li.append(get_employer(s))
            print(f"Сотрудник {li[i].get('surname')} оклад {li[i].get('salary')}")

        print()

        # avg_salary = reduce(sum_salary, li) / len(li)
        # print(f"Средняя величина дохода сотрудников: {avg_salary}")
        #
        # print()

        print("Список сотрудников с окладом меньше 20к:")
        avg_salary = 0
        for el in li:
            salary = el.get("salary")
            avg_salary +=  salary
            if salary < 20000:
               print(el.get("surname"))

        print()

        avg_salary = avg_salary / len(li)
        print(f"Средняя величина дохода всех сотрудников: {avg_salary}")
except IOError:
    print("Произошла ошибка ввода-вывода!")

# task 4
print()
print("Task 4")
print()
dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять"}
try:
    with open("homework_05_task_4_in.txt", "r", encoding="UTF-8") as f_in, open("homework_05_task_4_out.txt", "w", encoding="UTF-8") as f_out:
        for s in f_in:
            li = s.split()
            print(f"{dic.get(li[0])} {li[1]} {li[2]}")
            print(f"{dic.get(li[0])} {li[1]} {li[2]}", file=f_out)
except IOError:
    print("Произошла ошибка ввода-вывода!")

# task 5
from random import randint
print()
print("Task 5")
print()
try:
    with open("homework_05_task_5.txt", "w+", encoding="UTF-8") as f:
        for i in range(21):
            if i == 0:
                s = str(randint(0, 100))
            else:
                s = " " + str(randint(0, 10))
            f.write(s)

        f.seek(0)

        li = map(int, f.read().split())

        print(f"Сумма = {sum(li)}")
except IOError:
    print("Произошла ошибка ввода-вывода!")

# task 6
print()
print("Task 6")
print()
try:
    with open("homework_05_task_6.txt", "r", encoding="UTF-8") as f:
        dic = {}
        for line in f:
            li = line.split()
            lesson = li[0][0:-1]
            dic[lesson] = 0
            for i in range(1, len(li)):
                if li[i] == "-":
                    n = 0
                else:
                    n = int(li[i].split("(")[0])
                dic[lesson] += n
        print(dic)
except IOError:
    print("Произошла ошибка ввода-вывода!")

# task 7
import json
print()
print("Task 7")
print()
try:
    with open("homework_05_task_7.txt", "r", encoding="UTF-8") as f, open("homework_05_task_7.json", "w") as f_json:
        dic ={}
        li = f.readlines()
        for el in li:
            l = el.split()
            dic[l[0]] = float(l[2]) - float(l[3])

        avg = 0
        i = 0

        for val in dic.values():
            if val < 0:
                pass
            else:
                avg += val
                i += 1

        avg /= i

        res_li = [dic, {"average_profit": avg}]

        print(res_li)

        json.dump(res_li, f_json)
except IOError:
    print("Произошла ошибка ввода-вывода!")
