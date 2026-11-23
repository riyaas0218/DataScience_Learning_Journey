import pandas as pd
data={
     "Name": ["Riyas", "John", "Arun", "Kumar"],
    "Salary": [25000, 45000, 60000, 90000],
    "Department": ["IT", "Data", "IT", "HR"]
}
df=pd.DataFrame(data)


# Total salary per department
df.groupby("Department")["Salary"].sum()

# Average salary per department
df.groupby("Department")["Salary"].mean()

# Maximum salary per department
df.groupby("Department")["Salary"].max()

# Number of employees per department
df.groupby("Department")["Salary"].count()



import pandas as pd

data = {
    "Region": ["Chennai", "Chennai", "Bangalore", "Bangalore", "Chennai", "Bangalore"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Beauty"],
    "Sales": [5000, 2000, 7000, 3000, 4000, 1500],
    "Quantity": [2, 3, 4, 2, 3, 1]
}

df = pd.DataFrame(data)

df.groupby("Category")["Sales"].sum()
df.groupby("Region")["Sales"].mean()
df.groupby("Category")["Sales"].max()
df.groupby(["Region","Category"])["Sales"].sum()
df.groupby(["Region","Category"],as_index=False)["Sales"].sum()


#Topic 6.2 – Aggregation with agg()

df.groupby("Category")["Sales"].agg(["sum", "mean", "max", "min"])

#Named Aggregation 
df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Highest_Sales=("Sales", "max")
)


df.groupby("Category").agg(
    Total_sales =("Sales","sum"),
    Average_sales=("Sales","mean"),
    Highest_sales =("Sales","max"),
    total_quantity=("Quantity","count")
)


#transform()

df["Category_Average"] = (
    df.groupby("Category")["Sales"].transform("mean")
)

df["Department_Average"] = (
    df.groupby("Department")["Salary"].transform("mean")
)

df["Above_Average"] = (
    df["Salary"] > df["Department_Average"]
)

import pandas as pd

data = {
    "Region": ["Chennai", "Chennai", "Bangalore", "Bangalore", "Chennai", "Bangalore"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Beauty"],
    "Sales": [5000, 2000, 7000, 3000, 4000, 1500],
    "Quantity": [2, 3, 4, 2, 3, 1]
}

df = pd.DataFrame(data)
show=pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum"
)
print(show)


pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc=["sum", "mean", "max"],
    fill_value=0
)

pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0

)

import pandas as pd

data = {
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Category": ["Electronics", "Clothing", "Clothing", "Beauty",
                 "Electronics", "Electronics", "Beauty"]
}

df = pd.DataFrame(data)
pd.crosstab(df["Gender"], df["Category"],normalize="index",margins=True)