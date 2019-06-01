n = int(input())
a = n%10
b = int((n%100-a)/10)
c = int((n%1000-a-b)/100)
d = int((n%10000-a-b-c)/1000)
e = int((n%100000-a-b-c-d)/10000)
f = int((n%1000000-a-b-c-d-e)/100000)

if a+b+c==d+e+f:
    print("Счастливый")
else:
    print ("Обычный")
