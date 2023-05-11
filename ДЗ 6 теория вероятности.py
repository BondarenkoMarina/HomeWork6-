#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[6]:


import scipy.stats as stats


# In[8]:


from statsmodels.stats.weightstats import _tconfint_generic as t_stat


# In[9]:


from statsmodels.stats.weightstats import _zconfint_generic as z_stat


# In[13]:


zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])


# In[14]:


ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 632])


# In[15]:


x_mean = zp.mean()


# In[16]:


y_mean = ks.mean()


# In[17]:


xy_mean = (zp * ks).mean()


# In[18]:


cov_ks = xy_mean = x_mean * y_mean


# In[19]:


cov_ks


# In[ ]:




