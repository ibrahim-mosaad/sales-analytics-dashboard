def create_target(df):


    df["ProfitLabel"] = df["Profit"].apply(
        lambda x: 1 if x > df["Profit"].median() else 0
    )

    return df


def calculate_kpis(df):

    return {
        "sales": df["Sales"].sum(),
        "profit": df["Profit"].sum(),
        "orders": df["OrderID"].nunique(),
        "customers": df["CustomerID"].nunique()
    }