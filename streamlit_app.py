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

    # Time variables
    start_time = None
    end_time = None

    # Check if brewing is in progress
    is_brewing = st.session_state.get("is_brewing", False)

    # Toggle button label based on brewing status
    if is_brewing:
        pour_button_label = "End Pour"
    else:
        pour_button_label = "Start Pour"

    # Pour Button
    if st.button(pour_button_label):
        if not is_brewing:
            start_time = time.time()
            st.session_state.is_brewing = True
        else:
            end_time = time.time()
            st.session_state.is_brewing = False

    # Date
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Submit Button
    if st.button("Submit"):
        st.success(f"Bean Name: {bean_name}, Grams: {grams}, Grind: {grind}, Start Pour Time: {start_time}, End Pour Time: {end_time}, Date: {date}")

if __name__ == "__main__":
    main()