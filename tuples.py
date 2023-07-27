#!/usr/bin/env python
# coding: utf-8

# In[2]:


user_input = input()
user_input = user_input.lower()
ascii_dict = {}
for char in user_input:
    if 'a' <= char <= 'z':
        ascii_dict[char] = ord(char)
print(ascii_dict)


# In[ ]:




