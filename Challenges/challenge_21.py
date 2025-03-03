import streamlit as st
import pandas as pd
import json

def main():
    st.title("Excel to JSON Converter")

    # File uploader
    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

    if uploaded_file is not None:
        # Read the Excel file
        df = pd.read_excel(uploaded_file, sheet_name=0)

        # Display the DataFrame
        st.write("DataFrame:")
        st.dataframe(df)

        # Convert DataFrame to JSON
        json_data = df.to_json(orient='records')

        # Display JSON data
        st.write("JSON Data:")
        st.json(json.loads(json_data))

        # Provide download button for JSON file
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name="data.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()