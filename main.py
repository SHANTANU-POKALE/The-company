import streamlit as st
import pandas
st.set_page_config(layout="wide")

st.header("The Best Company")
content = """
Business structure First, you’ll want to define what type of organization your business is registered as.
The most common business structures in the US include: LLC C-corp ..."""
st.write(content)
st.subheader("Our Team")
# prepare the column
col1, col2, col3 = st.columns(3)
#  make a dataframe with the company member
df = pandas.read_csv("data.csv")
# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last name
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])
# Add content to second column
with col2:
    # Iterate over only the 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last name
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])
# Add content to third column
with col3:
    # Iterate over only the 8 to 11
    for index, row in df[8:].iterrows():
        # Add member's first and last name
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

