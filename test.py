import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df['2013'])
print(df.dtypes)
