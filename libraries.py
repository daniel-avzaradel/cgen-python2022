import pandas as pd
import numpy as np

marks = pd.Series([88,90,72,64], name="Mark")
print(marks)

df = pd.DataFrame({ "country":["israel","france","germany"],
"currency":["ils", "euro","euro"],
"capital":["jerusalem","paris","berlin"]
 })

print(df)