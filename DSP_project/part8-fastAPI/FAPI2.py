from fastapi import FastAPI,HTTPException
import numpy as np
import pandas as pd
import json
from pydantic import BaseModel
app = FastAPI()

lap_df = pd.read_csv('laptop.csv')
del lap_df['Unnamed: 0']


#searsing brand of the laptop
@app.get("/laptops/{brand}")
def read_student(brand:str):
    laptop= lap_df[lap_df.brand == brand]
    if len(laptop)>0:
        return json.loads(laptop.to_json())
    else:
        raise HTTPException(status_code=404,detail="brand not found!")
        return {"error":"brand not found!"}