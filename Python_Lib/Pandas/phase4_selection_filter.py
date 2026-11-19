import pandas as pd

data = {
    "Name": ["Riyas", "John", "Arun", "Kumar"],
    "Department": ["IT", "Data", "IT", "HR"],
    "Salary": [30000, 40000, 35000, 45000],
    "Experience": [1, 3, 2, 5]
}
#Advanced loc[]
df = pd.DataFrame(data, index=["E1", "E2", "E3", "E4"])
df.loc["E2", "Salary"]

df.loc["E3"]
df.loc["E1",["Name","Salary"]]
df.loc[["E1","E2","E3"],"Salary"]

df.loc["E1" : "E3"]
df.loc["E1":"E3",["Name","Department"]]
df.loc[df["Salary"] > 35000]

df.loc[df["Salary"] > 30000 and df["Experience"]>=3, ["Name", "Salary","Experience"]]

df.loc[(df["Salary"]>40000) | (df["Experience"]>=5) ,["Name","Salary"]]

#Advanced iloc[]

df.iloc[0]
df.iloc[2]
df.iloc[0:3]


df.iloc[0:3, 0:2]
df.iloc[0:, 3]
df.iloc[0:4:2, 0:3:2]


#Boolean Indexing
#Boolean indexing means filtering rows based on conditions that return True or False.

df[df["Salary"]>30000]
df[df["Experience"]<3]
df[(df["Salary"]>30000) & (df["Salary"]<40000)]
df[df["Salary"].between(30000, 40000)]

df[(df["Amount"]>5000) | (df["Quantity"]>=5)]


#Advanced Filtering with query()


df.query("Salary > 35000 and Experience >= 3")

df.query("Salary > 40000 or Experience < 3")


min_salary = 35000

df.query("(Salary > @min_salary ) and (Experience>=3)")




df[~(df["Department"] == "IT")  & (df["Salary"]>30000)]

df.loc[
    (df["Department"].isin(["IT", "Data"])) &
    (df["Salary"] > 30000),
    ["Name", "Department", "Salary"]
]
df.loc[
    (df["Product Category"].isin(["Electronics", "Beauty"])) &
    (df["Total Amount"].between(1000, 10000)) &
    (df["Quantity"] > 1),
    ["Transaction ID", "Product Category", "Quantity", "Total Amount"]
]