import pandas as pd
df =pd.read_csv("data/retail_sales_dataset.csv")
# print(df.head())

# print("Number of Row and column in CSV file")
# print(df.shape)

# print("Number of Columns")
# print(df.columns.to_list())


# print("Data type and non missing values")
# df.info()


# print("Missing values in each column")
# print(df.isnull().sum())
# 
print("Check the duplicate Record")
print(df.duplicated().sum())

# 
print("Check the dupilcate transaction id")
print(df["Transaction ID"].duplicated().sum())

dates = pd.to_datetime(df["Date"],errors="coerce")
print('\n Invalid Dates')

print(dates.isna().sum())


print("\n Dates Range")
print(dates.min(),'to',dates.max())


# 4. Verify recorded amounts
expected_amount = df["Quantity"] * df["Price per Unit"]

mismatch = df["Total Amount"] != expected_amount

print("\nIncorrect total amounts:")
print(mismatch.sum())

# 5. Inspect numerical ranges
print("\nNumerical summary:")
print(df[["Age", "Quantity", "Price per Unit", "Total Amount"]].describe())