"""def min2(a,b):
    if a<=b:
        return a
    else:
        return b"""

"""def f(n):
    return n * 10 + 5
    """

"""def my_range(start,stop,step=1):
    res=[]
    if step>0:
        x=start
        while x<stop:
            res+=[x]
            x+=step
    elif step<0:
        x=start
        while x>stop:
            res+=[x]
            x+=step
    return res
print(my_range(1,5))"""

"""def f(x):
    if x<=-2:
        print(1-(x+2)**2)
    elif x>2:
        print((x-2)**2+1)
    else:
        print(-x/2)"""


"""def update_dictionary(d,key,value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key]=[]
        d[2*key].append(value)
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)


Оно же:

def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
        
        """


