import pandas as pd

customers = pd.read_csv(
    "data/raw/olist_customers_dataset.csv"
)

geo = pd.read_csv(
    "data/raw/olist_geolocation_dataset.csv"
)

orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)


# 1. Check customer_id uniqueness

print("CUSTOMER INVESTIGATION")

print("Total customer IDs:", customers["customer_id"].count())

print("Unique customer IDs:", customers["customer_id"].nunique())


# 2. Check geolocation duplicates

print("\nGEOLOCATION INVESTIGATION")

print(
    "Duplicate ZIP prefixes:",
    geo["geolocation_zip_code_prefix"].duplicated().sum()
)

print(
    "Unique ZIP prefixes:",
    geo["geolocation_zip_code_prefix"].nunique()
)


# 3. Investigate missing order timestamps

print("\nORDERS INVESTIGATION")

print(
    orders["order_status"].value_counts(dropna=False)
)

print("\nMissing delivery timestamps by order status:")

print(
    orders.groupby("order_status")[
        "order_delivered_customer_date"
    ].apply(lambda x: x.isnull().sum())
)

# 4. Investigate delivered orders with missing delivery timestamps

print("\nDELIVERED ORDERS WITH MISSING DELIVERY DATE")

problem_orders = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_customer_date"].isna())
]

print("Number of affected orders:", len(problem_orders))

print(
    problem_orders[
        [
            "order_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ]
)

print("\nINVESTIGATE THE 8 DELIVERED ORDERS")

print(
    problem_orders[
        [
            "order_id",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ].to_string(index=False)
)



# 5. Investigate Order Items
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

print("\nORDER ITEMS INVESTIGATION")
print("Total item records:", len(order_items))
print("Unique orders:", order_items["order_id"].nunique())

items_per_order = order_items.groupby("order_id").size()

print("Orders with multiple items:", (items_per_order > 1).sum())
print("Maximum items in one order:", items_per_order.max())

# 6. Investigate Payments
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")

print("\nPAYMENTS INVESTIGATION")
print("Total payment records:", len(payments))
print("Unique orders:", payments["order_id"].nunique())

payments_per_order = payments.groupby("order_id").size()

print("Orders with multiple payment records:", (payments_per_order > 1).sum())
print("Maximum payment records for one order:", payments_per_order.max())

print("\nPayment types:")
print(payments["payment_type"].value_counts())


# 6. Investigate products

products = pd.read_csv("data/raw/olist_products_dataset.csv")

print("\nPRODUCT INVESTIGATION")

print("Total products:", len(products))
print("Unique product IDs:", products["product_id"].nunique())

print("\nMissing values in product columns:")
print(products.isnull().sum())

print("\nProducts with missing category:")
print(
    products[products["product_category_name"].isna()]
    .head(5)
)

print("\nProducts with missing physical dimensions:")
print(
    products[products["product_weight_g"].isna() |
             products["product_length_cm"].isna() |
             products["product_height_cm"].isna() |
             products["product_width_cm"].isna()]
)


reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")

print("REVIEW SCORE DISTRIBUTION")
print(reviews["review_score"].value_counts().sort_index())

print("\nREVIEW SCORE PERCENTAGE")
print(
    reviews["review_score"]
    .value_counts(normalize=True)
    .sort_index() * 100
)