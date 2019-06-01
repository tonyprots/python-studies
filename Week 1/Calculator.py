# Калькулятор

a,b,c = float(input()),float(input()),input()
if c=="+":
    print(a+b)
elif c=="-":
    print(a - b)
elif c=="/" and b==0:
    print("Деление на 0!")
elif c == "/":
    print(a / b)
elif c=="*":
    print(a * b)
elif c=="mod" and b==0:
    print("Деление на 0!")
elif c == "mod":
    print(a % b)
elif c=="pow":
    print(a ** b)
elif c=="div" and b==0:
    print("Деление на 0!")
elif c=="div":
    print(a // b)