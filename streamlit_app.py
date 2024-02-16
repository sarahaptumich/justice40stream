# app.py
import streamlit as st
import time
import csv

def main():
    st.title("Espresso Brew Timer")

    if "entries" not in st.session_state:
        st.session_state.entries = []

    if st.button("New Entry"):
        start_time = time.time()
        entry = {"start_time": start_time, "pour_start_time": None, "end_time": None, "bean_type": "", "grams": 0, "grind_size": ""}
        st.session_state.entries.append(entry)
        st.write("New entry started.")

    for i, entry in enumerate(st.session_state.entries):
        st.write(f"Entry {i+1}:")
        if not entry["pour_start_time"]:
            if st.button(f"Start Pour {i+1}"):
                entry["pour_start_time"] = time.time()
                st.write("Pour started.")
        elif not entry["end_time"]:
            if st.button(f"End Brew {i+1}"):
                entry["end_time"] = time.time()
                st.write("Brew ended.")
                st.write(f"Total brew time for Entry {i+1}: {entry['end_time'] - entry['start_time']} seconds")
                entry["bean_type"] = st.text_input("Bean Type", value=entry["bean_type"])
                entry["grams"] = st.number_input("Grams", value=entry["grams"])
                entry["grind_size"] = st.text_input("Grind Size", value=entry["grind_size"])

    if st.button("Save"):
        save_entries(st.session_state.entries)
        st.write("Entries saved successfully.")

def save_entries(entries):
    with open("brew_entries.csv", "w", newline="") as csvfile:
        fieldnames = ["start_time", "pour_start_time", "end_time", "bean_type", "grams", "grind_size"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

if __name__ == "__main__":
    main()
