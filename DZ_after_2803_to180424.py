# -*- coding: utf-8 -*-
import math
"""Реализация факториала циклами while, for, рекурсией"""

numfact = int(input("Введите число факториал которого хотите рассчитать: "))

# Первый вариант при помощи данного цикла
n = 1
whilefact = 1

while n <= numfact:

    whilefact = whilefact * n
    n += 1

print(f"Факториал рассчитанный при помощи цикла while числа {numfact} равен {whilefact} (первый вариант).")
print("Проверка при помощи модуля math: ", math.factorial(numfact))

# Второй вариант при помощи давнного цикла
n = 1
whilefact = 1
while n < numfact:
    n += 1
    whilefact = whilefact * n

print(f"Факториал рассчитанный при помощи цикла while числа {numfact} равен {whilefact} (второй вариант).")
print("Проверка при помощи модуля math: ", math.factorial(numfact))

# Рассчет факториала при помощи for

forfact = 1
for i in range(1, numfact + 1):
    forfact = forfact * i
print(f"Факториал рассчитанный при помощи цикла for числа {numfact} равен {forfact}.")

# Факториал расчитанный при помощи рекурсии

def recus_fact(numfact):
    if numfact == 1:
        return numfact
    else:
        return recus_fact(numfact - 1) * numfact

print(f"Факториал рассчитанный при помощи рекурсии {recus_fact(numfact)}.")

# Рассчет числа Фибоначчи при помощи циклов while и for и рекурсии

numfibo = int(input("Введите число для последовательности Фибоначчи: "))

for ik in range(1, numfibo + 1):
    if ik == 1:
        fibka = 0
    elif ik == 2:
        fibka = 1
        fibka2 = fibka
        fibka1 = 0
    else:
        fibka = fibka2 + fibka1
        fibka1 = fibka2
        fibka2 = fibka
    print(fibka)
print(f"Один из возможных вариантов для цикла for рассчет числа Фибоначчи из {numfibo} равно {fibka}")

i = 1
while i <= numfibo:
    if i == 1:
        fibkaW = 0
    elif i == 2:
        fibkaW = 1
        fibka2 = fibkaW
        fibka1 = 0
    else:
        fibkaW = fibka2 + fibka1
        fibka1 = fibka2
        fibka2 = fibkaW
    print(i, fibkaW)
    i += 1

print(f"Один из возможных вариантов для цикла while рассчет числа Фибоначчи из {numfibo} равно {fibkaW}")


def fibonachchy(im):
    if im < 2:
        return im
    return fibonachchy(im - 1) + fibonachchy(im - 2)
for im in range(numfibo):
    print(f"Рассчет чисел Фибоначчи с помощью рекурсии (вариант 1) {fibonachchy(im)}.")

# Свой метод max

def my_max(list_rand):
    nmm = sorted(list_rand)
    for i in range(len(nmm)):
        if nmm[i - 1] > nmm[i]:
            max_from_list = nmm[i - 1]
    return max_from_list

list_rand = [1, 6, 56, 7, 48, 34, 90]
print(my_max(list_rand))
print(max(list_rand))




