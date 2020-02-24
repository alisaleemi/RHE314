#!/usr/bin/env python
# coding: utf-8

# # Program 1

# In[31]:


def iterate(sequence):
    iterated = []
    for element in sequence:
        iterated = iterated + [element+1]
    print('The function uses iteration to go from ' + str(sequence) + ' to ' + str(iterated))


# In[32]:


iterate([3,4,6])


# This program is a very simple program that explains iteration and uses casting to print out lists. I specifically defined the function as "iterate", so that the new programming student knows that iteration is the word for what is happening to the sequence that they input. I had the function create a new sequence called "iterated", to let the student know that the new sequence that the program returns is the iterated version of the one they input originally. Finally, instead of just printing the iterated sequence, I thought it would be easier to explain in words what happened to the sequence, so I had it print out a sentence in a string form. I came across a problem where I had an error that told me I could not concatenate strings and sequences, so I used casting to convert the sequences into string by adding str(). This program is good for teaching a new programmer the basics of iteration and casting data types.

# In[ ]:




