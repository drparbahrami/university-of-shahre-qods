#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]

