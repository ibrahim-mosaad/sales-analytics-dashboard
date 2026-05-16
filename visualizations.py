import plotly.express as px


def sales_by_region(df):

    data = df.groupby("Region")["Sales"].sum().reset_index()

    fig = px.bar(data, x="Region", y="Sales", title="Sales by Region")

    return fig


def profit_distribution(df):

    fig = px.histogram(df, x="Profit", nbins=30, title="Profit Distribution")

    return fig