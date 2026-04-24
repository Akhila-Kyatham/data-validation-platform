import streamlit as st
import pandas as pd

st.title("📊 Data Validation Dashboard")

df = pd.read_csv("data/processed.csv")

st.subheader("Processed Data")
st.dataframe(df)

st.subheader("Basic Stats")
st.write(df.describe())

st.subheader("Null Values")
st.write(df.isnull().sum())