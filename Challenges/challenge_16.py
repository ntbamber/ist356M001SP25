import streamlit as st

# Initialize session state variables
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'history' not in st.session_state:
    st.session_state.history = []

# Input amount
amount = st.number_input("Enter an amount:", min_value=0.0, step=0.01)

# Create columns for horizontal buttons
col1, col2 = st.columns(2)

# Add to total button
with col1:
    if st.button("Add to Total"):
        st.session_state.total += amount
        st.session_state.history.append(amount)

# Clear button
with col2:
    if st.button("Clear"):
        st.session_state.total = 0
        st.session_state.history = []
        st.rerun()

# Display total and history
st.write(f"Total: {st.session_state.total}")
st.write("History of amounts entered:")
st.write(st.session_state.history)