import streamlit as st
import pandas as pd
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')
def main():
    # Create a checkbox
    operating_system = st.checkbox("Select Operating System!",list(df['Operating System'].unique()))
    #operating_system = st.checkbox("Select Operating System!",df['Operating System'].unique())

    # Display a message based on the checkbox state
    if operating_system:
        st.write("Checkbox is checked!")
    else:
        st.write("Checkbox is unchecked!")

if __name__ == '__main__':
    main()
