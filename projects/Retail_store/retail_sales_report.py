
import pandas as pd

# Create a summary of key business metrics
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
        456000,
        1000,
        2514,
        456,
        "Electronics",
        "Clothing",
        "2023-05"
    ]
})

print(summary)

summary.to_csv("retail_sales_summary.csv", index=False)

print("\nSummary exported successfully!")
