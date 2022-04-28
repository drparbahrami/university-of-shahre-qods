#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_vowels(string):
    return [each for each in string if each in 'aeiou'] 


get_vowels('foobar') # ['o', 'o', 'a']
get_vowels('gym') # []

