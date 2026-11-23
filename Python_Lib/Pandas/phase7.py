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


