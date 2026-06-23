import streamlit as st


def is_valid_email(email):
    email_pattern = r""


def contact_form():
    with st.form("contact form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("submit")

        if submit_button:
            st.success("Message sucessfully sent")
