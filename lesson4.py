# # 1) записать в новый текстовый файл только почты от gmail.com
# try:
#     string = '@gmail.com'
#     with open('Files/emails.txt', 'r') as file:
#         with open('Files/Gmails.txt', 'w') as file2:
#             for line in file:
#                 if string in line:
#                     file2.write(f'{line}')
# except Exception as err:
#     print(err)


# 2) для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

import json

try:
    print("Welcome To Shopping List!")
    print("Menu:")

    menu_options = {
        1: 'Create Shopping List',
        2: 'Show all Shopping List',
        3: 'Total amount of all purchases',
        4: 'The most expensive purchase',
        5: 'Search by purchase name',
        6: 'Exit',
    }


    def print_menu():
        for key in menu_options.keys():
            print(key, '--', menu_options[key])


    def option1():
        try:
            with open('Files/Shopping_list.txt', 'a') as file:
                print('Create shopping list:')
                num_items = input("How many items do you want?")
                my_list = []

                for x in range(int(num_items)):
                    item_name = input("Enter item name: ")
                    item_price = input("Enter item price: ")
                    my_tup = (item_price, item_name)
                    my_list.append(my_tup)

                for x in range(len(my_list)):
                    file.write(f'{my_list[x][1] + " = " + my_list[x][0] + "$"}\n')
        except FileNotFoundError as err:
            print(err)


    def option2():
        print(f'All Shopping List:\n')
        try:
            file = open('Files/Shopping_list.txt')
            try:
                print(file.read())
            finally:
                file.close()
        except FileNotFoundError as err:
            print(err)


    def option3():
        print(f'Total amount of all purchases\n')
        try:
            file = open('Files/Shopping_list.txt', 'r')
            try:
                print(file.read())

                # def sum_digits_string(str1):
                #     print(str1)
                #     sum_digit = 0
                #     for x in str1:
                #         if x.isdigit():
                #             z = int(x)
                #             sum_digit = sum_digit + z
                #
                #     return sum_digit
                #
                # print(f"Total: {sum_digits_string(open('Files/Shopping_list.txt'))}")
            finally:
                file.close()
        except FileNotFoundError as err:
            print(err)


    def option4():
        print(f'The most expensive purchase\n')
        try:
            file = open('Files/Shopping_list.txt')
            try:
                pass


            finally:
                file.close()
        except FileNotFoundError as err:
            print(err)


    def option5():
        print(f'Search by name\n')
        try:
            word = input(f'Find by name: ')
            with open('Files/Shopping_list.txt') as file:
                if word in file.read():
                    # print('Already added')
                    print(word)
                else:
                    print('Not found')
        except FileNotFoundError as err:
            print(err)


    if __name__ == '__main__':
        while (True):
            print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                option3()
            elif option == 4:
                option4()
            elif option == 5:
                option5()
            elif option == 6:
                print('BYE BYE')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 6.')

    menu = input(f"Chose number of menu: ")

except Exception as err:
    print(err)
