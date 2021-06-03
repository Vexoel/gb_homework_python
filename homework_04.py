# homework 4
from random import randint
from functools import reduce
from itertools import count
from itertools import cycle

# task 2
print("task 2")
li = [randint(1, 1000) for i in range(randint(1, 100))]
res_li = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]
print(li)
print(res_li)

# task 3
print("task 3")
li = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(li)

# task 4
print("task 4")
li = [randint(1, 10) for i in range(randint(1, 20))]
print(li)
res_li = [li[i] for i in range(0, len(li)) if li.count(li[i]) == 1]
print(res_li)

# task 5
print("task 5")
def reduce_func(a, b):
    return a * b

li = [i for i in range(100, 1001) if i % 2 == 0]
print(li)
print(reduce(reduce_func, li))

# task 6
print("task 6")
def iter_count(start):
    li = []

    for el in count(start):
        if el == start + 20:
            break
        else:
            li.append(el)

    return li

def iter_cycle(li):
    res_li = []

    length = len(li)

    for i, el in enumerate(cycle(li)):
        if i == 5 * length:
            break
        else:
            res_li.append(el)

    return res_li

print(iter_count(2))

print(iter_cycle("QWERTY"))

# task 7
print("task 7")
def fact_gen(n):
    li = []

    for i in range(0, n + 1):
        try:
            li.append(li[len(li) - 1] * (1 if i == 0 else i))
        except:
            li.append(1)

        yield li[len(li) - 1]

for i, el in enumerate(fact_gen(7)):
    print(f"{i}! = {el}")