import streamlit as st

st.title(" Loan Management")

with st.form("loan_form"):
    name=st.text_input("Customer Name")
    amount=st.number_input("Loan Amount",10000)

    submit=st.form_submit_button("Apply")

    if submit:
        st.success(f"Loan application submitted for {name}.")
