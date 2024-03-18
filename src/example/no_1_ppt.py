#%%
# 未安装包需安装
# !pip install pandas
# !pip install numpy
# !pip install matplotlib
# !pip install statistics
# !pip install scipy
#%%
# 数据加载
import pandas as pd
msleep = pd.read_csv("../../data/msleep.csv")
msleep.columns
#%%
import numpy as np
np.mean(msleep['sleep_total'])
#%%

msleep.plot(kind='scatter', x='sleep_total', y='bodywt')
# %%
msleep['vore'].value_counts()

# %%
msleep['vore'].value_counts().plot(kind="bar")
# %%
print(msleep)
# %%
np.mean(msleep['sleep_total'])
# %%
msleep['sleep_total'].sort_values()
#%%
msleep['sleep_total'].sort_values().iloc[41]
#%%
np.median(msleep['sleep_total'])

# %%
msleep['sleep_total'].value_counts()

# %%
msleep['vore'].value_counts()

# %%
import statistics 
statistics.mode(msleep['vore'])

# %%
msleep[msleep['vore'] == 'insecti']
#%%
msleep[msleep['vore'] == "insecti"]['sleep_total'].agg([np.mean, np.median])

# %%
msleep[msleep['vore'] == 'insecti']

# %%
msleep[msleep['vore'] == "insecti"]['sleep_total'].agg([np.mean, np.median])

# %%
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])
print(dists)

# %%
sq_dists = dists ** 2
print(sq_dists)

# %%
sum_sq_dists = np.sum(sq_dists)
print(sum_sq_dists)

# %%
variance = sum_sq_dists / (83 - 1)
print(variance)

# %%
np.var(msleep['sleep_total'], ddof=1)

# %%
np.var(msleep['sleep_total'])
#%%
np.sqrt(np.var(msleep['sleep_total'], ddof=1))
# %%
np.std(msleep['sleep_total'], ddof=1)

# %%
dists = msleep['sleep_total'] - np.mean(msleep['sleep_total'])
np.mean(np.abs(dists))

# %%
np.quantile(msleep['sleep_total'], 0.5)
#%%
np.quantile(msleep['sleep_total'], [0, 0.25, 0.5, 0.75, 1])

# %%
import matplotlib.pyplot as plt
plt.boxplot(msleep['sleep_total'])
plt.show()

# %%
np.quantile(msleep['sleep_total'], [0, 0.2, 0.4, 0.6, 0.8, 1])
#%%
# np.linspace(start, stop, num)

# %%
np.quantile(msleep['sleep_total'], np.linspace(0, 1, 5))

# %%
np.quantile(msleep['sleep_total'], 0.75) - np.quantile(msleep['sleep_total'], 0.25)

# %%

from scipy.stats import iqr
iqr(msleep['sleep_total'])

# %%
from scipy.stats import iqr
iqr = iqr(msleep['bodywt'])
lower_threshold	=	np.quantile(msleep['bodywt'],	0.25)	-	1.5	* iqr
upper_threshold	=	np.quantile(msleep['bodywt'],	0.75)	+	1.5	* iqr
# %%
msleep[(msleep['bodywt'] < lower_threshold) | (msleep['bodywt'] > upper_threshold)]
#%%
msleep['bodywt'].describe()

# %%
1 + 1
#%%
1