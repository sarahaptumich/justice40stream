import streamlit as st
import time
from datetime import datetime

def main():
    st.title("Coffee Brewing Log")

    # Bean Name
    bean_name = st.text_input("Bean Name")

    # Grams
    grams = st.number_input("Grams", min_value=0)

    # Grind
    grind = st.number_input("Grind", min_value=0)

    # Start Pour
    start_pour_button = st.button("Start Pour")
    start_time = None
    if start_pour_button:
        start_time = time.time()
        st.write("Pouring...")

    # End Pour
    end_pour_button = st.button("End Pour")
    end_time = None
    if end_pour_button:
        end_time = time.time()
        st.write("Pouring finished.")

    # Date
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Submit Button
    if st.button("Submit"):
        st.success(f"Bean Name: {bean_name}, Grams: {grams}, Grind: {grind}, Start Pour Time: {start_time}, End Pour Time: {end_time}, Date: {date}")

if __name__ == "__main__":
    main()
