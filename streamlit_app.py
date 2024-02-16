# app.py
import streamlit as st
import time
import csv
import pandas as pd

def form_callback(Bean_Name,Grams, Grind, Start_Pour, End_Pour, Date):    
    with open('espresso.csv', 'a+') as f:    #Append & read mode
        f.write(f"{Bean_Name},{Grams},{Grind},{Start_Pour},{End_Pour},{Date}\n")

with st.form(key="my_form",clear_on_submit=True):
    
    st.write("Enter Brewing Metrics")
    
    stock_ticker_input = st.text_input('Stock', key='ticker')
    note_input = st.text_input('Note', key='note')
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Note", note_input, "stock_ticker", stock_ticker_input)
        form_callback(stock_ticker_input,note_input)

st.info(" #### Show contents of the CSV file :point_down:")
st.dataframe(pd.read_csv("notes.csv",names=["Stock","Note"]),height=300)
