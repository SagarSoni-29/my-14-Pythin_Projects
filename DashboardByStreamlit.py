import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("This is Streamlit app of SAGAR")
st.title("Welcome to our Technical Round Selection :")
st.header("Here we can compare our candidates:")
st.write("Enter your dtail", 10 + 34)

name = st.text_input("Enter your name :")
age = st.number_input("Enter the Age ")

st.write("Your name is:", name)

st.selectbox("Enter your District: ", ["KOTA", "JAIPUR", "BHILWARA"])

if st.button("Click ME"):
    st.success("Clicked Button")

file = st.file_uploader("Upload file of student result")
if file:
    content = file.read()
    st.write("File uploaded successfully")

data = {"NAME": ["Noor", "Anurag", "Ashok", "Sagar"], "Marks": [10, 20, 30, 40]}
df = pd.DataFrame(data)
st.dataframe(df)

chart_data = pd.DataFrame({"Marks": [10, 20, 30, 40]})
st.line_chart(chart_data)
st.bar_chart(chart_data)


