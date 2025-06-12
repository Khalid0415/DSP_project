import numpy as np
import pandas as pd

lap_df = pd.read_csv('laptop.csv')

print(list(lap_df.brand.unique()))

l = 'Lenovo'
laptop = lap_df[lap_df['brand'] == l]
print(len(laptop))