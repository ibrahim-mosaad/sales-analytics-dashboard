import pandas as pd

def load_data():

    df = pd.read_csv("data/sales_data.csv", encoding="latin1")

    df.columns = df.columns.str.strip()

    df = df.rename(columns={
        "Order ID": "OrderID",
        "Order Date": "Date",
        "Product Name": "Product",
        "Category": "Category",
        "Region": "Region",
        "Sales": "Sales",
        "Profit": "Profit",
        "Quantity": "Quantity",
        "Customer ID": "CustomerID"
    })

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.dropna()

    return df