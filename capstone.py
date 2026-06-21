import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

URL = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"

df = pd.read_csv(
    URL,
    dtype={
        "Quarter": str,
        "Canada": np.int32,
        "Newfoundland and Labrador": np.int32,
        "Prince Edward Island": np.int32,
        "Nova Scotia": np.int32,
        "New Brunswick": np.int32,
        "Quebec": np.int32,
        "Ontario": np.int32,
        "Manitoba": np.int32,
        "Saskatchewan": np.int32,
        "Alberta": np.int32,
        "British Columbia": np.int32,
        "Yukon": np.int32,
        "Northwest Territories": np.int32,
        "Nunavut": np.int32,
    },
)


st.title("Population of Canada")
st.markdown(
    "Source Table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)"
)

with st.expander(label="See full data table"):
    st.write(df)

with st.form("Population-form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Choose a starting Date")
        start_quarter = st.selectbox(
            label="Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q"
        )
        start_year = st.slider(
            label="Year",
            min_value=1991,
            max_value=2023,
            value=1991,
            step=1,
            key="start_y",
        )

    with col2:
        st.write("Choose a Ending Date")
        end_quarter = st.selectbox(
            label="Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=0, key="end_q"
        )
        end_year = st.slider(
            label="Year",
            min_value=1991,
            max_value=2023,
            value=1991,
            step=1,
            key="end_y",
        )

    with col3:
        st.write("Choose a Location")
        target = st.selectbox("Choose a location", options=df.columns[1:], index=0)

    submit_btn = st.form_submit_button(label="Analyse", type="primary")
