import pandas as pd
import streamlit as st

# Load the CSV file into a DataFrame
url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
customers = pd.read_csv(url)

# Create the radio button widget for selecting Head or Tail
head_tail = st.radio("Select:", ('Head', 'Tail'))

# Create the number input widget for entering the number of lines
num_lines = st.number_input("Lines:", min_value=1, value=5)

# Display the head or tail of the DataFrame based on user input
if head_tail == 'Head':
    st.write(customers.head(num_lines))
else:
    st.write(customers.tail(num_lines))