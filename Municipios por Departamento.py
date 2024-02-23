#!/usr/bin/env python
# coding: utf-8
#Author: Ever Salazar
# In[1]:


import pandas as pd


# In[10]:


tabla_excesos = pd.read_excel("Tabla_excesos_2.xlsx", sheet_name = "SEPTIEMBRE", skiprows = 1)
tabla_excesos


# In[11]:


tabla_excesos_2 = tabla_excesos.groupby(["DEPARTAMENTO", "EXCESO DE PRECIPITACIÓN"]).count()
tabla_excesos_2


# In[12]:


tabla_excesos_3 = tabla_excesos_2["MUNICIPIO"]


# In[13]:


tabla_excesos_3.to_excel("Intento-Septiembre.xlsx")


# In[ ]:




