"""Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный."""

"""
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
"""
from math import ceil
def parting(xs, parts):
    part_len = ceil(len(xs)/parts)
    return [xs[part_len*k:part_len*(k+1)] for k in range(parts)]

n = int(input())

q=[]
s=[]
for i in range(n):
    q.append(input().split(sep=";"))

for i in q:
    s.append(parting(i,2))
teams=[]
games=[]
wins=[]
draws=[]
loses=[]
score=[]
for i in s:
    for ii in i:
        if ii[0] not in teams:
            teams.append(ii[0])
            games.append(1)
            wins.append(0)
            draws.append(0)
            loses.append(0)
            score.append(0)
        else:
            games[teams.index(ii[0])]=int(games[teams.index(ii[0])])+1
for i in s:
    if i[0][1]>i[1][1]:
        wins[teams.index(i[0][0])] = int(wins[teams.index(i[0][0])]) + 1
        loses[teams.index(i[1][0])] = int(loses[teams.index(i[1][0])]) + 1
    elif i[0][1]==i[1][1]:
        draws[teams.index(i[0][0])] = int(draws[teams.index(i[0][0])]) + 1
        draws[teams.index(i[1][0])] = int(draws[teams.index(i[1][0])]) + 1
    else:
        loses[teams.index(i[0][0])] = int(loses[teams.index(i[0][0])]) + 1
        wins[teams.index(i[1][0])] = int(wins[teams.index(i[1][0])]) + 1
#Команда:Всего_игр Побед Ничьих Поражений Всего_очков
count=-1
for i in teams:
    count+=1
    print(i + ':', games[count],wins[count],draws[count],loses[count], int(wins[count])*3+int(draws[count]))
