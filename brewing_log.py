import streamlit as st
import time

def main():
    st.title("Coffee Brewing Log")

    # Button state
    button_state = st.button("Start/End Pour")

    # Initialize variables
    start_time = None
    end_time = None
    lap_num = 1

    # Main loop
    if button_state:
        if st.session_state.get("is_running", False):
            end_time = time.time()
            st.session_state.is_running = False
        else:
            start_time = time.time()
            st.session_state.is_running = True

    # Calculate times
    if start_time is not None:
        total_time = time.time() - start_time
    else:
        total_time = 0

    if end_time is not None:
        lap_time = end_time - start_time
    else:
        lap_time = 0

    # Display lap info
    if start_time is not None:
        st.write(f"Lap Number {lap_num}")
        st.write(f"Total Time taken: {round(total_time, 2)} seconds")
        st.write(f"Lap Time: {round(lap_time, 2)} seconds")

if __name__ == "__main__":
    main()
