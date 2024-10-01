# nu1 = 5  #  первое число
# nu2 = 8  #  второе число
# nu1 -= nu2  #  отнимает щначение nu2 от nu1 и прибавляет жто к nu1
# print(nu1)  #
# nu1 *= nu2  #  nu2 * nu1 == nu1
# print(nu1)  #
# nu1 /= nu2  #  nu1 / nu2 == nu1
# print(nu1)  #
# nu1 %= nu2  #  делит по модулю операнды и присваисвает резкльтат nu1
# print(nu1)  #
# nu1 **= nu2  #  nu1 в степень nu2 == nu1
# print(nu1)  #
# nu1 //= nu2  # nu1 // nu2 == nu1
# print(nu1)  #
#
#
# num = [1, 2, 3, 4, 5, 6, 7]
# print(num[::-1])
# print(num[0::2])
# print(num[1::2])
# print(num[0])
# print(num[6])
# print(num[4])
# print(num[4::])
# print(num[-3:1:-1])
# print(num[2:5:1])
#
#
# numbers = list(map(int, input('введите числа через пробел: ').split()))
# number = int(input('введите искомое число: '))
# print(numbers.count(number))
#
#
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# num1 = int(input())
# num2 = int(input())
# print(list.append(num1))  # добавляет элемент в конец списка
# print(list.extend(num1))  # расширяет список лист, добавляя в конец все элементы списка
# print(list.insert(num1,num2)) # Вставляет на і-ый элемент значение х
# print(list.remove(num1)) # Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# print(list.pop(num1)) # Удаляет і-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# print(list.index(num1, num2)) # Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# print(list.count(num1)) # Возвращает количество элементов со значением х
# print(list.sort(num1)) # Сортирует список на основе функции
# print(list.reverse()) # разворачивает список
# print(list.copy()) # поверхнастная кеопия списка
# print(list.clear()) # очистить список


# try:
#     width = int(input('Введите ширину'))
#     longitude = int(input('Введите долготу'))
#     task = int(input('Введите номер задачи'))
#     if task == 1:
#         print(width + longitude * 2)
#     elif task == 2:
#         print(width + width + longitude + longitude)
#     elif task == 3:
#         radius = int(input('Введите радиус окружнасти'))
#         print(2*radius**3.14)
#     elif task >= 4:
#         print('Error:UnknowTasks')
# except:
#     print('Error:SymbholsError')


# import random
# matrix = [[random.randint(1,10)for i in range(8)] for j in range(9)]
# #
# for row in matrix:
#     for element in row:
#         print(element, end='\t')#Ставит в конце таб
#     print()#перенос строки


import random

g = int(input())
b = int(input())

matrix = [[random.randint(1, 10) for i in range(g)] for j in range(b)]
for row in matrix:
    for element in row:
        print(element, end='\t')
    print()