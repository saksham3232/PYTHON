import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter Your Name:")


if name:
    st.write(f"Hello, {name}")

age = st.slider("Select Your Age:",0,100,25)

st.write(f"Your age is {age}.")

options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox("Choose Your Favourite Language:",options)
st.write(f"You Selecte {choice}")


data = {
    'Name' : ['John', 'Jane', 'Jake', 'Jill'],
    'Age' : [28, 24, 35, 40],
    'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV File",type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)