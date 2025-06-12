import numpy as np
import pandas as pd

lap_df = pd.read_csv('laptop.csv')

#data exploration
print(lap_df)
print(lap_df.dtypes,lap_df.size)
print(lap_df.head(20))
print(lap_df.tail(20))
print(lap_df.info())
print(lap_df.describe())
print(lap_df.describe(include=['object']))



#Filtring
print(lap_df[(lap_df['brand'] == 'Lenovo') & (lap_df['price'] < 20000)])
print(lap_df[lap_df['ram(GB)'] == 16])
print(lap_df[lap_df['Operating System'].isin(('Mac','DOS'))])



#loc & ilic
print(lap_df.loc[20:30,['model_name','ssd(GB)','price']])
print(lap_df.iloc[20:31,[1,5,14]])

print(lap_df.loc[:,['Unnamed: 0','model_name','brand','processor_name','ram(GB)','ssd(GB)','Hard Disk(GB)','Operating System','graphics','screen_size(inches)','resolution (pixels)','no_of_cores','no_of_threads','spec_score']])
print(lap_df.iloc[:,0:-1])



#Selection,Addition,Deletion Column
print(lap_df['price']) #or print(lap_df.price)
#the price column contains the prices of laptops in INR and i will convert it to JD
lap_df['price(JD)'] = lap_df['price'] / 117
print(lap_df.loc[:,['price','price(JD)']])
#i will add column containing the storge type: SSD or HD or both SSD,HD
lap_df['Storge Type'] = ['SSD,HD' if s>0 and h>0 else
                        'SSD' if s>0 else
                        'HD' if h>0 else
                        'nothing'
                        for s,h in zip(lap_df['ssd(GB)'],lap_df["Hard Disk(GB)"])]
print(lap_df.loc[:,['model_name','ssd(GB)','Hard Disk(GB)','Storge Type']])
#delete Unnamed: 0 column
del lap_df['Unnamed: 0'] # or lap_df.pop('Unnamed: 0') or lap_df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(lap_df)