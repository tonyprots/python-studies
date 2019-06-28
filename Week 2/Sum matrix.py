"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен
сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""

count = 0
x = []
end = ["end"]
while True:
    x.append([])
    x[count] = (input().split())
    count += 1
    if x[count - 1] == end:
        x.pop()
        break
y = []
stolbtsy = len(x[0])
stroki = len(x)
for i in range(stroki):
    y.append([])
    for j in range(stolbtsy):

        a = i - 1
        c = i + 1

        b = j - 1
        d = j + 1

        if i == 0:
            a = stroki - 1
        if j == 0:
            b = stolbtsy - 1

        if i == stroki - 1:
            c = 0
        if j == stolbtsy - 1:
            d = 0
        y[i].append(int(x[a][j]) + int(x[c][j]) + int(x[i][b]) + int(x[i][d]))

for i in range(len(y)):
    for j in range(len(y[0])):
        if j!=len(y[0])-1:
            print(y[i][j], end=" ")
        else: print(y[i][j], end="\n")

