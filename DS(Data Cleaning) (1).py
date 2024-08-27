#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[25,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_cleaned=df.dropna(subset=['Salary'])
df_cleaned


# In[11]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[25,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_cleaned_all=df.dropna(how='all')
df_cleaned_all


# In[9]:


import pandas as pd
data={'Name':[None,'Blue','Charlie','Delta','Echo'],'Age':[None,32,None,41,28],'Salary':[None,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_cleaned_all=df.dropna(how='all')
df_cleaned_all


# In[15]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[25,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_cleaned_all=df.dropna(how='any')
df_cleaned_all


# In[16]:


import pandas as pd
import numpy as np
data={'Name':['Alice','Blue','Charlie','Delta','Echo','Blue','Charlie','Echo'],'Age':[25,32,np.nan,41,28,32,np.nan,38],'Salary':[50000,np.nan,70000,90000,60000,np.nan,70000,60000]}
df=pd.DataFrame(data)
~df.duplicated()


# In[24]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[25,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_filled=df.fillna(10)
df_filled


# In[23]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[25,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_filled=df.fillna(method='ffill')
df_filled


# In[21]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[25,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_filled=df.fillna(method='bfill')
df_filled


# In[22]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[None,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_filled=df.fillna(method='ffill')
df_filled


# In[31]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[None,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df_mean=df.fillna(df.mean())
df_mean


# In[1]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[None,32,None,41,28],'Salary':[50000,None,70000,90000,60000]}
df=pd.DataFrame(data)
df.isnull().sum()


# In[3]:


import pandas as pd
data={'Name':['Alice','Blue','Charlie','Delta','Echo'],'Age':[None,32,None,41,28],'Salary':[50000,None,70000,90000,50000]}
df=pd.DataFrame(data)
df.nunique()


# In[ ]:




