# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "data/raw/recruitment_data.csv"
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
undergraduate_students = data[data['EdLevel'].isin(['Undergraduate'])]
master_students = data[data['EdLevel'].isin(['Master'])]
phd_students = data[data['EdLevel'].isin(['PhD'])]

# Make a comparison of average skill count
avg_skills_high_performers = high_performers['SkillCount'].mean()
avg_skills_undergrad = undergraduate_students['SkillCount'].mean()
avg_skills_master = master_students['SkillCount'].mean()
avg_skills_phd = phd_students['SkillCount'].mean()

print("\nAverage number of skills in the 'high performer' category:")
print(avg_skills_high_performers)
print("\nAverage number of skills of Undergraduate Students:")
print(avg_skills_undergrad)
print("\nAverage number of skills of Master Students:")
print(avg_skills_master)
print("\nAverage number of skills of PhD Students:")
print(avg_skills_phd)

high_performer_skills = high_performers['HaveWorkedWith'].str.split(';').explode()
high_performer_skillcounts = high_performer_skills.value_counts()
undergrad_skills = undergraduate_students['HaveWorkedWith'].str.split(';').explode()
undergrad_skillcounts = undergrad_skills.value_counts()
master_skills = master_students['HaveWorkedWith'].str.split(';').explode()
master_skillcounts = master_skills.value_counts()
phd_skills = phd_students['HaveWorkedWith'].str.split(';').explode()
phd_skillcounts = phd_skills.value_counts()

# Display the results
print("\nThe Top 10 Most Common Skills For No Higher Education:")
print(high_performer_skillcounts.head(10))
print("\nThe Top 10 Most Common Skills For Undergraduate Students:")
print(undergrad_skillcounts.head(10))
print("\nThe Top 10 Most Common Skills For Master Students:")
print(master_skillcounts.head(10))
print("\nThe Top 10 Most Common Skills For PhD Students:")
print(phd_skillcounts.head(10))

# Funct to handle multiple skills as needed to analyze
for skill in ['Python', 'AWS', 'JavaScript', 'Docker', 'HTML/CSS', 'SQL']:
    skill_users = data[data['HaveWorkedWith'].str.contains(skill, na=False)]
    avg_salary = skill_users['PreviousSalary'].mean()
    print(f"Average salary for {skill} users: {avg_salary:.2f}")