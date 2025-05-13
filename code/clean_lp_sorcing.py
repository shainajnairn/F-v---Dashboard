import pandas as pd

# 1. Load your raw Excel sheet
file_in  = r"C:\\Users\\nived\\OneDrive\\Desktop\\Spring 2025\\frankenbuild ventures\\dashboard\\F(v) - LP Sourcing.xlsx"
df = pd.read_excel(file_in, sheet_name='Climate Tech | Master')

# 2. Fill defaults
text_cols = ['Fund Type','URL','Tech Type','Focus','Stage','Geography','City','Country']
num_cols  = ['Min Check','Max Check']

for c in text_cols:
    df[c] = df[c].fillna('Unknown')

for c in num_cols:
    df[c] = df[c].fillna(0)

# 3. Confirm no more missing data
missing_after = (df.isna().mean() * 100).round(1)
print("Missing % after cleanup:\n", missing_after)

# 4. Write cleaned file
file_out = r'C:\\Users\\nived\\OneDrive\\Desktop\\Spring 2025\\frankenbuild ventures\\dashboard\\fv_lp_sourcing_clean.csv'
df.to_csv(file_out, index=False)
print(f"\nCleaned CSV written to:\n  {file_out}")