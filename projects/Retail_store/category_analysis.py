
import pandas as pd
import matplotlib.pyplot as plt
# Load the ORIGINAL dataset using its full path
file_path = r"D:\DataScience_Learning_Journey\projects\Retail_store\data\retail_sales_dataset.csv"

df = pd.read_csv(file_path)

#Verify that the correct file was loaded
print("Loaded file:", file_path)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

#Analyze revenue by category

category_revenue = df.groupby("Product Category")["Total Amount"].sum()
total_revenue=df["Total Amount"].sum()

revanue_percentage = (category_revenue/total_revenue)*100

print("\nRevenue percantage by category:")
print(revanue_percentage)

# 
df["Date"] = pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.to_period("M")
monthly_revenue=df.groupby("Month")["Total Amount"].sum()
print("Mothly Revenue \n")
print(monthly_revenue)

#Quantity Sold by Category

category_quantity = df.groupby("Product Category")["Quantity"].sum()
print('the quantity soled by category')
print("\n ",category_quantity)


#average Revune bu Category

average_revenue_by_category = category_revenue / category_quantity
print("Average Revenue by Category")
print(average_revenue_by_category)



# category_revenue.plot(kind="bar")
# plt.title("Revenue by Category")
# plt.xlabel("Product Category")
# plt.ylabel("total reveune")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()
# 
# 
# monthly_revenue.plot(kind="line",marker="o")
# plt.title("Mothly Reveune")
# plt.xlabel("Month")
# plt.ylabel("Total Revenue")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()
# plt.show()
# 

#check the number of monthly Transaction

monthly_transaction = df.groupby("Month")["Transaction ID"].count()
print("Transaction Count by Month")
print("\n",monthly_transaction)

january_date=df[df["Month"]=="2024-01"]
print("\nJanuary 2024 Transactions:")
print(january_date[["Date","Transaction ID","Total Amount"]])
print("\n January Transaction Count",len(january_date))



# Key business metrics
total_revenue = df["Total Amount"].sum()
total_transactions = df["Transaction ID"].nunique()
total_units_sold = df["Quantity"].sum()
average_transaction_value = total_revenue / total_transactions

print("\n===== RETAIL SALES SUMMARY =====")
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Transactions: {total_transactions}")
print(f"Total Units Sold: {total_units_sold}")
print(f"Average Transaction Value: {average_transaction_value:,.2f}")
print(f"Top Revenue Category: {category_revenue.idxmax()}")
print(f"Top Selling Category: {category_quantity.idxmax()}")
print(f"Highest Revenue Month: {monthly_revenue.idxmax()}")
