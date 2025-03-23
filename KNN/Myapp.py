import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("./knn_dataset.csv")

st.line_chart(df.select_dtypes(include=['number']))
