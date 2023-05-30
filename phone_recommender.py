import streamlit as st
import pandas as pd

df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

def main():
    # Sidebar components for user input
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))

    # Filtered data
    filtered_data = df[df['Operating System'] == operating_system]

    # Apply additional filters based on user selections
    with st.beta_expander('Storage'):
        if st.checkbox('Filter by Storage Space'):
            storage_space = st.slider('Select Internal Storage Space (GB)', min_value=0, max_value=int(df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float).max()), step=1)
            filtered_data = filtered_data[filtered_data['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float) >= storage_space]

    with st.beta_expander('Connectivity'):
        connectivity_filters = []
        if st.checkbox('5G'):
            connectivity_filters.append('5G')
        if st.checkbox('4G'):
            connectivity_filters.append('4G')
        if st.checkbox('Wi-Fi'):
            connectivity_filters.append('Wi-Fi')
        if st.checkbox('NFC'):
            connectivity_filters.append('NFC')
        filtered_data = filtered_data[filtered_data['Connectivity'].str.contains('|'.join(connectivity_filters))]

    with st.beta_expander('Design & Build Quality'):
        design_filters = []
        if st.checkbox('Glass'):
            design_filters.append('Glass')
        if st.checkbox('Stainless Steel'):
            design_filters.append('Stainless Steel')
        if st.checkbox('Aluminium'):
            design_filters.append('Aluminium')
        if st.checkbox('Ceramic'):
            design_filters.append('Ceramic')
        if st.checkbox('Polycarbonate'):
            design_filters.append('Polycarbonate')
        filtered_data = filtered_data[filtered_data['Design and Build Quality'].str.contains('|'.join(design_filters))]

    with st.beta_expander('Security & Privacy'):
        security_filters = []
        if st.checkbox('Face ID or Facial Recognition'):
            security_filters.append('Face ID')
        if st.checkbox('In-Display Fingerprint'):
            security_filters.append('In-display Fingerprint')
        if st.checkbox('Side-Mounted Fingerprint'):
            security_filters.append('Side-mounted Fingerprint')
        if st.checkbox('Rear-Mounted Fingerprint'):
            security_filters.append('Rear-mounted Fingerprint')
        filtered_data = filtered_data[filtered_data['Security & Privacy'].str.contains('|'.join(security_filters))]

    with st.beta_expander('Camera'):
        front_camera = st.slider('Front Camera (MP)', min_value=0, max_value=int(df['Front Camera'].str.replace('\D', '', regex=True).str.strip().astype(float).dropna().max()), step=1)
        rear_camera = st.slider('Rear Camera (MP)', min_value=0, max_value=int(df['Front Camera'].str.replace('\D', '', regex=True).str.strip().astype(float).dropna().max()), step=1)
        ultrawide_camera = st.slider('Ultrawide Camera (MP)', min_value=0, max_value=int(df['Front Camera'].str.replace('\D', '', regex=True).str.strip().astype(float).dropna().max()), step=1)

        filtered_data = filtered_data[
            filtered_data['Front Camera'].str.replace('\D', '').astype(float) >= front_camera &
            filtered_data['Rear Camera'].str.replace('\D', '').astype(float) >= rear_camera &
            filtered_data['Ultrawide Camera'].str.replace('\D', '').astype(float) >= ultrawide_camera
        ]

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
