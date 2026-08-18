import streamlit as st
import pandas as pd

st.title("Transactions")

df=pd.DataFrame({
"Transaction":["T001","T002","T003"],
"Amount":[2500,8200,1500]
})

st.table(df)
