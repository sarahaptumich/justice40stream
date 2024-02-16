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
    
    bean_name_input = st.text_input('Bean Name', key='ticker')
    grams_input = st.text_input('Grams', key='note')
    grind_input = st.text_input('Grind', key='note2')
    start_pour_input = st.text_input('Start Pour', key='note3')
    end_pour_input = st.text_input('End Pour', key='note4')
    date_input = st.text_input('Date', key='note5')
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Bean Name", bean_name_input,
         "Grams", grams_input,
         "Grind", grind_input,
         "Start Pour", start_pour_input,
         "End Pour", end_pour_input,
         "Date", date_input)
        form_callback(bean_name_input, grams_input, grind_input, start_pour_input, end_pour_input, date_input)

st.info(" #### Show contents of the CSV file :point_down:")
st.dataframe(pd.read_csv("espresso.csv"),height=300)
