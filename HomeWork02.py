"""
14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
"""

# Number = input('Введите число: ')
# Sum = 0
#
# for d in Number:
#     if d.isdigit():
#         Sum += int(d)
# print(Number, '-> ', Sum)

'''15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

# N = int(input('Введите число: '))
# Mult = 1
# list =[]
# for d in range(1,N+1):
#     Mult *= d
#     list.append(Mult)
# print(list)

'''16. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}'''

# n = int(input('Введите число: '))
# dict = {}
# Sum = 0
# for i in range(1, n + 1):
#      dict[i] = (1 + 1 / i) ** i
#      Sum += dict[i]
#
# print(dict)
# print(Sum)


'''18. Реализуйте алгоритм перемешивания списка.'''
import random

list = [1, 2, 3, 4, 5, 6]
random.shuffle(list)
print(list)
