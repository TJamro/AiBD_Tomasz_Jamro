# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:20:33 2022

@author: student193
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Slaskie.txt', dtype=str)
info = df.describe()
df['Dni od zakupu'] = df['Dni od zakupu'].astype(int)
column1 = df['Dni od zakupu'].value_counts(dropna=False)
column1 = column1.sort_index()
column2 = df['Marka'].value_counts(dropna=False)
column3 = df['Wiek kupującego'].value_counts(dropna=False)
column4 = df['Płeć kupującego'].value_counts(dropna=False)
column5 = df['Ocena'].value_counts(dropna=False)
column5 = column5.sort_index()

#

dni_list =  list(df["Dni od zakupu"])
dni_list = list(np.float_(dni_list))
dni_list = np.array(dni_list)

column1_mean = np.mean(dni_list)
column1_std = np.std(dni_list)
column1_min = np.min(dni_list)
column1_25 = np.percentile(dni_list, 25)
column1_median = np.percentile(dni_list, 50)
column1_75 = np.percentile(dni_list, 75)
column1_max = np.max(dni_list)

#

df['Wiek kupującego'] = df['Wiek kupującego'].replace(' ','', regex=True)
wiek_list =  list(df["Wiek kupującego"])
wiek_list = list(np.float_(wiek_list))
wiek_list = np.array(wiek_list)
wiek_list = wiek_list[~np.isnan(wiek_list)]

column3_mean = np.mean(wiek_list)
column3_std = np.std(wiek_list)
column3_min = np.min(wiek_list)
column3_25 = np.percentile(wiek_list, 25)
column3_median = np.percentile(wiek_list, 50)
column3_75 = np.percentile(wiek_list, 75)
column3_max = np.max(wiek_list)

#

df['Ocena'] = df['Ocena'].replace(' ','', regex=True)

ocena_list =  list(df["Ocena"])
ocena_list = list(np.float_(ocena_list))
ocena_list = np.array(ocena_list)

column5_mean = np.mean(ocena_list)
column5_std = np.std(ocena_list)
column5_min = np.min(ocena_list)
column5_25 = np.percentile(ocena_list, 25)
column5_median = np.percentile(ocena_list, 50)
column5_75 = np.percentile(ocena_list, 75)
column5_max = np.max(ocena_list)


plt.figure()
plt.hist(dni_list, bins=14) #kończy się przedziałami z liczbami całkowitymi
plt.xlabel("Dni od zakupu a oceny")
plt.figure()
column2.plot.bar()
plt.xlabel("Marka odkurzacza")
plt.figure()
plt.hist(wiek_list, bins=66-18) #kończy się przedziałami z liczbami całkowitymi
plt.xlabel("Rozkład wieku klientów")
plt.figure()
column4.plot.bar()
plt.xlabel("Płeć klientów")
plt.figure()
column5.plot.bar()
plt.xlabel("Oceny klientów")

