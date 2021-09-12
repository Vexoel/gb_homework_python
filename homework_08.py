# homework 8
# task 1
print("Task 1")
print()


class Date:
    __MONTHS_INFO = {1: (31, "Январь"), 2: (28, "Февраль"), 3: (31, "Март"), 4: (30, "Апрель"), 5: (31, "Май"),
                     6: (30, "Июнь"), 7: (31, "Июль"), 8: (31, "Август"), 9: (30, "Сентябрь"), 10: (31, "Октябрь"),
                     11: (30, "Ноябрь"), 12: (31, "Декабрь")}

    __num_y = 0
    __num_m = 0
    __num_d = 0

    def __init__(self, str_date=""):
        Date.str_to_date(str_date)

    @staticmethod
    def __check_int(i, key):
        try:
            num = int(i)
        except ValueError as err:
            raise ValueError(f"В поле {key} введено не число")

        return num

    @staticmethod
    def __check_year(y):
        num_y = Date.__check_int(y, "год")

        return num_y

    @staticmethod
    def __check_month(m):
        num_m = Date.__check_int(m, "месяц")

        if num_m > 12 or num_m < 1:
            raise ValueError("Значение поля месяц должно быть в диапозоне от 1 до 12 включительно")

        return num_m

    @staticmethod
    def __check_day(d):  # не стал заморачиваться с високосным годом
        num_d = Date.__check_int(d, "день")

        if num_d < 1 or num_d > Date.__MONTHS_INFO[Date.__num_m][0]:
            raise ValueError(
                f"Значение в поле день должно быть в диапозоне от 1 до {Date.__MONTHS_INFO[Date.__num_m][0]} включительно")

        return num_d

    @classmethod
    def str_to_date(cls, str_date=""):
        li = str_date.split(".")
        if len(li) != 3:
            raise ValueError("Формат строки должен соответствовать дд.мм.гггг")
        else:
            cls.__num_y = cls.__check_year(li[2])
            cls.__num_m = cls.__check_month(li[1])
            cls.__num_d = cls.__check_day(li[0])

            print(f"День {cls.__num_d}")
            print(f"Месяц {cls.__MONTHS_INFO[cls.__num_m][1]}")
            print(f"Год {cls.__num_y}")


# Проверка
print("ввод данных с консоли")
Date.str_to_date(input("Введите строку формата дд.мм.гггг: "))
print()

dict = {1: "01.02.2020", 2: "30022020", 3: "dd.mm.yyyy", 4: "30.02.2020", 5: "01.13.2020"}
for key, value in dict.items():
    print(f"тест {key}: {value}")
    try:
        Date.str_to_date(value)
    except ValueError as err:
        print(err)
    print()

# task 2
print()
print("Task 2")
print()


class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.txt = text


class MyDivision:
    @staticmethod
    def division(a, b):
        if b == 0:
            raise MyZeroDivisionError("Вы ввели ноль, на ноль делить нельзя")
        else:
            return a / b


# Проверка
while True:
    try:
        n = input("Введите целочисленный делитель (для выхода введите /):")

        if n == "/":
            break

        try:
            n = int(n)
        except ValueError:
            print("Введено не число")

            continue

        print(MyDivision.division(100, n))
    except MyZeroDivisionError as err:
        print(err)

# task 3
print()
print("Task 3")
print()


class MyValueError(Exception):
    def __init__(self, text):
        self.txt = text


class MyCollection:
    collection = []

    @classmethod
    def add(cls, p):
        try:
            cls.collection.append(float(p))
        except ValueError:
            raise MyValueError("Введено не число")


# Проверка
while True:
    n = input("Введите число (для выхода введите /):")

    if n == "/":
        break

    try:
        MyCollection.add(n)
    except MyValueError as err:
        print(err)

print(MyCollection.collection)

# task 4-6
print()
print("Task 4-6")
print()


class Warehouse:
    """Класс склад"""
    __str = ""

    def __init__(self, printers=[], scanners=[], copiers=[]):
        self.printers = printers
        self.scanners = scanners
        self.copiers = copiers
        self.stocktaking = {}

    def __str__(self):
        printer_str = ""
        for el in self.printers:
            printer_str += "    " + str(el) + "\n"

        scanner_str = ""
        for el in self.scanners:
            scanner_str += "    " + str(el) + "\n"

        copier_str = ""
        for el in self.copiers:
            copier_str += "    " + str(el) + "\n"

        stocktaking_str = ""
        for k, v in self.stocktaking.items():
            stocktaking_str += "  " + k + "\n"

            for el in v:
                stocktaking_str += "    " + el.str + " " + str(el) + "\n"

        return f"На складе:\n" \
               f"  Принтеров - {len(self.printers)}\n" \
               f"{printer_str}" \
               f"  Сканеров - {len(self.scanners)}\n" \
               f"{scanner_str}" \
               f"  Копиров - {len(self.copiers)}\n" \
               f"{copier_str}" \
               f"Выдано:\n" \
               f"{stocktaking_str}"

    def acceptance(self, *equips):
        """Метод для добавления оргтехники на склад"""

        for el in equips:
            fl = True

            if isinstance(el, Printer):
                self.printers.append(el)
            elif isinstance(el, Scanner):
                self.scanners.append(el)
            elif isinstance(el, Copier):
                self.copiers.append(el)
            else:
                fl = False

                print("Такую оргтехнику склад не принемает")

            if fl:
                print(el.str + " добавлен")

    def __distrib(self, unit, equips):
        if len(equips) > 0:
            el = equips.pop(0)

            try:
                self.stocktaking[unit].append(el)
            except KeyError:
                self.stocktaking[unit] = [el]
            finally:
                print(f"{el.str} выдан в {unit}")

                return True
        else:
            return False

    def distribute(self, unit, equip):
        """Метод передачи оргтехники подразделению"""

        if equip == Printer:
            if not self.__distrib(unit, self.printers):
                print(f"На складе закончились принтеры")
        elif equip == Scanner:
            if not self.__distrib(unit, self.scanners):
                print(f"На складе закончились сканеры")
        elif equip == Copier:
            if not self.__distrib(unit, self.copiers):
                print(f"На складе закончились копиры")
        else:
            print("На складе нет запрашиваемой техники")

    @staticmethod
    def info():
        print("Класс склад для хранения оргтехники")

    @classmethod
    def set_name(cls, name):
        cls.__str = name

    @classmethod
    def get_name(cls):
        return cls.__str


