#!/usr/bin/env python
# coding: utf-8

# # Modified Double Double (Part 2)

# In[45]:


def multiply(sequence):
    total = []
    for element in sequence:
            total = total + [element*len(sequence)]
    return total


# In[52]:


multiply([3,2,4])


# This code multiplies each element of the sequence by the number of elements in the total sequence.

# In[ ]:




