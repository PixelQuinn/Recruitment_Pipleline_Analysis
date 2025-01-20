# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "../data/raw/recruitment_data.csv"
data = pd.read_csv(file_path)

# Display basic info
print("Dataset Overview:")
print(data.info())

# View first few rows
print("\nSample Data:")
print(data.head)

# Filling missing values in HaveWorkedWith with 'Unknown' to retain all rows
# and avoid making assumptions about the missing data.
data['HaveWorkedWith'].fillna("Unknown", inplace=True)

# Look for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Describe numerical data
print("\nNumerical Data Summary:")
print(data.describe())

# Check for unique values in key categorical columns
categorical_cols = data.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nUnique values in {col}:")
    print(data[col].unique())