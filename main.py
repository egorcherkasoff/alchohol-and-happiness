import streamlit as st
import plotly.express as pl
from modules.get_data import get_data


def filter_data(opt_reg, opt_x, opt_y, df):
    # check if user picked "All" region option
    if opt_reg != "All Regions":
        res_x = df.loc[df["Region"] == opt_reg][opt_x]
        res_y = df.loc[df["Region"] == opt_reg][opt_y]
    else:
        res_x = df[opt_x]
        res_y = df[opt_y]
    return res_x, res_y


# check if file exists
try:
    df = get_data()
except FileNotFoundError:
    st.warning("Data file not found. Check if it exists in data folder.")

region_options = {}
region_options = df["Region"].drop_duplicates()
region_options["all"] = "All Regions"


# Connection of user friendly options and colums in dataframe
axis_options = {
    "GDP Per Capita": "GDP_PerCapita",
    "Beer Per Capita": "Beer_PerCapita",
    "Spirit Per Capita": "Spirit_PerCapita",
    "Wine Per Capita": "Wine_PerCapita",
    "Happiness Score": "HappinessScore",
    "Human Development Index": "HDI",
}

# check if loaded dataframe
if df is not None:
    st.title("Happiness and Alcohol Consumption")
    st.write("By [egorcherkasoff](https://github.com/egorcherkasoff)")

    # config the graph
    filter_option = st.selectbox("Filter by region", options=region_options)

    x_option = axis_options[
        st.selectbox("Select data for X-axis", options=axis_options)
    ]

    y_option = axis_options[
        st.selectbox("Select data for Y-axis", options=axis_options)
    ]

    # display the graph

    data_x, data_y = filter_data(filter_option, x_option, y_option, df)

    st.subheader(
        f" {x_option.replace('_', ' ')} to {y_option.replace('_', ' ')} in {filter_option}"
    )

    chart_figure = pl.scatter(x=data_x, y=data_y, labels={"x": x_option, "y": y_option})
    st.plotly_chart(chart_figure)
