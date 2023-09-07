import pandas as pd
import plotly.express as ps
import streamlit as st
import re


# ----- Setting up the page -----
st.set_page_config(page_title="Youtube Most Subscribed To Channels",
                   page_icon=":bar_chart:",
                   layout="wide")


df = pd.read_csv("ytsubs.csv")

# Remove the last row
df = df.iloc[:-1]

# Remove the first column (Unnamed)
df = df.iloc[:, 1:]

st.dataframe(df)


# ----- Sidebar -----
st.sidebar.header("Add Filter:")
country = st.sidebar.multiselect("Select the Country:", 
                                 options=df['Country'].unique(), 
                                 default=df['Country'].unique()
                                 )

def extract_language_name(text):
    # Use a regular expression to match and extract the language name
    match = re.search(r'^([^\[]+)', text)
    if match:
        return match.group(1).strip()  # Extract and strip any leading/trailing whitespace
    else:
        return text
    
df['Primary language'] = df['Primary language'].apply(extract_language_name)


language = st.sidebar.multiselect("Select the Language:", 
                                 options=df['Primary language'].unique(), 
                                 default=df['Primary language'].unique()
                                 )

category = st.sidebar.multiselect("Select the Category:", 
                                 options=df['Category'].unique(), 
                                 default=df['Category'].unique()
                                 )

query_string = "Country in @country and `Primary language` in @language and Category in @category"

df_selection = df.query(query_string)



# ----- MAINPAGE -----
st.title("🥇 Ranking Dashboard")
st.markdown("##")

df_selection["Subscribers (millions)"] = df_selection["Subscribers (millions)"].astype(float)


#Top KPI
total_subs = float(df_selection["Subscribers (millions)"].sum()) #counting the subs all together then turning them to int
average_subs_by_ranking = round(df_selection["Subscribers (millions)"].mean(), 2)

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total Subscribers:")
    st.subheader(f"{total_subs} Millions")
with right_column:
    st.subheader("Average Subscribers Per Ranking:")
    st.subheader(f"{average_subs_by_ranking}")

st.markdown("---")