import streamlit as st
st.title("Rectangle Calculator")
length = st.number_input("Enter the length of the rectangle:", min_value=0.0, format="%.2f")
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, format="%.2f")
calculate = st.button("Calculate")
clear = st.button("Clear")
if calculate:
    perimeter = 2 * (length + width)
    area = length * width
    st.write(f"The perimeter of the rectangle is: {perimeter}")
    st.write(f"The area of the rectangle is: {area}")
if clear:
    st.rerun()