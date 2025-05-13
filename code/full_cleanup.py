import pandas as pd

# 1. Load your just-cleaned CSV
df = pd.read_csv('fv_lp_sourcing_clean.csv')

# 2. Drop the two fully-empty columns
df = df.drop(columns=[
    'Invest in Emerging VCs (Fund 1)?',
    'Anchor LP?'
])

# 3. (Optional) Verify they’re gone
print("Remaining columns:", list(df.columns))

# 4. Write out your final dataset
df.to_csv('fv_lp_sourcing_final.csv', index=False)
print("Final CSV saved as: fv_lp_sourcing_final.csv")