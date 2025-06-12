import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
lap_df = pd.read_csv('laptop.csv')
del lap_df['Unnamed: 0']
lap_df['price(JD)'] = lap_df['price'] / 117

#Handel with Null Values
print(lap_df.info())
print(lap_df.isnull().sum())
print(lap_df.notnull().sum())
print(lap_df['screen_size(inches)'].isnull().sum())
print(lap_df['resolution (pixels)'].isnull().sum())

#fill
print(lap_df.iloc[992:995,[0,8,9]])
lap_df['screen_size(inches)'].fillna(lap_df['screen_size(inches)'].mean(),inplace=True)
lap_df['resolution (pixels)'].fillna(method='pad',inplace=True)
print(lap_df.iloc[992:995,[0,8,9]])
#drop
lap_df.dropna(inplace=True) #drop row
lap_df.dropna(axis=1,inplace=True) #drop col



#astype
lap_df['price(JD)'] = lap_df['price(JD)'].astype(np.int32)
print(lap_df.dtypes)



#groupby
"""lap_df_brand = lap_df.groupby(by=['brand'])
for b in lap_df_brand:
    print(b)"""

#1 number of laptops for each brand
print(lap_df.groupby(by=['brand'])['brand'].count())
#highest price for each brand
print(lap_df.groupby(by=['brand'])['price(JD)'].max())
#avarage for price for each brand and Operating System
print(lap_df.groupby(by=['brand','Operating System'])['price(JD)'].mean())
#minimum for ram,ssd,hd for each processor
print(lap_df.groupby(by=['processor_name'])[['ram(GB)','ssd(GB)','Hard Disk(GB)']].min())
#minimum,maximum for price for each brand
print(lap_df.groupby(by=['brand'])['price(JD)'].agg([np.min,np.max]))



#Categorical
lap_df['OS cat'] = pd.Categorical(lap_df['Operating System'])
print(lap_df.dtypes)
print(lap_df['OS cat'].cat.categories)
print(lap_df['OS cat'].cat.codes)



#Visualization
lap_df.plot.scatter(x='spec_score',y='price',title='price vs spec_score',color='green',alpha=0.6,figsize=(8,5))
plt.ylabel('price')
plt.xlabel('spec_score')
plt.tight_layout()
plt.show()