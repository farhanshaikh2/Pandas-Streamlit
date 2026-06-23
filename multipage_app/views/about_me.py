import streamlit as st

from Forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# -----HERO SECTION-------------
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    pass

with col2:
    st.title("Farhan Shaikh", anchor=False)
    st.write(
        "Senior Data Analyst, assisting enterprise by supporting data-driven decision-making."
    )
    if st.button("📨 Contact Me"):
        show_contact_form()

# -------EXPERIENCE & QUALIFICATIONS-------------
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write("""
    - 24 years experience in Trade Finance
    - Strong hands on in Python and Excel
    - Good understanding of statistical Principles and their respective application
""")
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write("""
    - Program Python(Scikit-learn, Pandas),SQL,VBA
    - Data Visualization: Power BI, MS Excel, Plotly
    - Modelling: Logistic Regression, Decision Tree
""")
