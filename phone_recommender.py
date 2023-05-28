import streamlit as st
import pandas as pd

df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

def main():
    # Sidebar components for user input
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))

    # Filtered data
    filtered_data = df[df['Operating System'] == operating_system]

    # Apply additional filters based on user selections
    if st.checkbox('Filter by Storage Space'):
        storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=int(df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float).max()), step=1)
        filtered_data = filtered_data[filtered_data['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float) >= storage_space]

    with st.beta_expander('Connectivity'):
        if st.checkbox('5G'):
            filtered_data = filtered_data[filtered_data['Connectivity'].str.contains('5G')]
        if st.checkbox('4G'):
            filtered_data = filtered_data[filtered_data['Connectivity'].str.contains('4G')]
        if st.checkbox('Wi-Fi'):
            filtered_data = filtered_data[filtered_data['Connectivity'].str.contains('Wi-Fi')]
        if st.checkbox('NFC'):
            filtered_data = filtered_data[filtered_data['Connectivity'].str.contains('NFC')]

    with st.beta_expander('Design & Build Quality'):
        if st.checkbox('Glass'):
            filtered_data = filtered_data[filtered_data['Design and Build Quality'].str.contains('Glass')]
        if st.checkbox('Stainless Steel'):
            filtered_data = filtered_data[filtered_data['Design and Build Quality'].str.contains('Stainless Steel')]
        if st.checkbox('Aluminium'):
            filtered_data = filtered_data[filtered_data['Design and Build Quality'].str.contains('Aluminium')]
        if st.checkbox('Ceramic'):
            filtered_data = filtered_data[filtered_data['Design and Build Quality'].str.contains('Ceramic')]
        if st.checkbox('Polycarbonate'):
            filtered_data = filtered_data[filtered_data['Design and Build Quality'].str.contains('Polycarbonate')]

    with st.beta_expander('Security & Privacy'):
        if st.checkbox('Face ID or Facial Recognition'):
            filtered_data = filtered_data[filtered_data['Security & Privacy'].str.contains('Face ID')]
        if st.checkbox('In-Display Fingerprint'):
            filtered_data = filtered_data[filtered_data['Security & Privacy'].str.contains('In-Display Fingerprint')]
        if st.checkbox('Side-Mounted Fingerprint'):
            filtered_data = filtered_data[filtered_data['Security & Privacy'].str.contains('Side-Mounted Fingerprint')]
        if st.checkbox('Rear-Mounted Fingerprint'):
            filtered_data = filtered_data[filtered_data['Security & Privacy'].str.contains('Rear-Mounted Fingerprint')]

    # Display the filtered data
    if st.button('Filter'):
        if not filtered_data.empty:
            st.write("Phone Models that meet the criteria:")
            st.dataframe(filtered_data['Phone Model'])
        else:
            st.write("No Phone Models meet the criteria.")

    if st.button('Reset'):
        st.experimental_rerun()  # Rerun the app

if __name__ == '__main__':
    main()
