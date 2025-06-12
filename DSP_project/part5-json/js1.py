import pandas as pd
import json
lap_df = pd.read_csv('laptop.csv')
lap_df.to_json('laptop.json',orient='records')

lap_df2 = pd.read_json('laptop.json')
del lap_df['Unnamed: 0']
lap_df2.to_json('laptop_clearned.json',orient='columns')