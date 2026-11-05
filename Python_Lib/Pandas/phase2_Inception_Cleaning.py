import pandas as pd

data = {
    "Name": ["Riyas", "John", "Arun", "Kumar", "Sam"],
    "Department": ["Data", "IT", "Analytics", "IT", "Data"],
    "Salary": [30000, 40000, 35000, 45000, 50000],
    "Experience": [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# print(df.head(3))
# print(df.tail(3))
# print(df.info())

# print(df.describe())
# 
# print(df.describe(include="all"))

# print(df.describe(include="str"))
# 
# 
# print(df.shape)
# print(df.size)
# print(df.ndim)
# print(df.dtypes)

# print(df["Department"].value_counts(normalize=True))

# df["Salary"] = df["Salary"].fillna()

df["Name"]=df["Name"].fillna("Unknown")
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
# print(df.isnull().sum())
df.dropna(axis=1)
df.dropna(axis=0)

data = {
    "Name": ["Riyas", "John", None, "Kumar"],
    "Salary": [30000, None, 35000, 45000],
    "Department": ["IT", "Data", "HR", None]
}

df = pd.DataFrame(data)
# print(df.dropna(axis=0))
# print(df.dropna(axis=1))


data = {
    "Customer": ["Riyas", "John", "Riyas", "Kumar", "John"],
    "Amount": [1000, 2000, 1000, 3000, 2000]
}

df = pd.DataFrame(data)
# 
# print(df.duplicated())
# print(df.drop_duplicates())
# print(df.drop_duplicates(keep="last"))
# print(df.drop_duplicates(keep=False))
# 

#This method converts a column from one data type to another.

df["Amount"] = df["Amount"].astype(float)


data = {
    "Employee": ["Riyas", "John", "Arun"],
    "Salary": ["30000", "40000", "50000"]
}

df = pd.DataFrame(data)

# print(df.dtypes)

df["Salary"] = df["Salary"].astype(float)
# 
# print(df.dtypes)
# 
# print(df["Salary"].mean())
# 

#What happens if a dataset contains invalid values?
#we need to handle one by one


data = {
    "Salary": ["30000", "40000", "Unknown", "50000"]
}
df = pd.DataFrame(data)


#when we try to convert type int float it will cause type error
# float("30000")    # 30000.0
# float("Unknown")  # ValueError

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

print(df)
print(df.dtypes)
print(df.isnull().sum())

# coerce → Convert invalid values into missing values.
# raise → Raise an error when invalid values are found.

