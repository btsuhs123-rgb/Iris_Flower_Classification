# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in india.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove extra spaces from column names
df.columns = df.columns. str.strip()

# Convert Date column into datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Average unemployment by region
region_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by Region:")
print(region_unemployment.sort_values(ascending=False))


# Plot unemployment over time
plt.figure(figsize=(12,6))
sns . lineplot(
x='Date',
y='Estimated Unemployment Rate (%)',
data=df)

plt. title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt. show()


# Covid-19 Impact Analysis
covid_data = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(12,6))
sns.lineplot(
X='Date',
y='Estimated Unemployment Rate (%)',
data=covid_data
)

plt.title("Impact of COVID-19 on Unemployment")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()

#

# Heatmap of unemployment by region

pivot_table = df.pivot_table(
values='Estimated Unemployment Rate (%)',
index='Region',
aggfunc='mean'
)

plt.figure(figsize=(8,10))
sns.heatmap(pivot_table, annot=True, cmap='y10rRd')

plt.title("Average Unemployment Rate by Region")
plt . show()

print("\nAnalysis Completed Successfully!")