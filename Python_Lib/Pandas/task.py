import pandas as pd
import numpy as np
a = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)

b = pd.Series(
    [10, 20, 40],
    index=["B", "C", "D"]
)

result = a + b

print(result)



data = {
    "Name": ["Riyas", "John", "Arun"],
    "Salary": [30000, 40000, 50000]
}

df = pd.DataFrame(
    data,
    index=["E01", "E02", "E02"]
)

print(df)
print(df.loc["E02"])
print(df.index.is_unique)
print(df.index.duplicated())



data = {
    "EmployeeID": ["E01", "E02", "E03"],
    "Name": ["Riyas", "John", "Arun"],
    "Salary": [30000, 40000, 50000]
}

df = pd.DataFrame(data)

print(df)
df = df.set_index("EmployeeID")

print(df)
df = df.reset_index()

print(df)


data = {
    "Name": ["Riyas", "John", "Arun", "Kumar", "Sam"],
    "Department": ["Data", "IT", "Analytics", "IT", "Data"],
    "Salary": [30000, 40000, 35000, 45000, 50000],
    "Experience": [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

print(df["Salary"])
print(df[["Name","Department"]])
print(df.iloc[2])
print(df.loc[1,["Name","Salary"]])
print(df.iloc[0:3, 0:2])
print(df["Salary"].shape)
print(type(df["Salary"]))

print(df[["Salary"]].shape)
print(type(df[["Salary"]]))



df["Annual Salary"]=df["Salary"]*2
df["Experience Category"] = np.where(
    df["Experience"] < 2,
    "Junior",
    np.where(
        df["Experience"].between(2, 4),
        "Mid-Level",
        "Senior"
    )
)

df.loc[df["Department"] == "IT", "Salary"] = df["Salary"] * 1.10

df.loc[
    (df["Department"] == "IT") & (df["Experience"] >= 3),
    "Salary"
] = df["Salary"] * 1.15


#Approach 1 – Modify the existing DataFrame
df.drop(columns=["Annual Salary"], inplace=True)

#Approach 2 – Return a new DataFrame and assign it
df = df.drop(columns=["Annual Salary"])


df = df.drop(index=df[df["Experience"] < 2].index)


df = df.rename(columns={
    "Name": "Employee Name",
    "Salary": "Monthly Salary"
})


df.sort_values(by="Salary", ascending=True)

df.sort_values(
    by=["Department", "Experience"],
    ascending=[True, False]
)


df_copy = df.copy()

df_copy.loc[0, "Salary"] = 100000

print(df["Salary"])
print(df_copy["Salary"])