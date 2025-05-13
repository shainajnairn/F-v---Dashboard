import pandas as pd

df = pd.read_excel('F(v) - LP Sourcing.xlsx', sheet_name='Climate Tech | Master')
missing = df.isna().mean().round(3) * 100
print(missing)