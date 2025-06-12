import pandas as pd
import requests

laptops = requests.get(url='https://raw.githubusercontent.com/Khalid0415/DSP_project/refs/heads/main/laptop.json')
print(laptops.status_code)
print(type(laptops))
print(type(laptops.json()))

if laptops:
    df = pd.DataFrame(laptops.json())
    print(df)
else:
    print('Json file is not found!')



laptops2 = requests.get(url='https://raw.githubusercontent.com/Khalid0415/DSP_project/refs/heads/main/lap.json')
print(laptops2.status_code)

if laptops2:
    df = pd.DataFrame(laptops.json())
    print(df)
else:
    print('Json file is not found!')