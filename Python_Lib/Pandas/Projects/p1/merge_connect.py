
import pandas as pd

# Load CSV files
customers = pd.read_csv("Customers.csv")
orders = pd.read_csv("Orders.csv")
products = pd.read_csv("Products.csv")

# Clean column names
customers.columns = customers.columns.str.strip()
orders.columns = orders.columns.str.strip()
products.columns = products.columns.str.strip()

# Merge customers and orders
customer_orders = pd.merge(
    customers,
    orders,
    on="Customer_ID",
    how="inner"
)

# Merge with products
final_df = pd.merge(
    customer_orders,
    products,
    on="Product_ID",
    how="inner"
)

print(final_df)
