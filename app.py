import streamlit as st
import pandas as pd

st.write("# Addition of two given numbers")

st.header('User Input Parameters')
def user_input_features():
 first_number = st.number_input("first_number")
 second_number = st.number_input("second_number")
 return (first_number + second_number)
 
df = user_input_features()
st.subheader('Result')
#sum = first_number+second_number
st.write("The sum of given 2 numbers is", df)
