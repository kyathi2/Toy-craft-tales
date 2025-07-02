import pandas as pd

# Load the dataset
df = pd.read_csv('../dataset/manufacturer_data.csv')

# Clean data (remove nulls and calculate Profit)
df.dropna(inplace=True)
df['Profit'] = df['Revenue'] - (df['UnitsSold'] * df['ManufacturingCost'])

# Save cleaned data
df.to_csv('../dataset/cleaned_data.csv', index=False)

print("✅ Data cleaned and saved to cleaned_data.csv")
