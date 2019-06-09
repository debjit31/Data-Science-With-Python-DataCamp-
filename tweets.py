import pandas as pd
tweets_df = pd.read_csv('tweets.csv')
print(tweets_df.columns)
print(tweets_df)
print('\n')
def count_entries(df, *args):
    count_cols = {}
    for col_name in args:
        if col_name not in df.columns:
            raise ValueError('Column '+ col_name + 'not present in the dataframe '+df)
        else:
            col = df[col_name]
            for entry in col :
                if entry in count_cols.keys():
                    count_cols[entry] += 1
                else:
                    count_cols[entry] =  1
    return count_cols

result1 = count_entries(tweets_df, 'source', 'lang')
print(result1)
print('\n')
for key, val in  result1.items():
    print(key + ': ' + str(val))

