import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler,normalize,Binarizer,LabelEncoder,OneHotEncoder

lap_df = pd.read_csv('laptop.csv')
del lap_df['Unnamed: 0']

#preprocessing
#numerical data
#1-price
lap_df['price MinMaxScaler'] =  MinMaxScaler(feature_range=(0,1)).fit_transform(lap_df.loc[:,['price']])
lap_df['price StandardScaler'] =  StandardScaler().fit_transform(lap_df.loc[:,['price']])
lap_df['price normlize'] =  normalize(lap_df.loc[:,['price']])
lap_df['price binarizer'] =  Binarizer(threshold=50000).fit_transform(lap_df.loc[:,['price']])
print(lap_df.loc[:,['price MinMaxScaler','price StandardScaler','price normlize','price binarizer']])
#2-screen_size(inches)
lap_df['screen_size(inches)'].fillna(lap_df['screen_size(inches)'].mean(),inplace=True)
lap_df['S_size MinMaxScaler'] =  MinMaxScaler(feature_range=(0,1)).fit_transform(lap_df.loc[:,['screen_size(inches)']])
lap_df['S_size StandardScaler'] =  StandardScaler().fit_transform(lap_df.loc[:,['screen_size(inches)']])
lap_df['S_size normlize'] =  normalize(lap_df.loc[:,['screen_size(inches)']])
lap_df['S_size binarizer'] =  Binarizer(threshold=15).fit_transform(lap_df.loc[:,['screen_size(inches)']])
print(lap_df.loc[:,['S_size MinMaxScaler','S_size StandardScaler','S_size normlize','S_size binarizer']])
#3-spec_score
lap_df['spec_score MinMaxScaler'] =  MinMaxScaler(feature_range=(0,1)).fit_transform(lap_df.loc[:,['spec_score']])
lap_df['spec_score StandardScaler'] =  StandardScaler().fit_transform(lap_df.loc[:,['spec_score']])
lap_df['spec_score normlize'] =  normalize(lap_df.loc[:,['spec_score']])
lap_df['spec_score binarizer'] =  Binarizer(threshold=65).fit_transform(lap_df.loc[:,['spec_score']])
print(lap_df.loc[:,['spec_score MinMaxScaler','spec_score StandardScaler','spec_score normlize','spec_score binarizer']])


#Categorical data
#1-brand
lap_df['brand label_enc'] = LabelEncoder().fit_transform(lap_df.loc[:,['brand']])
print(lap_df.loc[:,['brand','brand label_enc']])

ohe = OneHotEncoder()
ohe_brand = ohe.fit_transform(lap_df[['brand']])
print(ohe.get_feature_names_out(['brand']))
ohe_df = pd.DataFrame(ohe_brand.toarray(),columns=[ohe.get_feature_names_out(['brand'])])
print(ohe_df)

#2-Operating System
lap_df['OS label_enc'] = LabelEncoder().fit_transform(lap_df.loc[:,['Operating System']])
print(lap_df.loc[:,['Operating System','OS label_enc']])

ohe_OS = ohe.fit_transform(lap_df[['Operating System']])
print(ohe.get_feature_names_out(['Operating System']))
ohe_df2 = pd.DataFrame(ohe_OS.toarray(),columns=[ohe.get_feature_names_out(['Operating System'])])
print(ohe_df2)