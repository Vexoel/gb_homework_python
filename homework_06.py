# homework 6
# task 1
print("Task 1")
print()

from time import sleep
from itertools import cycle

class TrafficLight:
    __COLORS = ("RED", "YELLOW", "GREEN")

    def __init__(self, red_s=7, yellow_s=2, green_s=5, cycles=5):
        self.__color = self.__COLORS[0]
        self.__length = len(self.__COLORS)
        self.__COLORS_WAIT = {self.__COLORS[0]: red_s, self.__COLORS[1]: yellow_s, self.__COLORS[2]: green_s}
        self.__cycles = cycles

    def get_current_color(self):
        return self.__color

    def running(self):
        for i, el in enumerate(cycle(self.__COLORS)):
            if i == self.__cycles * self.__length:
                break
            else:
                self.__color = el

            print(self.__color)
            sleep(self.__COLORS_WAIT[self.__color])


t = TrafficLight()
t.running()

# task 2
print()
print("Task 2")
print()

class Road:
    __WEIGHT = 25

    def __init__(self, length, width, depth):
        self._length = length
        self._width = width
        self._depth = depth

    def calculation(self):
        return self._length * self._width * self._depth * self.__WEIGHT

r = Road(5000, 20, 5)
print(r.calculation())

# task 3
print()
print("Task 3")
print()

class Worker:
    name = "NONE"
    surname = "NONE"
    position = "NONE"
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position("Василий", "Петров", "Дворник в Газпром", {"wage": 100000, "bonus": 100000})
print(p.get_full_name())
print(p.get_total_income())
print(p.name)
print(p.surname)
print(p.position)
print(p._income["wage"])
print(p._income["bonus"])

# task 4
print()
print("Task 4")
print()

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print(f"машина повернула {direction}")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("привышение скорости")
        else:
            super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("привышение скорости")
        else:
            super().show_speed()

class PoliceCar(Car):
    pass

tc = TownCar(50, "green", "Volkswagen Beetle", False)
sc = SportCar(350, "red", "Ferrari 812", False)
wc = WorkCar(50, "yellow", "Lada Vesta", False)
pc = PoliceCar(100, "gray", "UAZ", True)

print("TownCar")
print(tc.speed)
print(tc.name)
print(tc.color)
print(tc.is_police)
tc.go()
tc.turn("направо")
tc.stop()
tc.show_speed()

print()
print("SportCar")
print(sc.speed)
print(sc.name)
print(sc.color)
print(sc.is_police)
sc.go()
sc.turn("налево")
sc.stop()
sc.show_speed()

print()
print("WorkCar")
print(wc.speed)
print(wc.name)
print(wc.color)
print(wc.is_police)
wc.go()
wc.turn("назад")
wc.stop()
wc.show_speed()

print()
print("PoliceCar")
print(pc.speed)
print(pc.name)
print(pc.color)
print(pc.is_police)
pc.go()
pc.turn("в никуда")
pc.stop()
pc.show_speed()

# task 5
print()
print("Task 5")
print()

class Stationery:
    def __init__(self, title):
        self.title = title;

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Пишем.")

class Pencil(Stationery):
    def draw(self):
        print("Рисуем.")

class Handle(Stationery):
    def draw(self):
        print("Подчеркиваем.")

pen = Pen("Ручка")

pencil = Pencil("Карандаш")

handle = Handle("Маркер")

pen.draw()
pencil.draw()
handle.draw()
