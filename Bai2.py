import streamlit as st
import pandas as pd

data=pd.read_csv("Bai2-1.csv")
#st.write(data)
#st.table(data)
st.dataframe(data, width=None, height=None)
