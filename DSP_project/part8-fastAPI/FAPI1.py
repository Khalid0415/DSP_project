from fastapi import FastAPI
import numpy as np
import pandas as pd
app = FastAPI()

lap_df = pd.read_csv('laptop.csv')

#root
@app.get("/")
def root():
    return {'message':'Hello world'}

# read brands
@app.get("/brands")
def read_brands():
    return list(lap_df.brand.unique())