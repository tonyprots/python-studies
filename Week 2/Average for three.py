"""Напишите программу, которая считывает с клавиатуры два числа 𝑎 и 𝑏, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [𝑎;𝑏], которые делятся на 3.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12]. Всего чисел, делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.﻿
"""

a,b= int(input()),int(input())
s=0
q=0

for i in range(a,b+1):
    if i%3==0:
        s+=i
        q+=1
print(s/q)