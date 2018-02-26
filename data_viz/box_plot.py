# CAPP 30122: Group Project
# Saptarshi Ghose


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


sns.set(style="darkgrid")
my_data = pd.read_csv('CPI_data_cleaned.csv', sep=',', encoding='latin-1')
ax = sns.countplot(x="industry", data=my_data)

plt.xlabel('industry')
plt.show(ax)
