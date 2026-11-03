# Pandas Mastery
# 10 Phases

# 10
# Total learning phases

# 1

# Pandas Fundamentals

# Series, DataFrame, indexes, construction, architecture

# 8+ topic areas



# 2

# Data Inspection

# head, tail, info, describe, shape, dtypes, memory

# 8+ topic areas



# 3

# Data Cleaning

# Missing values, duplicates, outliers, type conversion

# 10+ topic areas



# 4

# Selection & Filtering

# loc, iloc, Boolean indexing, query, slicing

# 10+ topic areas



# 5

# Data Transformation

# apply, map, lambda, replace, astype, vectorization

# 10+ topic areas



# 6

# Grouping & Aggregation

# groupby, agg, transform, pivot tables, crosstab

# 10+ topic areas



# 7

# Combining Datasets

# merge, join, concat, index alignment

# 8+ topic areas



# 8

# Date & Time Analysis

# Datetime, periods, resampling, time series

# 8+ topic areas



# 9

# Advanced Pandas

# MultiIndex, memory optimization, performance, advanced operations

# 10+ topic areas



# 10

# Real-World Projects

# End-to-end analytics, ETL, business insights, data pipelines

# 4 projects topic areas









import pandas as pd
prices = pd.Series([5000,233,223])
print(prices)
print(prices.index)
print(prices.values)
print(prices.dtype)
print(prices.shape)
print(prices.ndim)

#Can we create our own index?

prices = pd.Series(
    [50000, 500, 1500],
    index=["Laptop", "Mouse", "Keyboard"]
)

print(prices)

#create DATA FRAME
products = ["Laptop", "Mouse", "Keyboard"]
prices = [50000, 500, 1500]
quantities = [2, 3, 1]

#1 Convert to SERIES
product_series = pd.Series(products)
price_series = pd.Series(prices)
quantity_series = pd.Series(quantities)
#@CONVER TO DF

df = pd.DataFrame({
    "Product": product_series,
    "Price": price_series,
    "Quantity": quantity_series
})

print(df)
print(df.index)
print(df.columns)
print(df.shape)
print(df.ndim)


#index alignment.  
#Because Pandas aligns Series by their index labels, not simply by their positions.

name=pd.Series(["Riyas","Asiga","Ajim"],
               index=[0,1,2])
age=pd.Series([22,23,31],
               index=[1,2,3])

df=pd.DataFrame({
    "Name":name,
    "Age":age
})
print(df)


#Dictionary With Multiple List

data = {
    "Name": ["Riyas", "John", "Arun", "Kumar", "Sam"],
    "Department": ["Data", "IT", "Analytics", "IT", "Data"],
    "Salary": [50000, 50000, 20000, 40000, 30000],
    "Experience": [0, 1, 3, 4, 2]
}

df_1 = pd.DataFrame(data)

print(df_1)

print("\nShape:")
print(df_1.shape)

print("\nData types:")
print(df_1.dtypes)

print("\nAverage salary:")
print(df_1["Salary"].mean())


#List with Mutiple Dictionary

data = [
    {"Name": "Riyas", "Salary": 50000},
    {"Name": "John", "Salary": 40000},
    {"Name": "Arun", "Department": "Data"}
]

df = pd.DataFrame(data)

print(df)
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())



import pandas as pd

data = {
    "Name": ["Riyas", "John", "Arun"],
    "Department": ["Data", "IT", "Analytics"]
}

df = pd.DataFrame(
    data,
    index=["E101", "E102", "E103"]
)

print(df)
print(df.index)
print(df.loc["E102"])
print(df.iloc[2])
print(df.loc["E103", "Name"])