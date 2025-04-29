import streamlit as st

st.title("How old will I be?")

birth_year = st.number_input("What year were you born?")

pick_year = st.number_input("Pick a year!")

if st.button("Tell me my age!"):
    age = pick_year - birth_year
    st.write(f"In {pick_year}, you will be {age} years old!")
