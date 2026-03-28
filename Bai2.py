import streamlit as st
import pandas as pd

data = pd.read_csv("data_lesson2_none_header.csv")
df = pd.DataFrame(data, index=["Thời gian", "Nội dung", "Địa điểm", "Cảm xúc"])
st.write(data)
st.table(data)
st.dataframe(data, width=None, height=None)
