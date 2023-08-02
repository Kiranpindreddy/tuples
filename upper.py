#!/usr/bin/env python
# coding: utf-8

# In[7]:


def count_upper_lower(input_str):
    upper_count = sum(1 for char in input_str if char.isupper())
    lower_count = sum(1 for char in input_str if char.islower())
    
    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

sample_string = "The quick Brow Fox"
count_upper_lower(sample_string)





