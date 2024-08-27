#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df


# In[6]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
print(df.head(5))
df.tail(2)


# In[7]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.info()


# In[8]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.describe()


# In[9]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.shape


# In[11]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.isnull().sum()


# In[4]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.dropna(how='any').shape


# In[6]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
x=df.dropna(how='any')
x


# In[7]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.nunique()


# In[9]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
x2=df.dropna(how='all').shape
x2


# In[11]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
tot=df.dropna(subset=['TOTAL'],how='any')
tot


# In[13]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
tot=df.dropna(subset=['M1','M2','M3','M4'],how='any')
tot


# In[15]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
s=df.fillna(0)
s


# In[16]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.isna().sum()


# In[17]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df['M2']


# In[18]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.isnull()


# In[19]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.notnull()


# In[20]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
xl=df.dropna(axis=0)
xl


# In[21]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
df.duplicated()


# In[24]:


import pandas as pd
df=pd.read_csv("SAMPLEIDs.csv")
m=df.drop_duplicates(inplace=False)
m


# In[31]:


import seaborn as sns
sns.heatmap(df.isnull(),yticklabels=False,annot=True)


# In[33]:


import seaborn as sns
sns.heatmap(df.notnull(),yticklabels=False,annot=True)


# In[35]:


import seaborn as sns
df.dtypes


# In[ ]:




