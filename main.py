# 📊 South Africa Crime Data Visualization
# Author: tshivhenga Thompho Sheriff
# Final version of my data analysis and visualization script

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

# -------------------------------------
# 🧪 Step 1: Load the dataset
# -------------------------------------
df = pd.read_csv("crime-statistics-for-south-africa/SouthAfricaCrimeStats_v2.csv")

# -------------------------------------
# 🔄 Step 2: Reshape the dataset from wide to long format
# Each row will represent a (Province, Station, Category, Year, Crime Count) entry
# -------------------------------------
df_melted = pd.melt(
    df,
    id_vars=['Province', 'Station', 'Category'],
    var_name='Year',
    value_name='Crime Count'
)

# -------------------------------------
# 🧹 Step 3: Clean the data
# -------------------------------------
df_melted['Crime Count'] = pd.to_numeric(df_melted['Crime Count'], errors='coerce')

# -------------------------------------
# 📈 Step 4: National crime trend over the years
# -------------------------------------
crime_by_year = df_melted.groupby('Year')['Crime Count'].sum()

# -------------------------------------
# 📊 Step 5: Line chart - Total Crimes Over Time
# -------------------------------------
plt.figure(figsize=(12, 5))
sns.lineplot(x=crime_by_year.index, y=crime_by_year.values, marker='o', color='steelblue')
plt.title("Total Crimes in South Africa (2005–2016)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Total Crimes")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------
# 🏙️ Step 6: Bar chart - Total Crimes by Province
# -------------------------------------
province_total = df_melted.groupby('Province')['Crime Count'].sum().sort_values()

plt.figure(figsize=(10, 6))
province_total.plot(kind='barh', color='tomato')
plt.title("Total Crimes by Province (2005–2016)", fontsize=14)
plt.xlabel("Total Crimes")
plt.ylabel("Province")
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# -------------------------------------
# Step 7: Line chart - Top 5 Crime Categories Over Time
# -------------------------------------
top_categories = df_melted['Category'].value_counts().head(5).index
df_top = df_melted[df_melted['Category'].isin(top_categories)]

plt.figure(figsize=(14, 6))
sns.lineplot(
    data=df_top,
    x='Year',
    y='Crime Count',
    hue='Category',
    estimator='sum',
    marker='o'
)
plt.title("Top 5 Crime Categories Over Time", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Crime Count")
plt.xticks(rotation=45)
plt.legend(title="Category")
plt.tight_layout()
plt.show()

# -------------------------------------
# Step 8: Optional - Line chart for a specific province (e.g., Gauteng)
# -------------------------------------
gauteng_data = df_melted[df_melted['Province'] == 'Gauteng']

plt.figure(figsize=(12, 5))
sns.lineplot(
    data=gauteng_data,
    x='Year',
    y='Crime Count',
    hue='Category',
    estimator='sum',
    marker='o'
)
plt.title("Crimes in Gauteng (2005–2016)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Crime Count")
plt.xticks(rotation=45)
plt.legend(title="Category")
plt.tight_layout()
plt.show()
