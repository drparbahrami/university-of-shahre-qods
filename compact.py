#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def compact(lst):
    return list(filter(bool, lst))
  
  
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]

