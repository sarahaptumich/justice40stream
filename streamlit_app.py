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

    # Pour Button
    pour_button_label = "Start Pour"
    pour_button_state = st.button(pour_button_label)

    start_time = None
    end_time = None

    if pour_button_state:
        if pour_button_label == "Start Pour":
            start_time = time.time()
            pour_button_label = "End Pour"
        elif pour_button_label == "End Pour":
            end_time = time.time()
            pour_button_label = "Start Pour"

    # Date
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Submit Button
    if st.button("Submit"):
        st.success(f"Bean Name: {bean_name}, Grams: {grams}, Grind: {grind}, Start Pour Time: {start_time}, End Pour Time: {end_time}, Date: {date}")

if __name__ == "__main__":
    main()