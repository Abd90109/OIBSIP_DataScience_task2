# Unemployment Analysis using Python

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset(
data = pd.read_csv("Unemployment in India (1).csv")

# Show first few rows
print("Dataset Preview:")
print(data.head())


# Check basic information about dataset
print("\nDataset Information:")
print(data.info())


# Rename columns for easier use
data.columns = ['region', 'date', 'frequency', 'unemployment_rate',
                'employed', 'labour_participation', 'area']


# Convert date column into proper datetime format
data['date'] = pd.to_datetime(data['date'])


# Plot unemployment rate over time
plt.figure(figsize=(10,5))
sns.lineplot(x='date', y='unemployment_rate', data=data)
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()


# Plot unemployment rate by region
plt.figure(figsize=(12,6))
sns.barplot(x='region', y='unemployment_rate', data=data)
plt.xticks(rotation=90)
plt.title("Unemployment Rate by Region")
plt.show()


# Average unemployment rate
avg_rate = data['unemployment_rate'].mean()

print("\nAverage Unemployment Rate:", avg_rate)