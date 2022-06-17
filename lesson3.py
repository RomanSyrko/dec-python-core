# 1. Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.__area = x * y

    def __add__(self, other):
        return self.__area + other.__area

    def __sub__(self, other):
        return self.__area - other.__area

    def __eq__(self, other):
        return self.__area == other.__area

    def __ne__(self, other):
        return self.__area != other.__area

    def __gt__(self, other):
        return self.__area > other.__area

    def __lt__(self, other):
        return self.__area < other.__area

    def __len__(self):
        return self.x + self.y


rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(6, 8)

print(rectangle1 + rectangle2)
print(rectangle1 - rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)
print(rectangle1 > rectangle2)
print(rectangle1 < rectangle2)
print(len(rectangle1))
print(len(rectangle2))


# ________________________________________________________________________________________________________________________
# 2. создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, leg_size):
        super().__init__(name, age)
        self.leg_size = leg_size
        Cinderella.__count += 1

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name, age, size_found):
        super().__init__(name, age)
        self.size_found = size_found

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if self.size_found == cinderella.leg_size:
                print("_" * 34 + "\n")
                print(f"Congrats! Your Cinderella is: {cinderella.name}")
                print("_" * 34)
                return
        print("Not Found")


cinderellas_list = [
    Cinderella('Anna', 18, 36),
    Cinderella('Kate', 19, 35),
    Cinderella('Natalia', 20, 34),
    Cinderella('Inna', 18, 37),
    Cinderella('Maria', 21, 38),
    Cinderella('Olia', 22, 39),
    Cinderella('Yulia', 19, 34),
]

prince = Prince('Ivan', 30, 35)

prince.find_cinderella(cinderellas_list)

# # _______________________________________________________Additional_________________________________________________________________
# # 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# from abc import ABC, abstractmethod
#
#
# class Printable(ABC):
#     def print(self):
#         return print("Hello")
#
#
# # 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
#
# class Book(Printable):
#     def __init__(self, name):
#         self.name = name
#
#
# class Magazine(Printable):
#     def __init__(self, name):
#         self.name = name
#
#
# # 3) Створити клас Main в якому буде:
# # - змінна класу printable_list яка буде зберігати книжки та журнали
# # - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# # - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# # - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# class Main(Printable):
#     def printable_list(self, book, magazine):
#         self.book = book
#         self.magazine = magazine
#
#     def add(self, book, magazine):
#         self.book = book
#         self.magazine = magazine
#
#
#     def show_all_magazines(self):
#         Printable.print(self.magazine)
#
#     def show_all_books(self):
#         Printable.print(self.book)
#
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine2'))
# Main.add(Magazine('Magazine3'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines
# print('-' * 40)
# Main.show_all_books
