import streamlit as st

# st.title("Modern Building Leaders")


about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    default=True,
    icon="🧓",
)
project1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon="🧓",
)
project2_page = st.Page(page="views/chatbot.py", title="Chat Bot", icon="🧓")

# ----------------NAVIGATION SETUP [WITH SECTIONS]-------------------
pg = st.navigation({"Info": [about_page], "Projects": [project1_page, project2_page]})

# ---------SHARED ON ALL PAGES---------
st.sidebar.text("Made with ❤️ by Farhan Shaikh")

# -------RUN THE NAVIGATION----------
pg.run()
