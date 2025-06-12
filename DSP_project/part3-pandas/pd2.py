import numpy as np
import pandas as pd

lap_df = pd.read_csv('laptop.csv')
del lap_df['Unnamed: 0']

#Selection,Addition,Deletion row
#selection first 5 rows
print(lap_df[0:5])
print(lap_df.loc[0:4])
print(lap_df.iloc[0:5])

#add first 5 rows
f5rows = lap_df.iloc[0:5]
lap_df2 = pd.concat([lap_df,f5rows])
lap_df2.reset_index(inplace=True,drop=True)
print(lap_df2)
#delete first 5 rows
lap_df.drop([0,1,2,3,4],inplace=True)
lap_df.reset_index(inplace=True,drop=True)
print(lap_df)



#Descriptive Statistics
print(lap_df.count())
print(lap_df['price'].min())
print(lap_df['price'].max())
print(lap_df['price'].mean())
print(lap_df.loc[:,['no_of_cores','no_of_threads']].mode())
print(lap_df.loc[:,['screen_size(inches)','spec_score']].median())



#Covariance & Correlation & Ranking
lap_df['price(JD)'] = lap_df['price'] / 117

print(lap_df['price'].cov(lap_df['price(JD)']))
print(lap_df['price'].corr(lap_df['price(JD)']))

print(lap_df['ssd(GB)'].cov(lap_df['Hard Disk(GB)']))
print(lap_df['ssd(GB)'].corr(lap_df['Hard Disk(GB)']))

print(lap_df.loc[:,['ram(GB)','ssd(GB)','Hard Disk(GB)']].cov())
print(lap_df.loc[:,['ram(GB)','ssd(GB)','Hard Disk(GB)']].corr())

lap_df['spec_score(RK)'] = lap_df['spec_score'].rank(method='dense')
print(lap_df.loc[:,['model_name','spec_score','spec_score(RK)']].head(10))



#Sorting
#sort column
lap_dfs =lap_df.sort_index(axis=1)
print(lap_dfs)

#sort rows
lap_df.sort_values(by=['spec_score'],inplace=True)
print(lap_df)
lap_df.sort_values(by=['price','spec_score'],inplace=True,ascending=False)
print(lap_df)
print(lap_df['price'].max())



# str
#Extract laptop model from model_name column
lap_df['brand2'] = [b.split()[0] for b in lap_df['model_name']]
print(lap_df)