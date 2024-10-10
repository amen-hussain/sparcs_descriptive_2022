import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url_nassau = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Nassau&$limit=500000'
url_suffolk = 'https://health.data.ny.gov/resource/5dtw-tffi.csv?hospital_county=Suffolk&$limit=500000'

nassau_df = pd.read_csv(url_nassau)
len(nassau_df)

suffolk_df = pd.read_csv(url_suffolk)
len(suffolk_df)

merged = pd.concat([nassau_df, suffolk_df])

len(merged)

print(merged)

# Visualizations**:
   # Create at least 3 visualizations to summarize the dataset:

    #  Histogram of Length of Stay
plt.figure(figsize=(8, 6))
sns.histplot(merged['length_of_stay'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay')
plt.ylabel('Frequency')
plt.show()

# Sample 10% of the data
sampled_data = merged['total_charges'].dropna().sample(frac=0.1, random_state=42)

# Plot boxplot for the sampled data
plt.figure(figsize=(8, 6))
sns.boxplot(x=sampled_data, color='green')
plt.title('Boxplot of Total Charges (Sampled Data)')
plt.xlabel('Total Charges')
plt.show()

# Apply log transformation to reduce the range of values
plt.figure(figsize=(8, 6))
sns.boxplot(x=np.log1p(merged['total_charges'].dropna()), color='green')
plt.title('Log-transformed Boxplot of Total Charges')
plt.xlabel('Log of Total Charges')
plt.show()

# Use the existing counts for type of admission
plt.figure(figsize=(8, 6))
sns.barplot(x=admission_type_counts.index, y=admission_type_counts.values, palette='coolwarm')
plt.title('Type of Admission Analysis')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
