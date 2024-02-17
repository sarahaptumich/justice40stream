# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

# Create a connection object.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Sheet1")

st.dataframe(df)
