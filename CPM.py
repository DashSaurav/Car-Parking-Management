import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

@st.cache_data
def car_data(url):
    data = conn.read(spreadsheet=url, ttl=36000)
    return data

url = "https://docs.google.com/spreadsheets/d/1VYrpcJnaw7kPEtUQxxN-_UR2okw8RmtD5YgygWifJmg/edit?usp=sharing"

# data = conn.read(spreadsheet=url)

st.dataframe(car_data(url))
