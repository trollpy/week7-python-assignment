# 📊 South Africa Crime Data Analysis (2005–2016)

A data analysis and visualization project exploring crime trends across South Africa from 2005 to 2016, broken down by province, police station, and crime category.

---

## 🧠 Overview

Using data from Kaggle's *"Crime Statistics for South Africa"* dataset, this project:

- Loads and cleans raw crime statistics.
- Transforms the data into a usable format.
- Analyzes trends over time and by location.
- Visualizes key insights using Python libraries.

---

## 📁 Dataset

- **Source**: [Kaggle: Crime Statistics for South Africa](https://www.kaggle.com/datasets/slwessels/crime-statistics-for-south-africa)
- **File**: `crimes_in_south_africa.csv`
- **Fields**:
  - `Province`
  - `Station`
  - `Category` (type of crime)
  - Yearly crime counts: `2005-2006` to `2015-2016`

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install pandas matplotlib seaborn

2. (Optional) Download with Kaggle CLI

Ensure you’ve configured your Kaggle API token, then:

kaggle datasets download -d slwessels/crime-statistics-for-south-africa
unzip crime-statistics-for-south-africa.zip -d crimesa/

🧹 Data Cleaning

    Checked for missing values and data types.

    Reshaped the dataset from wide to long format using pandas.melt.

    Converted all crime counts to numeric.

🔍 Exploratory Data Analysis
✅ What We Explored:

    📈 Total crimes over the years (nationally)

    🏙️ Crimes by Province

    🔍 Most common Crime Categories

    📍 Crime trends in Gauteng

📊 Visualizations
Chart Type	Description
Line Chart	National crime trend over 11 years
Bar Chart	Total crimes per province
Multi-Line Chart	Top 5 crime categories over time
Province Focus	Gauteng crime trends by category

Each chart includes titles, labels, color styling, and legends for clarity and aesthetics using matplotlib and seaborn.


