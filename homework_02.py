# homework 2
# task 1
types = ("<class 'int'>", "<class 'float'>")
li = [1, 1.1, complex(1, 1), '1', True, b"1", [11, 12], (21, 22), {1, 2}, {"31": 31, "32": 32}, None]
for el in li:
    print(type(el))

# task 2
li = []
while True:
    str = input("Введите элемент списка (для выхода введите exit): ")
    if str.lower() == "exit":
        break
    li.append(str)
print(li)

for i in range(0, len(li) - 1, 2):
    li[i], li[i + 1] = li[i + 1], li[i]
print(li)

# task 3
seasons_dict = {1: "Winter",
                2: "Winter",
                3: "Spring",
                4: "Spring",
                5: "Spring",
                6: "Summer",
                7: "Summer",
                8: "Summer",
                9: "Autumn",
                10: "Autumn",
                11: "Autumn",
                12: "Winter"}
seasons_li = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn",
              "Autumn", "Winter"]
print(seasons_dict)
print(seasons_li)

n = int(input("Введите номер месяца: "))

print(seasons_dict.get(n))
print(seasons_li[n - 1])

# task 4
li = input("Введите несколько слов через пробел: ").split()
for el in li:
    print(el[:10])

# task 5
li = []
while True:
    str = input("Введите натуральное число (для выхода введите exit): ")
    if str.lower() == "exit":
        break
    li.append(int(str))
print(li)

li.sort()
li.reverse()

print(li)

n = int(input("Введите новый элемент рейтинга: "))

idx = 0
for i in range(len(li)):
    if li[i] < n:
        idx = i
        break
    else:
        idx = i + 1

li.insert(idx, n)
print(li)
# li.append(n)
# li.sort()
# li.reverse()

# task 6
li = []
while True:
    str = input("Введите номер товара (для выхода введите exit): ")
    if str.lower() == "exit":
        break
    num = int(str)

    product_name = input("Введите название товара (для выхода введите exit): ")
    if product_name.lower() == "exit":
        break

    str = input("Введите цену товара (для выхода введите exit): ")
    if str.lower() == "exit":
        break
    price = int(str)

    str = input("Введите количество товара (для выхода введите exit): ")
    if str.lower() == "exit":
        break
    quantity = int(str)

    units = input("Введите единицы измерения товара (для выхода введите exit): ")
    if units.lower() == "exit":
        break

    co = (num, {"название": product_name, "цена": price, "количество": quantity, "ед": units})

    li.append(co)
print(li)

stat_dict = {}
for el in li:
    co = el[1]
    for k, v in co.items():
        try:
            stat_dict[k].append(v)
        except KeyError:
            stat_dict[k] = [v]
print(stat_dict)
