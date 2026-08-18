import streamlit as st

st.title("📊 Banking Dashboard")

col1,col2,col3,col4=st.columns(4)

col1.metric("Customers","1,245")
col2.metric("Accounts","2,186")
col3.metric("Loans","342")
col4.metric("Transactions","15,240")
