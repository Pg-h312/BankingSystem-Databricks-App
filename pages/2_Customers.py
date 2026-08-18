import streamlit as st
import pandas as pd

st.title("👤 Customers")

df=pd.DataFrame({
"Customer":["Priya","Rahul","Aman","Neha"],
"City":["Lucknow","Kanpur","Delhi","Noida"]
})

st.dataframe(df)
