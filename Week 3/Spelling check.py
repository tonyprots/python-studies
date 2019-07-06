# -*- coding: utf8 -*-
"""Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура:
первой строкой — количество d записей в списке известных слов,
после передаётся  d строк с одним словарным словом на строку,
затем — количество l строк текста,
после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
"""

d = int(input())
q = set()
for i in range(d):
    q.add(input().lower())
l = int(input())
w = []
t = []
for i in range(l):
    t = input().split()
    w.extend(t)
# print(q)
# print(w)
delq = set()
ww=w.copy()
for i in ww:
    if i in delq:
        w.remove(i)
    else:
        delq.add(i)
for i in w:
    if i.lower() not in q:
        print(i)