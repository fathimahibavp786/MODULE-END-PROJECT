#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as pt


# In[4]:


import seaborn as sns


# In[5]:


import re


# In[6]:


import io


# In[7]:


df=pd.read_csv('myexcel.csv.csv')
df


# In[8]:


df.info()


# In[9]:


df.fillna('Unknown')


# In[10]:


df.describe()


# In[11]:


df.describe(include="all")


# In[12]:


df.shape


# In[13]:


df.head(15)


# In[14]:


df.tail(10)


# In[15]:


df.isnull()


# In[16]:


df[['Name','Team']]


# In[17]:


df.isnull().sum()


# In[18]:


df["Salary"].fillna(0,inplace=True)


# In[19]:


df.head(25)


# In[20]:


df['College'].fillna('Unknown',inplace=True)


# In[21]:


df['Team'].value_counts()


# In[22]:


df['Height']


# In[23]:


df['Height']=np.random.uniform(150,180,size=len(df))
df


# In[24]:


#1.How many are there in each Team and the percentage splitting with respect to the total employees.


# In[25]:


df1=df[['Name','Team']]
df1=pd.DataFrame(df1)
df1


# In[26]:


team_count=df['Team'].value_counts()


# In[27]:


team_count


# In[28]:


percentage=(team_count/len(df1)*100)
percentage


# In[29]:


#2Segregate the employees w.r.t different positions.


# In[30]:


df[['Name','Position']]


# In[31]:


df['Position'].value_counts


# In[32]:


#3.Find from which age group most of the employees belong to


# In[33]:


df[['Name','Age']]


# In[34]:


df['Age'].value_counts().head(1)


# In[35]:


#4.Find out under which team and position, spending in terms of salary is high.


# In[36]:


df['Salary'].fillna(0,inplace=True)


# In[37]:


df1=df[['Team','Position','Salary']]
df1


# In[38]:


df1=df[['Team','Position','Salary']]
df1=pd.DataFrame(df1)
df1


# In[39]:


team_position_salary=df1.groupby(['Team','Position','Salary'])['Salary'].sum()
team_position_salary


# In[40]:


Team_salary=df1.groupby(["Team","Position"])["Salary"].sum()
Team_salary


# In[41]:


Team_salary.sort_values().tail()


# In[42]:


#5.Find if there is any correlation between age and salary , represent it visually.


# In[43]:


correlation=df['Age'].corr(df['Salary'])
correlation


# In[44]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.scatterplot(x='Age',y='Salary',data=df)
plt.title("Correlation between age and salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# In[45]:


df1


# In[46]:


df1.isnull().sum()


# In[47]:


df1.info()


# In[48]:


df.info()


# In[49]:


df.to_csv("Module_end_project.csv")


# In[ ]:




