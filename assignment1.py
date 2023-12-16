#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pass something return something
#oddeven
def evenorodd(num):
    return num%2
msg=evenorodd(9)
if msg:
    print ('odd')
else:
    print('even')


# In[13]:


def addition(a,b):
    c=a+b
    return c
a=4
b=9
result=addition(a,b)
print(result)


# In[14]:


def substraction(x,y):
    z=x-y
    return z
x=9
y=8
result=substraction(x,y)
print(result)


# In[15]:


def multiplication(k,a):
    v=k*a
    return v
k=3
a=2
res=multiplication(k,a)
print(res)


# In[17]:


def division(k,l):
    k=k*l
    return k
k=9
l=6
res=division(k,l)
print(res)


# In[18]:


def area_circle(radius):
    area=3.14*radius
    return area
radius=8
res=area_circle(radius)
print(res)


# In[19]:


def area_triangle(l,b):
    area=l*b
    return area
l=9
b=8
res=area_triangle(l,b)
print(res)


# In[21]:


def area_reactangle(w,h):
    area=w*h
    return area
w=7
h=6
res=area_reactangle(w,h)
print(res)


# In[22]:


def area_square(a):
    area=a*a
    return area
a=89
res=area_square(a)
print(res)


# In[24]:


#pass something return nothing
def addition(a,b):
    result=a+b
    print(result)
a=int(input('enter number'))
b=int(input('enter number'))


# In[25]:


addition(a,b)


# In[26]:


def substraction(a,b):
    result=a-b
    print(result)
a=int(input('enter number'))
b=int(input('enter number'))
substraction(a,b)


# In[27]:


def multiplication(x,y):
    result=x*y
    print(result)
x=int(input('enter number'))
y=int(input('enter number'))


# In[29]:


multiplication(x,y)


# In[31]:


def division(t,r):
    result=t/r
    print(result)
t=int(input('enter number'))
r=int(input('enter number'))


# In[32]:


division(t,r)


# In[43]:


def area_circle(radius):
    area=3.14*radius
    print(area)




# In[44]:


area_circle(6)


# In[45]:


def area_triangle(l,b):
    area=l*b
    print(area)


# In[48]:


area_triangle(8,8)


# In[49]:


def area_square(a):
    area=a*a
    print(area)


# In[50]:


area_square(7)


# In[51]:


def area_reactangle(h,w):
    area=h*w
    print(area)


# In[53]:


area_reactangle(6,89)


# In[54]:


def area_cube(a):
    area=6*a*a
    print(area)


# In[55]:


area_cube(4)


# In[ ]:


def addition():
    a=8
    b=7
    c=a+b
    print(c)


# In[ ]:


addition()


# In[ ]:




