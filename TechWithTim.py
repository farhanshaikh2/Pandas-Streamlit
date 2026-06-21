import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Dashboard Data")

uploaded_file = st.file_uploader(label="Choose a CSV File", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.to_list()
    selected_column = st.selectbox(label="Select columns to filter by", options=columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox(
        label="Select a value to filter by", options=unique_values
    )
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Area")
    x_column = st.selectbox(label="Select x-axis columns", options=columns)
    y_column = st.selectbox(label="Select y-axis columns", options=columns)

    if st.button("Generate Plot"):
        st.line_chart(
            filtered_df.set_index(x_column)[y_column],
        )
else:
    "Waiting for File upload"
