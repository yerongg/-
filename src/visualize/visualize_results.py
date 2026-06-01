import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

os.system("hdfs dfs -getmerge /user/project/results/top10_efficiency data/top10_efficiency.csv")
os.system("hdfs dfs -getmerge /user/project/results/yearly_trend data/yearly_trend.csv")
os.system("hdfs dfs -getmerge /user/project/results/top10_per_capita data/top10_per_capita.csv")
os.system("hdfs dfs -getmerge /user/project/results/major_economies data/major_economies.csv")

df_efficiency = pd.read_csv("data/top10_efficiency.csv", names=['country', 'gdp', 'co2', 'carbon_intensity'])
df_trend = pd.read_csv("data/yearly_trend.csv", names=['year', 'avg_intensity', 'total_co2'])
df_per_capita = pd.read_csv("data/top10_per_capita.csv", names=['country', 'co2', 'population', 'co2_per_capita'])
df_economies = pd.read_csv("data/major_economies.csv", names=['country', 'gdp', 'co2', 'carbon_intensity'])

plt.style.use('ggplot')

fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.lineplot(data=df_trend, x='year', y='avg_intensity', marker='o', color='green', ax=axes[0])
axes[0].set_title("Global Average Carbon Intensity Trend (1990-2020)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Carbon Intensity (CO2 / GDP)")

sns.lineplot(data=df_trend, x='year', y='total_co2', marker='s', color='red', ax=axes[1])
axes[1].set_title("Global Total CO2 Emissions Trend")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Total CO2 Emissions")
plt.tight_layout()
plt.savefig("yearly_trend.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_efficiency, x='carbon_intensity', y='country', palette='Greens_r')
plt.title("Top 10 Green Energy Transition Countries (2020)")
plt.xlabel("Carbon Intensity (CO2 / GDP)")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top10_efficiency.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_per_capita, x='co2_per_capita', y='country', palette='Reds_r')
plt.title("Top 10 CO2 Emissions Per Capita (2020)")
plt.xlabel("CO2 Per Capita")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top10_per_capita.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(data=df_economies, x='country', y='carbon_intensity', palette='Blues_r')
plt.title("Carbon Intensity of Major Economies (2020)")
plt.xlabel("Country")
plt.ylabel("Carbon Intensity (CO2 / GDP)")
plt.tight_layout()
plt.savefig("major_economies.png")
plt.close()

print("Visualization completed successfully. All charts are saved.")
