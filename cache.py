import streamlit as st
import time
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Cache demonstration")

st.button("Test Cache")

st.subheader("st.cache_data")
time.sleep(2)

st.subheader("st.cache_resources")
