#!/usr/bin/env python
# coding: utf-8

# In[37]:


from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb") # True


# In[40]:


from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb") #True


# In[ ]:




