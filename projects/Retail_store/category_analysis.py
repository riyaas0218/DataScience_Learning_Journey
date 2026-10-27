
import pandas as pd

# Load the ORIGINAL dataset using its full path
file_path = r"D:\DataScience_Learning_Journey\projects\Retail_store\data\retail_sales_dataset.csv"

df = pd.read_csv(file_path)

# Verify that the correct file was loaded
print("Loaded file:", file_path)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Analyze revenue by category
category_revenue = df.groupby("Product Category")["Total Amount"].sum()
total_revenue=df["Total Amount"].sum()

revanue_percentage = (category_revenue/total_revenue)*100

print("\nRevenue percantage by category:")
print(revanue_percentage)
