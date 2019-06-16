def modify_list(l):
    count=0
    del1=len(l)
    while count<del1:
        if l[count]%2!=0:
            l.pop(count)
            del1-=1
        else:
            l[count]=l[count]//2
            count+=1

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)