class OfficeEquipment:
    """Родительский класс - оргтехника"""

    str = "Оргтехника"

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    def __str__(self):
        return f"произоводитель: {self.manufacturer}, модель: {self.model}"

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def do(self):
        pass


class Printer(OfficeEquipment):
    """Дочерний класс оргтехники - принтер (доп параметр color=True\\False)"""

    str = "Принтер"

    def __init__(self, manufacturer, model, color=False):
        super().__init__(manufacturer, model)
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = False

        if isinstance(color, bool):
            self.__color = color

            print(f"{self.str} {self.__str__()} {'цветной' if self.color else 'черно-белый'}")
        else:
            print("Свойство color принимает только булевое значени")

    def do(self, pages=0):
        print(f"{'Черно-белая' if self.color else 'Цветная'} печать {pages} страниц")


class Scanner(OfficeEquipment):
    str = "Сканер"

    def __init__(self, manufacturer, model, resolution="600x1200"):
        super().__init__(manufacturer, model)
        self.resolution = resolution

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution):
        self.__resolution = "0x0"

        li = resolution.split("x")

        if len(li) == 2:
            iserr = False

            for el in li:
                try:
                    n = int(el)
                except ValueError:
                    iserr = True

                    break

            if not iserr:
                self.__resolution = resolution

                print(f"{self.str} {self.__str__()} с разрешением {self.resolution}")
            else:
                print("Разрешение должно быть формата WxH, где W и H должны быть целочисленными значениями")
        else:
            print("Введено не верное разрешение сканирования")

    def do(self, colorscan=False):
        print(f"{'Черно-белое' if colorscan else 'Цветное'} сканирование разрешением {self.resolution}")


class Copier(OfficeEquipment):
    str = "Копир"

    def __init__(self, manufacturer, model, speed=0):
        super().__init__(manufacturer, model)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = 0

        try:
            n = int(speed)
        except ValueError:
            print("Скорость печати должна быть целочисленным числом")
        else:
            if n < 0:
                print("Скорость печати не может быть отрицательной")
            else:
                self.__speed = n

                print(f"{self.str} {self.__str__()} со скоростью печати {self.speed} страниц в минуту")

    def do(self, colorcopy=False):
        print(f"{'Черно-белое' if colorcopy else 'Цветное'} копирование {self.speed} копий в минуту")


# Проверка
printers = [Printer("Brother", "1", True), Printer("LG", "2", False), Printer("LG", "2C", True)]
scanners = [Scanner("LG", "1", "600x1200")]
copiers = [Copier("Xerox", "3", 5), Copier("Xerox", "25", 100), Copier("HP", "2", 50)]

warehouse = Warehouse(printers, scanners, copiers)

warehouse.printers[0].do(2)
warehouse.scanners[0].do()
warehouse.copiers[0].do()

warehouse.printers[0].color = "a"
warehouse.printers[0].color = False

warehouse.scanners[0].resolution = "W"
warehouse.scanners[0].resolution = "WxH"
warehouse.scanners[0].resolution = "1200x2400"

warehouse.copiers[0].speed = "a"
warehouse.copiers[0].speed = -5
warehouse.copiers[0].speed = 20

print(warehouse)

warehouse.acceptance(Printer("Brother", "2", True), Scanner("LG", "4", "300x600"), Copier("HP", "100", 100))

print(warehouse)

warehouse.distribute("Подразделение1", Printer)
warehouse.distribute("Подразделение1", Copier)

print(warehouse)

warehouse.distribute("Подразделение2", Scanner)
warehouse.distribute("Подразделение2", Scanner)

warehouse.distribute("Подразделение3", Scanner)

print(warehouse)

Warehouse.info()

Warehouse.set_name("Warehouse")
print(Warehouse.get_name())

# task 7
print()
print("Task 7")
print()


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, float) or isinstance(x, int):
            self.__x = x
        else:
            raise ValueError("X должно быть вещественным числом")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, float) or isinstance(y, int):
            self.__y = y
        else:
            raise ValueError("Y должно быть вещественным числом")

    def __str__(self):
        return f"{self.x}{'+' if self.y > 0 else '-'}{abs(self.y)}i"

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ComplexNumber(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __truediv__(self, other):
        return ComplexNumber((self.x * other.x - self.y * other.y) / (other.x ** 2 + other.y ** 2),
                             (other.x * self.y - self.x * other.y) / (other.x ** 2 + other.y ** 2))


# Проверка
cn1 = ComplexNumber(3, 1)
cn2 = ComplexNumber(2, 3)
cn3 = cn1 + cn2
cn4 = cn1 - cn2
cn5 = cn1 * cn2
cn6 = cn1 / cn2
print(f"cn1 = {cn1}")
print(f"cn2 = {cn2}")
print(f"cn1 + cn2 = {cn3}")
print(f"cn1 - cn2 = {cn4}")
print(f"cn1 * cn2 = {cn5}")
print(f"cn1 / cn2 = {cn6}")
