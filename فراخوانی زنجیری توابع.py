#!/usr/bin/env python
# coding: utf-8

# In[62]:


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9


# In[ ]:




