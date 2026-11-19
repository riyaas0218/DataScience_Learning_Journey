import pandas as pd
import numpy as np
data={
    "Employee" : ["Riyas", "John", "Arun", "Kumar", "John"],
    "Age":[24, 26, np.nan, 28, 26],
    "Salary":[30000, 40000, 35000, -5000, 40000],
    "Department":["IT", "Data", "IT", "data", "Data"]
}
df=pd.DataFrame(data)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())

df["Department"] = df["Department"].str.upper()
print(df["Department"].value_counts())


df["Age"]=df["Age"].fillna(df["Age"].median())
df["Department"]=df["Department"].fillna(df["Department"].mode()[0])




data = {
    "Date": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Stock_Price": [100, None, None, 110, 120]
}

df = pd.DataFrame(data)
df["Forward_Fill"]=df["Stock Price"].ffill()
df["Backward_Fill"]=df["Stock Price"].bfill()

df.duplicated()
df.duplicated().sum()
df = df.drop_duplicates()


#df.duplicated() → No duplicate rows.
#df.duplicated(subset=["Transaction_ID"]) → One duplicate ID.

# Find duplicate transactions based on Transaction_ID
df.duplicated(subset=["Transaction_ID"]).sum()

# Remove duplicate transactions based on Transaction_ID
df = df.drop_duplicates(subset=["Transaction_ID"])



data = {
    "Customer_ID": ["C101", "C101", "C102", "C101"],
    "Transaction_ID": ["T001", "T002", "T003", "T004"],
    "Amount": [1000, 2000, 1500, 3000]
}

df = pd.DataFrame(data)

count_dup_customer=df.duplicated(subset=["Customer_ID"]).sum()
count_dup_transaction=df.duplicated(subset=["Transaction_ID"]).sum()

df["Transaction_ID"].is_unique()

df["Department"].str.replace(" ", "")

df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "M": "Male",
    "female": "Female",
    "F": "Female"
})
print(df["Gender"].value_counts())



#IQR METHOD 


q1 = df["Salary"].quantile(0.25)
q3 = df["Salary"].quantile(0.75)

IQR = q3-q1
lower_bound = q1 - (1.5*(IQR))
upper_bound =q3 + (1.5*(IQR))

outliers = df[
    (df["Salary"] < lower_bound) |
    (df["Salary"] > upper_bound)
]

print(outliers)



#Capping
df["Capped_Salary"] = np.clip(
    df["Salary"],
    lower_bound,
    upper_bound
)
# 
# Behind the scenes:
# - Values below the lower bound become the lower bound.
# - Values above the upper bound become the upper bound.
# - Values inside the boundaries remain unchanged.



invalid_age = df[df["Age"] < 18]

invalid_salary = df[df["Salary"] < 0]

valid_employee = df.query("Age>18 and salary>0")


#Data Validation with assert

assert (df["Salary"] > 0).all()
assert (df["Age"]>=18).all()
assert(df["Transaction_ID"].is_unique).all()