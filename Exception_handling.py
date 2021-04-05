#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Exception():
    try:
        a/b
        return a/b
    except:
        print("Zero division error")
a=int(input("Enter the number"))
b=int(input("Enter the number"))
Exception()


# In[2]:




subjects=["Americans ","Indians "]
verbs=["play ","watch "]
objects=["Baseball ","Cricket"]
Output=[ (i+j+ k) for i in subjects for j in verbs for k in objects ]
for a in Output:
    print(a)


# In[ ]:




