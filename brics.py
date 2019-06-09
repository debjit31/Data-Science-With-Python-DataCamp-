import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

brics = pd.read_csv('brics.csv', index_col = 0)
print('Displaying the entire dataframe')
print(brics)
print('\n')
print('Column access : displaying multiple columns from brics dataframe')
print(brics[['country', 'capital']])
print('\n')
print('Row access  : only through slicing')
print(brics[1:4])
print('\n')
print('loc function : loc  uses label bases indexing :- list of row labes followed by column labels')
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])
print('\n')
print(brics.loc[:, ["country", "capital"]])
print('\n')
print('iloc function : used for accessing datasets based on indexing, dataframes always follow zero indexing for both rows and columns: - row index followed by column index')
print(brics.iloc[[1,2,3], [1,3]])
print('\n')

refind_pop = brics[np.logical_and(brics['population'] > 200, brics['population'] < 2500)]
print('Countries with population greater than 200 and less than 2500')
print('\n')
print(refind_pop)
## Fetching data from dataframe to numpy arrays for plotting
area = brics[['area']]
np_area = np.array(area)
## Fetching data from dataframe to numpy arrays for plotting
pop = brics[['population']]
np_pop=np.array(pop)
plt.scatter(x = np_area, y = np_pop, s = np.array(pop) * 2)
plt.grid(True)
plt.xlabel('Area')
plt.ylabel('Population')
plt.title('Population vs Area plot')
plt.show()

print('#####')
a = brics[brics["area"] > 2]
print(a)
