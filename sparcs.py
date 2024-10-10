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

# Calculate the following basic statistics for **Length of Stay**, **Total Charges**, and **Total Costs**:
     # Mean
     # Median
     # Standard Deviation
     # Min/Max
     # Percentiles (25th, 50th, 75th)
     # Quartiles

value_counts = merged['length_of_stay'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['age_group'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['gender'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['total_charges'].value_counts()
print("Value Counts:\n", value_counts)
value_counts = merged['total_costs'].value_counts() 
print("Value Counts:\n", value_counts)
value_counts = merged['type_of_admission'].value_counts()
print("Value Counts:\n", value_counts)

length_of_stay = np.array([74085, 66479, 49343, 33418, 23726])
total_charges = np.array([9203.04, 15082.10, 17690.10, 14587.88, 15611.25])
total_costs = np.array([2384.85, 1743.66, 1924.39, 4825.86, 3011.89])

def calculate_statistics(data, label):
    print(f"Statistics for {label}:")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    print(f"25th Percentile: {np.percentile(data, 25)}")
    print(f"50th Percentile (Median): {np.percentile(data, 50)}")
    print(f"75th Percentile: {np.percentile(data, 75)}")
    print(f"Quartiles: {np.percentile(data, [25, 50, 75])}")
    print("\n")

calculate_statistics(length_of_stay, "Length of Stay")
calculate_statistics(total_charges, "Total Charges")
calculate_statistics(total_costs, "Total Costs")

# Exploring Categorical Variables**:
 
    # Count distribution for Age Group, Gender, and Type of Admission
age_group_counts = merged['age_group'].value_counts()
gender_counts = merged['gender'].value_counts()
admission_type_counts = merged['type_of_admission'].value_counts()

print("Age Group Distribution:\n", age_group_counts)
print("\nGender Distribution:\n", gender_counts)
print("\nType of Admission Distribution:\n", admission_type_counts)

    # Create a bar plot for Age Group, Gender, and Type of Admission
plt.figure(figsize=(14, 6))
plt.subplot(1, 3, 1)
sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette='viridis')
plt.title('Age Group Distribution')
plt.xticks(rotation=90)

plt.subplot(1, 3, 2)
sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='viridis')
plt.title('Gender Distribution')

plt.subplot(1, 3, 3)
sns.barplot(x=admission_type_counts.index, y=admission_type_counts.values, palette='viridis')
plt.title('Type of Admission Distribution')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

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

# Handling missing data

# Handling missing values in the dataset

print(merged.isnull().sum())  # Shows the count of missing values per column

# 1. Dropping rows with missing values
merged_dropped = merged.dropna()

# 2. Filling missing values with mean/median for numerical columns
# and most frequent value for categorical columns
merged_filled = merged.fillna({
    'length_of_stay': merged['length_of_stay'].median(),
    'total_charges': merged['total_charges'].median(),
    'total_costs': merged['total_costs'].median(),
    'age_group': merged['age_group'].mode()[0],  # Fill categorical columns with mode (most frequent value)
    'gender': merged['gender'].mode()[0],
    'type_of_admission': merged['type_of_admission'].mode()[0]
})

print(merged_filled.isnull().sum())  # Check again after filling missing values
