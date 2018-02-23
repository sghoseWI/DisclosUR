# CAPP 30122: Group Project
# Saptarshi Ghose


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


sns.set(style="darkgrid")
my_data = pd.read_csv("CPI_data_prac.csv")
ax = sns.countplot(x="industry", data=my_data)

plt.show(ax)

# sns.set_style("whitegrid")
# tips = pd.read_csv('CPI_data.csv')
# ax = sns.barplot(x="cpi_id", y="body", data=tips)
# plt.show(ax)
