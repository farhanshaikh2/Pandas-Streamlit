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


st.title("Modern Building Leaders")
st.markdown(
    "Source Table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)"
)

with st.expander(label="see full data table"):
    st.write(df)

quarter = df["Quarter"].sort_values().str[:2].unique()
year_min_value = df["Quarter"].str[3:].astype("Int32").min()
year_max_value = df["Quarter"].str[3:].astype("Int32").max()

with st.form("Population-Form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Choose a Starting Date")
        start_quarter = st.selectbox(label="Quarter",options=quarter,key="start_q")
        start_year = st.slider("Year",min_value=year_min_value, max_value=year_max_value,key="start_y",step=1)

    with col2:
        st.write("Choose an End Date")
        end_quarter = st.selectbox(label="Quarter",options=quarter,key="end_q")
        end_year = st.slider("Year",min_value=year_min_value, max_value=year_max_value,key="end_y",step=1)
        
    with col3:
        st.write("Choose a Location")
        target = st.selectbox(label="Choose a Location",options=df.columns[1:].sort_values(), index=0)


    submit = st.form_submit_button("Analyse",type="primary")

start_date = f"{start_quarter} {start_year}"
end_date = f"{end_quarter} {end_year}"

def format_date_for_comparision(date):
    if date[1] == 2:
        return float(date[2:])*0.25
    elif date[1] == 3:
        return float(date[2:])*0.50
    elif date[1] == 4:
        return float(date[2:])*0.75
    else:
        return float(date[2:])

def end_before_start(start_date, end_date):
    num_start_date = format_date_for_comparision(start_date)
    num_end_date = format_date_for_comparision(end_date)

    if num_start_date > num_end_date:
        return True
    else:
        return False
    

def display_dashboard(start_date, end_date, target):
    tab1,tab2 = st.tabs(["Population Change","Compare"])

    with tab1:
        st.subheader(f"Population change from {start_date} to {end_date}")

        col1,col2 = st.columns(2)

        with col1:
            initial = df.loc[df["Quarter"] == start_date,target].item()
            final = df.loc[df["Quarter"] == end_date,target].item()
            percentage_diff = round((final-initial)/initial,2)
            delta = f"{percentage_diff}%"
            st.metric(start_date,value=initial)
            st.metric(end_date,final,delta=delta)
        
        with col2:
            start_idx = df.loc[df["Quarter"]==start_date].index.item()
            end_idx = df.loc[df["Quarter"]==end_date].index.item()

            filtered_df = df.iloc[start_idx:end_idx+1]
            fig,ax = plt.subplots()
            ax.plot(filtered_df['Quarter'],filtered_df[target])
            ax.set_xlabel("Population")
            ax.set_ylabel("Target")
            ax.set_xticks([filtered_df["Quarter"].iloc[0], filtered_df["Quarter"].iloc[-1]])
            fig.autofmt_xdate()
            st.pyplot(fig)

    with tab2:
        st.subheader("Compare with Other Locations")
        all_targets = st.multiselect("Choose Other Location",options=df.columns[1:],default=target)

        fig, ax = plt.subplots()
        for each in all_targets:
            ax.plot(filtered_df['Quarter'],filtered_df[each])
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        ax.set_xticks([filtered_df["Quarter"].iloc[0], filtered_df["Quarter"].iloc[-1]])
        fig.autofmt_xdate()
        
        st.pyplot(fig)


if start_date not in df["Quarter"].to_list() or end_date not in df["Quarter"].to_list():
    st.error("No Data available. Check your quarter and year selection")
elif end_before_start(start_date,end_date):
    st.error("Dates don't work, Start Date must be before end date")
else:
    display_dashboard(start_date,end_date,target)