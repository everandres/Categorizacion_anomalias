#!/usr/bin/env python
# coding: utf-8
#Author: Ever Salazar
# In[31]:


import pandas as pd


# In[43]:


categorizacion = pd.read_excel("ANOMALIA-JUNIO-2021.xlsx", sheet_name = "Junio_2021")
categorizacion


# In[44]:


categorizacion.columns


# In[45]:


def df(dataframe):
    
    if dataframe["%Exceso/Deficit"] > 80:
        val = "Severo"
    elif dataframe["%Exceso/Deficit"] > 60 and dataframe["%Exceso/Deficit"] < 80:
        val = "Muy alto"
    elif dataframe["%Exceso/Deficit"] > 40 and dataframe["%Exceso/Deficit"] < 60:
        val = "Alto"
    elif dataframe["%Exceso/Deficit"] > 20 and dataframe["%Exceso/Deficit"] < 40:
        val = "Moderado"
    else:
        val = "Bajo"
    return val

# categorizacion["Categorizacion"] = ["Severo" if x > 90 "Muy alto" elif x > 80 and x < 90 "Alto" elif x > 60 and x < 80
#                                    "Moderado" elif x > 40 and x < 60 else "Bajo" for x in categorizacion["% Exceso/ Deficit"]]

categorizacion['Categorizacion'] = categorizacion.apply(df, axis=1)
categorizacion


# In[46]:


categorizacion.to_excel("CATEGORIZACION-JUNIO-2021-CORRECCION.xlsx", index = False)


# In[ ]:




