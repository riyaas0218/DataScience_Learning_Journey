import pandas as pd
from pathlib import Path

data_path = Path("data/raw")

for file in data_path.glob("*.csv"):

    df = pd.read_csv(file)

    print("\n" + "=" * 60)
    print("Dataset:", file.name)

    print("Total Rows:", len(df))
    print("Total Columns:", len(df.columns))

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)