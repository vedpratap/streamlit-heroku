import streamlit as st
import pandas as pd

st.write("# Addition of two given numbers")

st.header('User Input Parameters')

def user_input_features():
    first_number = st.number_input("first_number")
    second_number = st.number_input("second_number")
    data = {'first_number': int(first_number),'second_number': int(second_number)}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Result')
sum = df['first_number']+df['second_number']
st.write("The sum of given 2 numbers is", sum[0])
