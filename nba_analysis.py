import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('nba.csv',header = 0,skipinitialspace=True)

##df['College'] = df['College'].fillna('missing')
##df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
##
##df_bostonCeltics = df[df['Team'] == 'Boston Celtics']
##print(df_bostonCeltics)
##
##plot_cols = ['Position', 'Weight', 'Salary']
##df_bostonCeltics[plot_cols].plot(x=plot_cols[0], subplots=True)
##plt.xlabel('Position')
##plt.ylabel.axes[0]('Salary')
##plt.ylabel('Weight')
##plt.show()
##print(df)

df_by_team = df.groupby(['Team', 'Position'])
print(df_by_team.first())
salary_sum = df_by_team['Salary'].sum()
print(salary_sum)
