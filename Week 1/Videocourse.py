
# coding: utf-8

# In[2]:


11111*1111111


# In[3]:


40//8


# In[4]:


42%5


# In[5]:


42//(4+2*(-2))


# In[6]:


2014**14


# In[9]:


1.2345e3



# In[10]:


1.2345e-3


# In[11]:


(2014.0)**14


# In[15]:


7/3


# In[16]:


7//3


# In[17]:


int(2.99)


# In[18]:


int(-1.6)


# In[19]:


9**19 - int(float(9**19))


# In[21]:


float(9**19)


# In[31]:


x=int(input())
h=int(input())
m=int(input())
print((x+h*60+m)//60)
print((x+h*60+m)%60)





# In[2]:


a = True
b = False
a and b or not a and not b


# In[9]:


a,b,h=int(input()),int(input()),int(input())

if a<=h<=b:
    print("Это нормально")
elif h>b:
    print("Пересып")
else:
    print("Недосып")


# In[13]:


a = int(input())
if ((a%4==0) and a%100!=0) or (a%400==0):
    print("Високосный")
else:
    print("Обычный")


# In[14]:


"123" + "42"


# In[16]:


a = int(input())
if (-15<a<=12) or (14<a<17) or (19<=a):
    print(True)
else:
    print(False)




