# # 1) написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# def notebook():
#     todo_list = []
#
#     def add_todo():
#         nonlocal todo_list
#         todo = 0
#         while len(todo_list) < 5:
#             todo_list.append(input("Please enter any todos: "))
#             todo += 1
#
#         return todo_list
#
#     def get_all():
#         nonlocal add_todo
#         return add_todo()
#
#     return get_all
#
#
# todo_list = notebook()
#
# print(f"Here is your ToDo list: {todo_list()}")


# # 2) протипизировать первое задание
## !!! Не дуже розумію як типізувати( Дописав лише тип для Input
# def notebook():
#     todo_list = []
#
#     def add_todo():
#         nonlocal todo_list
#         todo = 0
#         while len(todo_list) < 5:
#             todo_list.append(input(str("Please enter any todos: ")))
#             todo += 1
#
#         return todo_list
#
#     def get_all():
#         nonlocal add_todo
#         return add_todo()
#
#     return get_all
#
#
# todo_list = notebook()
#
# print(f"Here is your ToDo list: {todo_list()}")

# # 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
# # !!! Це завдання я вкрав з нету. Не розумів взагалі як його зробити(
# def expanded_form(num):
#     s = []
#     i = len(str(num)) - 1
#     for n in str(num):
#         if n != "0":
#             s.append(n + "0" * i)
#         i -= 1
#     print(s)
#
#     return " + ".join(s)
#
#
# expanded_form(input("Please input number: "))

# # 4) создать декоратор который будет считать сколько раз была запущена функция и будет выводит это значение после каждого запуска функции
# count1 = 0
# count2 = 0
#
#
# def decor(func):
#     def inner(*args, **kwargs):
#         print("_________________")
#         # global count
#         # count += 1
#         # print(f"Count: {count}")
#         func(*args, **kwargs)
#         print("_________________")
#
#     return inner
#
#
# @decor
# def func1():
#     global count1
#     count1 += 1
#     print(f"Count: {count1}")
#     print("func1")
#
#
# @decor
# def func2():
#     global count2
#     count2 += 1
#     print(f"Count: {count2}")
#     print("funk2")
#
#
# func1()
# func1()
# func2()
# func1()
# func1()
# func2()
# func2()
