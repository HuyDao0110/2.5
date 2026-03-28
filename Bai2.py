import streamlit as st
import pandas as pd

data=pd.raed_csv("Bai2.csv")
#st.write(data)
#st.table(data)
st.dataframe(data, width=None, height=None)