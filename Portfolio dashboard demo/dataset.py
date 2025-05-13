import pandas as pd
import random
import numpy as np

# Define dummy company names and industries
company_names = ["EcoEnergy", "BlueTech", "SolarWave", "AIGrid", "GreenFusion", "HydroNext", "ClimateCore", "FusionX", "TerraVolt", "WindSynergy"]
industries = ["Climate Tech", "Deep Tech", "AI", "Renewable Energy", "Space Tech", "Ocean Tech"]

# Generate dummy data
num_companies = 10
data = {
    "Company Name": random.choices(company_names, k=num_companies),
    "Industry": random.choices(industries, k=num_companies),
    "Founded Year": [random.randint(2005, 2022) for _ in range(num_companies)],
    "HQ Location": random.choices(["San Francisco, USA", "Berlin, Germany", "Bangalore, India", "London, UK", "Toronto, Canada"], k=num_companies),
    "Founder Count": [random.randint(1, 5) for _ in range(num_companies)],
    "Total Employees": [random.randint(10, 500) for _ in range(num_companies)],

    # Financial Metrics
    "Annual Recurring Revenue (USD)": [random.randint(500000, 50000000) for _ in range(num_companies)],
    "Burn Rate (USD)": [random.randint(10000, 1000000) for _ in range(num_companies)],
    "Runway (Months)": [random.randint(6, 36) for _ in range(num_companies)],
    "EBITDA (USD)": [random.randint(-200000, 1000000) for _ in range(num_companies)],
    "Gross Margin (%)": [round(random.uniform(20, 80), 2) for _ in range(num_companies)],
    "Revenue Growth Rate (%)": [round(random.uniform(-10, 100), 2) for _ in range(num_companies)],

    # Investment Metrics
    "Total Capital Raised (USD)": [random.randint(1000000, 100000000) for _ in range(num_companies)],
    "Last Funding Round": random.choices(["Seed", "Series A", "Series B", "Series C"], k=num_companies),
    "Valuation (USD)": [random.randint(5000000, 500000000) for _ in range(num_companies)],
    "Investor Count": [random.randint(1, 10) for _ in range(num_companies)],
    "Exit Status": random.choices(["Active", "IPO", "Acquired", "Failed"], k=num_companies),

    # Operational Metrics
    "Product Development Stage": random.choices(["Prototype", "MVP", "Scaling", "Mature"], k=num_companies),
    "Customer Growth Rate (%)": [round(random.uniform(-5, 50), 2) for _ in range(num_companies)],
    "Sustainability Score": [random.randint(1, 10) for _ in range(num_companies)]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
csv_path = "/mnt/data/portfolio_dashboard_dummy_data.csv"
df.to_csv(csv_path, index=False)

# Display DataFrame
import ace_tools as tools
tools.display_dataframe_to_user(name="Dummy Portfolio Data", dataframe=df)

# Provide file download link
csv_path