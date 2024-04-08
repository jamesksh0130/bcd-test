#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('employee.csv')
average_salary = df.groupby(["country", "sex"])["salary"].mean()

print(average_salary)


# In[ ]:




