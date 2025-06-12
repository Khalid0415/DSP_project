import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder

#Step 1: Data Preparation
lap_df = pd.read_csv('laptop.csv')
del lap_df['Unnamed: 0']

numeric_features = ['price', 'screen_size(inches)', 'spec_score']
categorical_features = ['brand', 'Operating System']

#Step 2: Define Transformation pipeline
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', MinMaxScaler())
])
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

#Step 3: create & execute the full transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ],remainder='passthrough') #or drop

transformed_features = preprocessor.fit_transform(lap_df)
transformed_lap_df = pd.DataFrame(
    transformed_features,
    columns=preprocessor.get_feature_names_out()
)

print(preprocessor.get_feature_names_out())
print(transformed_lap_df)