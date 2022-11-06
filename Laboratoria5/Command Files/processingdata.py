# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:25:01 2022

@author: To_Ja
"""
import pandas as pd
# Open the file as read
f = open("Weather.txt", "r")
# Create an array to hold write data
new_file = []
# Loop the file line by line
for line in f.readlines():
    # modify line
    new_line = line[0:11] + "|" + line[11:15] + "|" + line[15:17] + "|" + line[17:21] + "|" + line[21:28]
    for i in range(1,31):
        a=28 + (i*8)
        #if line[a] != "S" and line[a] != " " and line[a] != "I": #sprawdza, czy zapis danych jest w taki sposób jak przewidziano
        #    print(line[a])     
        new_line = new_line + "|" + line[a-7:a]
    # Add
    
    new_file.append(new_line)#.replace(' ',''))
# Open the file as Write, loop the new array and write with a newline
with open("loadme.txt", "w+") as f:
  for i in new_file:
    f.write(i+"\n")
#reading data   
df = pd.read_csv('loadme.txt', sep="|", header=None, dtype=str)
df.columns=["ID","Year","Month","Measuremnet","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
#changing days into two columns, date and corresponding value
df = df.melt(id_vars=["ID","Year","Month","Measuremnet"], 
        var_name="Day", 
        value_name="Value")
#changing measurement row and value column into three separate columns

df = pd.pivot(df, values='Value', index=["ID","Year","Month","Day"],
                    columns=["Measuremnet"])

df = df.reset_index()
#Unifying data type
df['TMIN'] = df['TMIN'].astype(str)
df['TMAX'] = df['TMAX'].astype(str)
df['PRCP'] = df['PRCP'].astype(str)
#Deleting junk letter from original data file, unifying -9999 
df['PRCP'] = df['PRCP'].str.replace('D','')
df['TMIN'] = df['TMIN'].str.replace('D','')
df['TMAX'] = df['TMAX'].str.replace('D','')
# unifying -9999 and nan created from pivot - there are months without measurment of variable! it will result in nan value after pivoting
df['PRCP'] = df['PRCP'].str.replace('-9999','nan')
df['TMIN'] = df['TMIN'].str.replace('-9999','nan')
df['TMAX'] = df['TMAX'].str.replace('-9999','nan')
#stripping and padding for equal length
df['PRCP'] = df['PRCP'].str.strip()
df['TMIN'] = df['TMIN'].str.strip()
df['TMAX'] = df['TMAX'].str.strip()
df['TMIN']= df['TMIN'].str.pad(7, side ='right', fillchar =' ')
df['TMAX']= df['TMAX'].str.pad(7, side ='right', fillchar =' ')
df['PRCP']= df['PRCP'].str.pad(7, side ='right', fillchar =' ')

#deleting days without any data
df = df.drop(df[(df.TMIN == "nan    ") & (df.TMAX == "nan    ") & (df.PRCP == "nan    ")].index)
#df.to_csv('weather_sorted_year_month_day.txt', index=None, sep='|', mode='a')
#adding date column
df["Date"] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df['Date'] = df["Date"].dt.strftime('%Y-%m-%d')
#deleting obsolete columns
df = df.drop(columns=['Year', 'Month', 'Day'])
df = df[['ID', 'Date','TMAX','TMIN','PRCP']]
#saving pandas DataFrame into file
df.to_csv('weather_sorted_date.txt', index=None, sep='|', mode='a')

