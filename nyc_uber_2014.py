import pandas as pd
import matplotlib.pyplot as plt
##Importing the data set 
df = pd.read_csv('nyc_uber_2014.csv', index_col=0)
##Assigning new column names
df.columns = ['Date', 'Lat', 'Lon', 'Base']

df.Date = pd.to_datetime(df.Date)

df.set_index('Date', inplace=True)
df.to_csv('new_nyc_uber_2014.csv')

print(df.loc['2014-05-01':'2014-05-03','Lat' ])






