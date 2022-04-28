#!/usr/bin/env python
# coding: utf-8

# In[52]:


def most_frequent(list):
    return max(set(list), key = list.count)
  

numbers = [1,2,1,2,3,2,1,4,2]
most_frequent(numbers)


# In[ ]:




