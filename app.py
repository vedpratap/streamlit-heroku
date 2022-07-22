import streamlit as st
import pandas as pd

st.write("# Addition of two given numbers")

st.header('User Input Parameters')

first_number = st.number_input("first_number")
second_number = st.number_input("second_number")
 
st.subheader('Result')
sum = first_number+second_number
st.write("The sum of given 2 numbers is", sum)
