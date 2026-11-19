import pandas as pd
data={
     "Name": ["Riyas", "John", "Arun", "Kumar"],
    "Salary": [25000, 45000, 60000, 90000],
    "Age":[17, 22, 35, 65]
}
df=pd.DataFrame(data)

def salary_category(salary):
    if salary < 30000:
        return "Low"
    elif salary <= 60000:
        return "Medium"
    else:
        return "High"

df["Salary_Category"] = df["Salary"].apply(salary_category)


def age_category(age):
    if age<18:
        return "Minor"
    elif age>=18 and age<=59:
        return "Adult"
    else:
        return "Senior"

df["Age_category"]=df["Age"].apply(age_category)



df["salary_Category"] = df["Salary"].apply(salary_category)


data = {
    "Math": [80, 90, 70],
    "Science": [85, 95, 75],
    "English": [75, 85, 65]
}

marks = pd.DataFrame(data)

def calculate_total(row):
    return row.sum()

marks["Total"] = marks.apply(calculate_total, axis=1)
    


#Map

import pandas as pd

data = {
    "Name": ["Riyas", "John", "Arun", "Kumar"],
    "Department": ["IT", "Data", "IT", "HR"]
}

df = pd.DataFrame(data)

department_mapping = {
    "IT": "Information Technology",
    "Data": "Data Science",
    "HR": "Human Resources"
}

df["Department"] = df["Department"].map(department_mapping)
print(df["Department"])


#lampda

df["Age_category"] = df["Age"].apply(
    lambda age: "minor" if age<18  else "Adult" if age>=18 and age<59 else "Senior"
)


#Replace

df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "F": "Female"
})

df["Status"] = df["Status"].replace({
    "Y": "Active",
    "N": "Inactive"
})