import numpy as np
import seaborn as sns
import pandas as pd
from scipy import stats
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt

num_samples = 61
group_size = 10

x = np.linspace(0, 15, num_samples)
a = np.sin(x) + np.linspace(0, 5, num_samples)

x = np.linspace(0, 50, num_samples)
b = np.sin(x) + np.linspace(0, -8, num_samples)
c = np.sin(x + 2)
print(c)
d = np.linspace(0, 14, num_samples)
e = np.random.randn(group_size, 1) + np.linspace(0, -3, num_samples)

x = np.linspace(0, 4, num_samples)
f = np.sin(x)

timeSeries = pd.DataFrame()
ax = None
#append到DataFrame
for arr in [a,b,c,d,e,f]:
    arr = arr + np.random.rand(group_size, num_samples) + (np.random.randn(group_size, 1)*3)
    df = pd.DataFrame(arr)
    timeSeries = timeSeries.append(df)
    # We use seaborn to plot what we have
    #ax = sns.tsplot(ax=ax, data=df.values, ci=[68, 95])
    ax = sns.tsplot(ax=ax, data=df.values, err_style="unit_traces")
print(timeSeries.describe)

Z = hac.linkage(timeSeries.head(), 'single', 'correlation')
# Plot the dendogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
hac.dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()
