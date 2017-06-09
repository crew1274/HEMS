import pandas as pd
import numpy as np
thresold = 15
counter = 0
df = pd.read_csv('tpr.csv')
for index, row in df.iterrows():
    if row["distance"] < thresold:
        counter = counter +1
print (counter)