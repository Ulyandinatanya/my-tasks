#!/usr/bin/env python
# coding: utf-8

# In[10]:


import math
 
print("Введите координаты точки и радиус круга")
x = float(input("x = "))
y = float(input("y = "))
r_circle = float(input("R = "))
 
hypotenuse = math.sqrt(x ** 2 + y ** 2)
 
if hypotenuse <= r_circle:
    print("точка внутри")
else:
    print("точка снаружи")


# In[ ]:




