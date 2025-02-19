import streamlit as st
from io import StringIO  # required to convert binary to text

st.title("File Upload Example")
st.markdown('''
This example demonstrates how to process an uploaded file.

- The first example can process any file-like (image, video, data for a dataframe, etc)
- The second example shows how to process text explicitly.

''')
text_file_data = st.file_uploader("Upload a text file", type=["txt", "csv", "md"])

if text_file_data:
    st.markdown(f"### {text_file_data.name}")
    binary_contents = text_file_data.getvalue()
    # Convert binary to text
    text_contents = StringIO(binary_contents.decode("utf-8")).read()

    # Extract numbers from the text file
    numbers = [float(num) for num in text_contents.split() if num.replace('.', '', 1).isdigit()]

    # Initialize session state variables
    if 'total' not in st.session_state:
        st.session_state.total = 0
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Add numbers from file to total
    if st.button("Add to Total"):
        st.session_state.total += sum(numbers)
        st.session_state.history.extend(numbers)

    # Clear button
    if st.button("Clear"):
        st.session_state.total = 0
        st.session_state.history = []
        st.rerun()

    # Display total and history
    st.write(f"Total: {st.session_state.total}")
    st.write("History of amounts entered:")
    st.write(st.session_state.history)