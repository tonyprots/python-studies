"""
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:

5
Sample Output:

 1  2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

n = int(input())

x = []
for i in range(n):
    x.append([])
    for j in range(n):
        x[i].append(1)

count = 1
for i in range(n):
    x[0][i] = count
    count += 1
cnt = 0

while True:
    if count > n * n:
        break
    for i in range(n - 1 - cnt * 2):
        x[i + 1 + cnt][n - 1 - cnt] = count
        count += 1
    if count > n * n:
        break
    for i in range(n - 2 - cnt, -1 + cnt, -1):
        x[n - 1 - cnt][i] = count
        count += 1
    if count > n * n:
        break
    for i in range(n - 2 - cnt, 0 + cnt, -1):
        x[i][0 + cnt] = count
        count += 1
    if count > n * n:
        break
    for i in range(1 + cnt, n - 1 - cnt):
        x[1 + cnt][i] = count
        count += 1
    if count > n * n:
        break
    cnt += 1

for i in x:
    for ii in i:
        print(ii, end=" ")
    print()

# Код, который ни к чему не привел:

"""
count = 1
round = -1
round_x = 1

while round<2:
    round += 1
    while count != (n * (round_x)):
        x[round][count % n - 1] = count
        count += 1
        if count > (n * n):
            break

    while count != (n * 2 + (n * (round + 1) + 4) * round):
        x[count % n][n - 1] = count
        count += 1
        if count > (n * n):
            break
    count_n = 0
    count += -1

    while count < (n * 2 * (round + 1) + n - 2 +round*2):
        print(n * 2 * (round + 1) + n - 2 +round*2, count - n - count_n - n*(round+round)-round*4, count_n, count)
        x[n - 1 - round][count - n - count_n - n*(round+round)-round*4] = count
        count += 1
        count_n += 2
        if count > (n * n):
            break
    count_n = 0

    while count != (n - 1) * (4 + round * 2) + 1:
        #print(count - n * 2 * (round + 1) - 2 - count_n, count)
        x[count - n * 2 * (round + 1) - 2 - count_n][round] = count
        count += 1
        count_n += 2
        if count > (n * n):
            break
        round_x = 4

for line in x:
    print(line, end="\n")


round = 0
while count!=(n+1):
    x[0][count-1]=count
    count+=1
round = 1
while count!=(n*2):
    x[count%n][n-1]=count
    count+=1
count_n=0
count+=-1
round = 3
while count!=(n*3-1):
    x[n-1][count-n-count_n]=count
    count+=1
    count_n+=2
count_n=0
round = 4
while count!=(n-1)*4+1:
    x[count-n*2-1-count_n][0]=count
    count+=1
    count_n+=2
print(*x)
"""
