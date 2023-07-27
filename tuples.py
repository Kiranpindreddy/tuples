#!/usr/bin/env python
# coding: utf-8

# In[2]:

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(sample_list, key=lambda x: (x[-1], sample_list.index(x)))
print(sorted_list)
# In[ ]:




