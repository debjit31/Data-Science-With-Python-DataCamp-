import pandas as pd

groups = pd.read_csv('groups.csv', index_col = 0)

print(groups)
print('\n')

print(groups.iloc[:, [0,1]])

