import pandas as pd
from pathlib import Path

file_path = r"D:\DataScience_Learning_Journey\projects\Retail_store\data\retail_sales_dataset.csv"
df=pd.read_csv(file_path)

print("Data set Loaded Successfully")


total_revenue =df["Total Amount"].sum()
total_transactions=df["Transaction ID"].nunique()
total_units_sold =df["Quantity"].sum()

average_transaction_value = total_revenue / total_transactions
# print("Total Revenue:", total_revenue)
# print("Total Transactions:", total_transactions)
# print("Total Units Sold:", total_units_sold)
# print("Average Transaction Value:", average_transaction_value)
# 

category_revenue = df.groupby("Product Category")["Total Amount"].sum()

category_quantity = df.groupby("Product Category")["Quantity"].sum()

top_revenue_category = category_revenue.idxmax()

top_selling_category = category_quantity.idxmax()
# 
# print("Top Revenue Category:", top_revenue_category)
# print("Top Selling Category:", top_selling_category)


df["Date"]=pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y"
)
df["Month"]=df["Date"].dt.to_period("M")
Monthly_revenue=df.groupby("Month")["Total Amount"].sum()
highest_revenue_month=Monthly_revenue.idxmax()
# print("Highest Revenue Month",highest_revenue_month)
# 

summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Transactions",
        "Total Units Sold",
        "Average Transaction Value",
        "Top Revenue Category",
        "Top Selling Category",
        "Highest Revenue Month"
    ],
    "Value": [
        total_revenue,
        total_transactions,
        total_units_sold,
        average_transaction_value,
        top_revenue_category,
        top_selling_category,
        str(highest_revenue_month)
    ]
})

print("\n===== RETAIL SALES REPORT =====")
print(summary)

from pathlib import Path

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

output_file = output_folder / "retail_sales_summary.csv"

summary.to_csv(output_file, index=False)

print("\nReport saved successfully!")
print("File location:", output_file.resolve())