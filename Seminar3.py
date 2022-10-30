# -----------------------------------------ДЗ к семинару №3---------------------------------------------------------
#Задача №1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# from random import randint

# n = int(input("Введите размерность N "))
# min = int(input("Введите минимальное значение "))
# max = int(input("Введите максимальное значение "))

# lst = [randint(min, max) for i in range(n)]
# print(lst)

# lst_new = []
# i = 1
# while i < len(lst):
#     lst_new.append(lst[i])
#     i +=2
# k = sum(lst_new)
# print(f'Сумма элементов на нечётных позициях: {k}')

# Задача №2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# import math
# from random import randint

# n = int(input("Введите размерность N "))
# min = int(input("Введите минимальное значение "))
# max = int(input("Введите максимальное значение "))

# lst = [randint(min, max) for i in range(n)]
# lst_new = [lst[i]*lst[-i-1] for i in range(math.ceil(n/2))]
# print(f'{lst} => {lst_new}')

# Задача №3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# n = int(input("Введите размерность N "))
# lst = [float(input(f'Введите {i+1}-й элемент списка: ')) for i in range(n)]  

# fract_lst = []     
# for i in range(n):
#     if lst[i] < 0:
#         fract_lst.append(1 - lst[i]%1)
#     else:
#         fract_lst.append(lst[i]%1)

# fract_lst.sort() 
# for i in range(n):
#     if 0 in fract_lst:
#         fract_lst.remove(0.0) 

# if len(fract_lst) == 1:
#     diff  = fract_lst[0]
# else:
#     diff = (fract_lst[-1] - fract_lst[0]) 

# print(f'{lst} => {diff}')

#Задача №4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input("Введите число "))
# a = n
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(f'{a} -> {b} ')

#Задача №5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def fib(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

# k = abs(int(input('Введите количество элементов k ')))
# posfib = []
# negfib = []

# for i in range(0, k+1):
#     posfib.append(fib(i))
#     negfib.append(pow(-1, (i+1)) * fib(i))

# lst = []
# count = -1
# for i in range(2*k+1):
#     if count >= -k:
#         lst.insert(i, negfib[-i-1])
#         count -= 1
#     else:
#         lst.insert(i, posfib[i-k])
# print(lst)

