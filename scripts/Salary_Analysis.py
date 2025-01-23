# Import libraries
import pandas as pd
import numpy as np

file_path = ("data/raw/recruitment_data.csv")
data = pd.read_csv(file_path)

# Average salary by education level
avg_salary_by_edlevel = data.groupby('EdLevel')['PreviousSalary'].mean()

# Average salary by gender
avg_salary_by_gender = data.groupby('Gender')['PreviousSalary'].mean()

# Save to CSV
avg_salary_by_edlevel.to_csv('data/processed/Salary_By_EdLevel.csv', index=True)
avg_salary_by_gender.to_csv('data/processed/Salary_By_Gender.csv', index=True)