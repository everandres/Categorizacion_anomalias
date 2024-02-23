#!/usr/bin/env python
# coding: utf-8
#Author: Ever Salazar
# In[1]:


import pandas as pd


# In[372]:


anomalias = pd.read_excel("JUL21.xlsx", sheet_name = "BANCO DE DATOS", skiprows = 1) #"BANCO DE DATOS"
anomalias


# In[373]:


filtro_a = anomalias["ESTACION "].isin(["R E G I O N   C A R I B E", "R E G I O N   A N D I N A", "R E G I O N   P A C I F I C A",
                                       "O R I N O Q U I A   Y   A M A Z O N I A", "SIATA - VALLE DE ABURRA", "CRQ  - QUINDIO",
                                       "CAR - CUNDINAMARCA", "C,V,C DE CALI (Telefono)", "'AREA OPERATIVA 2 ATLANTICO - BOLIVAR - CORDOBA - SUCRE (Barranquilla)",
                                       "'AREA OPERATIVA 5 MAGDALENA-CESAR (Santa Marta)", " AREA OPERATIVA 8 SANTANDERES - ARAUCA (Bucaramanga)", 
                                       "AREA OPERATIVA 6 BOYACA - CASANARE  (Duitama)", "AREA OPERATIVA 4 HUILA - CAQUETA - AMAZONAS (Neiva)", 
                                       "AREA OPERATIVA 1 ANTIOQUIA - CHOCO - RISARALDA (Medellin)", "AREA OPERATIVA 3 META -  CASANARE (Villavicencio)", 
                                       "'AREA OPERATIVA 10 TOLIMA - CUNDINAMARCA No,10 (Ibague)", "'AREA OPERATIVA 9 - VALLE - RISARALDA - QUINDIO - CAUCA No,9 (Cali)", 
                                       "AREA OPERATIVA 7 NARIÑO - PUTUMAYO CAUCA (Pasto)", "AREA OPERATIVA 11 - BOGOTA - CUNDINAMARCA", "'AUTOMATICAS - FOPAE", 
                                       "HYDRAS - DESLIZAMIENTOS", "GRUPO  OCENSA", "HYDRAS - INCENDIOS"])


# In[374]:


anomalias = anomalias[~filtro_a]
#anomalias = anomalias.iloc[1:, :]
lista_anomalia = anomalias.columns.to_list()
lista_anomalia


# In[375]:


anomalias.columns = anomalias.columns.astype(str)
anomalias.columns.tolist()


# In[376]:


anomalias_2 = anomalias.loc[:, :'PROM,\nMult-anual mm']
anomalias_2


# In[377]:


anomalias_2.columns


# In[378]:


anomalias_3 = anomalias_2[['lon',
 'lat', "CODIGO", "ESTACION ", "MUNICIPIO", "DPTO", "PREC\nTOTAL", 'PROM,\nMult-anual mm']]
anomalias_3


# In[379]:


anomalias_3['PROM,\nMult-anual mm'] = pd.to_numeric(anomalias_3['PROM,\nMult-anual mm'], errors = "coerce")
anomalias_3["Porcentaje Anomalia"] = (anomalias_3["PREC\nTOTAL"] * 100)/(anomalias_3['PROM,\nMult-anual mm'])
anomalias_3


# In[380]:


anomalias_4 = anomalias_3.loc[anomalias_3["Porcentaje Anomalia"] > 100]
anomalias_4


# In[381]:


anomalias_4.to_excel("ANOMALIA-JULIO-2021.xlsx") #-NUEVOS-PROMEDIOS


# In[ ]:




