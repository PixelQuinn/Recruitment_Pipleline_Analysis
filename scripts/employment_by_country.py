# Import libraries
import pandas as pd
import numpy as np

# Load dataset
file_path = "data/raw/recruitment_data.csv"
data = pd.read_csv(file_path)

# Group by country and calculate average employment rate
country_counts = data['Country'].value_counts()
valid_countries = country_counts[country_counts >= 50].index
filtered_data = data[data['Country'].isin(valid_countries)]

employment_rate_by_country = (
    filtered_data.groupby('Country')['Employed']
    .mean()
    .sort_values(ascending=False)
)

# Save to CSV
employment_rate_by_country.to_csv('data/processed/Employment_Rate_By_Country.csv', index=True)