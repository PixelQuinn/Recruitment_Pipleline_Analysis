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

# Split 'HaveWorkedWith' into individual skills
skills = data['HaveWorkedWith'].str.split(';').explode()

# Count occurences of each tech
skill_counts = skills.value_counts()

print("Top 10 Most Common Technologies:")
print(skill_counts.head(10))

# Plot the top ten tech
skill_counts.head(10).plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Technologies in HaveWorkedWith')
plt.ylabel('Frequency')
plt.xlabel('Technologies')
plt.xticks(rotation=45)
plt.show()

# Add a new column for number of skills each candidate has
data['SkillCount'] = data['HaveWorkedWith'].str.split(';').apply(len)

# Describe skill count distribution
print("\nSkill Count Summary:")
print(data['SkillCount'].describe())

# Visualize skill count distribution
data['SkillCount'].plot(kind='hist', bins=15, color='lightgreen', edgecolor='black', figsize=(8, 5))
plt.title('Distribution of Skill Count')
plt.ylabel('Frequency')
plt.xlabel('Number of Skills')
plt.show()

# Correlation between SkillCount and PreviousSalary
correlation = data[['SkillCount', 'PreviousSalary']].corr()
print("\nCorrelation Between Skill Count and Previous Salary:")
print(correlation)

# Boxplot: Skill count by employment status
sns.boxplot(x='Employed', y='SkillCount', data=data)
plt.title("Skill Count by Employment Status")
plt.ylabel('Number of Skills')
plt.xlabel('Employment Status(0 = Unemployed, 1 = Employed)')
plt.show()

# Group by education level and calculate the employment rate
edlevel_employment = data.groupby('EdLevel')['Employed'].mean()

# Sort the results in descending
edlevel_employment = edlevel_employment.sort_values(ascending=False)

print(edlevel_employment)

# Plot of employment rate by education level
edlevel_employment.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Employment Rate by Education Level')
plt.ylabel('Employment Rate')
plt.xlabel('Education Level')
plt.xticks(rotation=45)
plt.show()

# Filter out high performers to investigate closer
high_performers = data[data['EdLevel'].isin(['NoHigherEd', 'Other'])]

# Make a comparison of average skill count
avg_skills_high_performers = high_performers['SkillCount'].mean()
avg_skills_higher_ed = data[~data['EdLevel'].isin(['NoHigherEd', 'Other'])]['SkillCount'].mean()
print("\nAverage number of skills in the 'high performer' category:")
print(avg_skills_high_performers)
print("\nAverage number of skills in the 'higher ed' category:")
print(avg_skills_higher_ed)

high_performer_skills = high_performers['HaveWorkedWith'].str.split(';').explode()
high_performer_skillcounts = high_performer_skills.value_counts()

# Display the results
print("\nThe Top 10 Most Common Skills For High Performers Category:")
print(high_performer_skillcounts.head(10))