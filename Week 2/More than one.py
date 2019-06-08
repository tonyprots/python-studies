"""Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным."""

q=input().split()
a=sorted(q)
b=[]
for i in range(1, len(a)):
    if a[i] == a[i-1]:
        if a[i] not in b:
            b.append(a[i])
for i in range(0, len(b)):
    print(b[i], end =' ')



""""
for i in range(len(q)):
    if (len(q)>0):
        if (len(q)>i+2) and (q[i+1]==q[i]) and (q[i+2]!=q[i+1]):
            s.append(q[i])
        else:
            if (q[-1]==q[-2]):
                s.append(q[-1])
            else:
                s.append(q[-1])
                s.append(q[-2])
for i in range(len(s)):
    print(s[i], end=" ")
"""

