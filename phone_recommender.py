import streamlit as st
import pandas as pd
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')
def main():
    # Create a checkbox
    # Sidebar components for user input
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))

    # Filter the data based on the selected operating system
    #filtered_data = df[df['Operating System'] == operating_system]

    # Display the filtered data
    #st.write("Filtered Data:")
    #st.dataframe(filtered_data)
    # Display a message based on the checkbox state
    if operating_system:
        st.write("Checkbox is checked!")
    else:
        st.write("Checkbox is unchecked!")

if __name__ == '__main__':
    main()
