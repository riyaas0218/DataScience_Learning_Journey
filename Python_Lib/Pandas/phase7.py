import pandas as pd

january = pd.DataFrame({
    "Transaction_ID": [101, 102],
    "Sales": [5000, 3000]
})

february = pd.DataFrame({
    "Transaction_ID": [103, 104,101],
    "Sales": [4000, 6000]
})

combained=pd.concat([january,february],ignore_index=True)

print(combained)


result = pd.merge(
    february,
    january,
    on="Transaction_ID"
)


import pandas as pd

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
    "Department": ["IT", "HR", "IT", "Finance"],
    "Name": ["Riyas", "John", "Arun", "Kumar"]
})

salaries = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 105],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [50000, 40000, 45000, 35000]
})

result = pd.merge(
    employees,
    salaries,
    on=["Employee_ID", "Department"],
    how="inner"
)

second = pd.merge(
    employees,
    salaries,
    on=["Employee_ID", "Department"],
    how ="left"

)

print(result)
print(second)

df = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 101, 104, 102],
    "Name": ["Riyas", "John", "Arun", "Riyas", "Kumar", "John"],
    "Amount": [5000, 3000, 2000, 4000, 6000, 1500]
})
df["Customer_ID"].is_unique
df["Customer_ID"].duplicated().sum()
df[df["Customer_ID"].duplicated(keep=False)]