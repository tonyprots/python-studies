w=[]
with open('../Week 3/dataset.txt') as inf:
    q = inf.readlines()
# q = "abc a bCd bC AbC BC BCD bcd ABC"
print(q)
for i in q:
    w +=i.split()
print(w)
count=0
for i in w:
    w[count]=i.lower()
    count+=1
s = w
print(s)
s.sort()
count = 0
key = ""
check = ""
for i in s:
    if s.count(i) > count:
        count = s.count(i)
        key = i
    if s.count(i) == count:
        check = i
if check < i:
    key = check
print(key, count)
