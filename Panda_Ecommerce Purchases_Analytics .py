#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# # Ecommerce Purchases Exercise
# 
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[2]:


ecom= pd.read_csv('Ecommerce Purchases')


# **Check the head of the DataFrame.**

# In[87]:


ecom.head()


# ** How many rows and columns are there? **

# In[3]:


ecom.info()


# ** What is the average Purchase Price? **

# In[5]:


ecom['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **

# In[6]:


ecom['Purchase Price'].max()


# In[7]:


ecom['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[13]:


ecom[ecom['Language']=='en'].count()


# ** How many people have the job title of "Lawyer" ? **
# 

# In[15]:


ecom[ecom['Job']=='Lawyer'].info()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[16]:


ecom['AM or PM'].value_counts()


# ** What are the 5 most common Job Titles? **

# In[19]:


ecom['Job'].value_counts().head(5)


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[21]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[22]:


ecom[ecom['Credit Card']==4926535242672853]['Email']


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[28]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[29]:


sum(ecom['CC Exp Date'].apply(lambda x : x[3:]=='25'))


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[41]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

