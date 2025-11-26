import streamlit as st
import pandas as pd

st.title("Snowflake Streamlit Test App")
st.write("This is a simple test app to verify Snowflake Streamlit integration.")

# Create sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "Finance", "IT", "Marketing"],
    "Salary": [70000, 80000, 75000, 72000]
}

df = pd.DataFrame(data)

# Display the table
st.dataframe(df)

# Interactive filter
column_options = df.columns.tolist()
selected_col = st.selectbox("Select a column to filter", column_options)
filter_value = st.text_input(f"Enter value to filter '{selected_col}' column")

if filter_value:
    filtered_df = df[df[selected_col].astype(str).str.contains(filter_value, case=False)]
    st.write(f"Filtered results for {filter_value}:")
    st.dataframe(filtered_df)
