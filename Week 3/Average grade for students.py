"""Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
"""
a=[]
q=[]
count=0
sum1,sum2,sum3=0,0,0
with open ('../Week 3/dataset2.txt') as inf:
    for line in inf:
        s = line.strip().split(';')
        a.append(s)
for i in a:
    sum1 += float(i[1])
    sum2 += float(i[2])
    sum3 += float(i[3])
    count+=1
    print((float(i[1])+float(i[2])+float(i[3]))/3)
print(sum1/count, sum2/count, sum3/count)