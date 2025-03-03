import streamlit as st
import requests
import pandas as pd
from pandas import json_normalize

# URL of the JSON data
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Normalize the JSON data
df = json_normalize(data, 'employees', ['dept'])

# Select the required columns
df = df[['dept', 'age', 'firstName', 'lastName']]

# Display the dataframe in Streamlit
st.title("Employee Data")
st.write(df)