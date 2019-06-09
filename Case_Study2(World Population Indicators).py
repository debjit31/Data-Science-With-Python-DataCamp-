import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##Reader Object(Iterable)
world_pop_ind=pd.read_csv('world_ind_pop_data.csv')

def create_set(df,country_code, country_name, year, popula):
    
    data = pd.DataFrame()

    for pop_ind in world_pop_ind:
        df_large_pop = pop_ind[pop_ind[popula]>5000000]

        z = zip(df_large_pop[country_name], df_large_pop[year], df_large_pop[popula])

        pop_list = list(z)

        data = data.append(pop_list)
    
    print(data)
    
create_set(world_pop_ind, 'CountryCode','CountryName','Year','Population')
