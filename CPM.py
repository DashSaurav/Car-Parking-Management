import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1VYrpcJnaw7kPEtUQxxN-_UR2okw8RmtD5YgygWifJmg/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, ttl=3600)

st.dataframe(data)
