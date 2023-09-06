import pandas as pd
import plotly.express as ps
import streamlit as st

st.set_page_config(page_title="Youtube Most Subscribed To Channels",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_csv("ytsubs.csv")
st.dataframe(df)