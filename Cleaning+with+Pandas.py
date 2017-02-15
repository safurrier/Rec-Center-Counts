
# coding: utf-8

# In[56]:

import pandas as pd
import numpy as np
import csv


# with open("file-name", "r") as fp:
# fileData = fp.read()
# #to print the contents of the file print(fileData)
# 
# import CSV
# 
# With open(‘some.csv’, ‘rb’) as f:
# 
# reader = csv.reader(f)
# 
# for row in reader:
# 
#     print row

# Opening the csv and turning it into a dataframe

# The csv file is encoded in something weird: MAC OS Roman not utf-8 wtf gotta fix that

# **Printing the CSV**

# In[57]:

with open("rec_center_counts.csv", "rt") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)


# **Turning the csv into a dataframe**

# In[58]:

df = pd.read_csv('rec_center_counts.csv')

df.head(5)


# Check column types

# In[59]:

df.dtypes


# Checking if "Date" is being read as a column

# In[60]:

'Date' in df.keys()


# It's not reading as a column. Pulling the column names

# In[61]:

list(df.columns.values)


# "Date" is actually "Date " with a space. Fixing that.

# In[62]:

df = df.rename(columns = {"Date ": "Date"})

list(df.columns.values)


# Dropping last column "Unnamed: 20"

# In[63]:

del df['Unnamed: 20']


# In[64]:

df


# Melting the columns into variables

# In[65]:

id_vars = ["Weight Room", "Date"]

formatted_df = pd.melt(df,
                       id_vars = id_vars,
                       var_name = "time",
                       value_name = "count")
formatted_df


# Dropping NaN just to see what happens

# In[66]:

df2 = formatted_df.dropna()

df2


# Dropping Na values in Weight Room column to see difference

# In[69]:

df3 = formatted_df.dropna(subset=['Weight Room'])

df3


# Changing the date into datetime

# In[71]:

df3['Date'] = pd.to_datetime(df3['Date'])

df3


# In[74]:

df3.dtypes


# Seeing how many null counts vs filled counts

# In[84]:

df3['count'].count()


# In[85]:

df3['count'].isnull().sum()


# In[87]:

df3.to_csv('rec_center_cleaned.csv')


# In[ ]:



