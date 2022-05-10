import pandas as pd
import numpy as np

## Series Class

marks = pd.Series([88,90,72,64], name="Mark")
print(marks)

df = pd.DataFrame({ "country":["israel","france","germany"],
"currency":["ils", "euro","euro"],
"capital":["jerusalem","paris","berlin"]
 })

print(df)


## Selecting Column

print('=============')

countries = df["country"]
print(countries)
print(type(countries))


## Selecting Rows

ds = pd.DataFrame({ "first name":["moshe","daniel","tal"],
 "last name":["israeli","cohen","lahat"],
"id":["234234","645645","678678"],
"average":[85,90,64]
 })

beststudents = ds[ds["average"]>80]
print(beststudents)
print(type(beststudents))