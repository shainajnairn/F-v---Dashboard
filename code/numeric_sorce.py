import pandas as pd
import re

def parse_suffix(val):
    """
    Convert strings like '100k', '1.5M', '2B' into numeric values.
    Handles case ‐ insensitive suffixes:
      k → thousand (× 1e3)
      M → million  (× 1e6)
      B → billion  (× 1e9)
    Falls back to float(val) or 0 if unparseable.
    """
    if pd.isna(val):
        return 0
    s = str(val).strip()
    match = re.match(r'^([\d,.]+)\s*([kKmMbB])?$', s)
    if not match:
        # no suffix, just try to parse directly
        try:
            return float(s.replace(',', ''))
        except:
            return 0
    number, suffix = match.groups()
    # remove any commas
    number = float(number.replace(',', ''))
    if not suffix:
        return number
    suf = suffix.upper()
    if suf == 'K':
        return number * 1e3
    if suf == 'M':
        return number * 1e6
    if suf == 'B':
        return number * 1e9
    return number

# 1. Load your cleaned CSV
df = pd.read_csv('fv_lp_sourcing_final.csv')

# 2. Apply parsing to both columns
for col in ['Min Check','Max Check']:
    df[col] = df[col].apply(parse_suffix)

# 3. (Optional) Convert to int if you want whole numbers
df['Min Check'] = df['Min Check'].round(0).astype(int)
df['Max Check'] = df['Max Check'].round(0).astype(int)

# 4. Save the result
df.to_csv('fv_lp_sourcing_numeric.csv', index=False)
print("Written numeric CSV: fv_lp_sourcing_numeric.csv")