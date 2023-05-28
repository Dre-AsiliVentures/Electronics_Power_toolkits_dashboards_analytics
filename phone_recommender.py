import streamlit as st
import pandas as pd

df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

def main():
    # Sidebar components for user input
    st.subheader('Operating System')
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))
    st.subheader('Storage')
    show_storage = st.checkbox('Filter by Storage Space')
    storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=int(df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float).max()), step=1) if show_storage else None

    st.subheader('Connectivity')
    with st.beta_expander('Connectivity Options'):
        with st.beta_container():
            col1, col2, col3, col4 = st.beta_columns(4)
            with col1:
                is_5g = st.checkbox('5G')
            with col2:
                is_4g = st.checkbox('4G')
            with col3:
                is_wifi = st.checkbox('Wi-Fi')
            with col4:
                is_nfc = st.checkbox('NFC')

    st.subheader('Design & Build Quality')
    with st.beta_expander('Design & Build Quality Options'):
        with st.beta_container():
            col1, col2, col3, col4, col5 = st.beta_columns(5)

            with col1:
                is_glass = st.checkbox('Glass')
            with col2:
                is_stainless_steel = st.checkbox('Stainless Steel')
            with col3:
                is_aluminium = st.checkbox('Aluminium')
            with col4:
                is_ceramic = st.checkbox('Ceramic')
            with col5:
                is_polycarbonate = st.checkbox('Polycarbonate')

    st.subheader('Security & Privacy')
    with st.beta_expander('Security & Privacy Options'):
        with st.beta_container():
            col1, col2, col3, col4 = st.beta_columns(4)
            with col1:
                is_face_id = st.checkbox('Face ID or Facial Recognition')
            with col2:
                is_in_display = st.checkbox('In-Display Fingerprint')
            with col3:
                is_side_mounted = st.checkbox('Side-Mounted Fingerprint')
            with col4:
                is_rear_mounted = st.checkbox('Rear-Mounted Fingerprint')

    # Filter the data based on the selected criteria
    filtered_data = df[
        (df['Operating System'] == operating_system) &
        ((df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float) >= storage_space) if show_storage else True) &
        ((df['Connectivity'].str.contains('5G')) == is_5g) |
        ((df['Connectivity'].str.contains('4G')) == is_4g) |
        ((df['Connectivity'].str.contains('Wi-Fi')) == is_wifi) |
        ((df['Connectivity'].str.contains('NFC')) == is_nfc) |
        ((df['Design and Build Quality'].str.contains('Glass')) == is_glass) |
        ((df['Design and Build Quality'].str.contains('Stainless Steel')) == is_stainless_steel) |
        ((df['Design and Build Quality'].str.contains('Aluminium')) == is_aluminium) |
        ((df['Design and Build Quality'].str.contains('Ceramic')) == is_ceramic) |
        ((df['Design and Build Quality'].str.contains('Polycarbonate')) == is_polycarbonate) |
        ((df['Security & Privacy'].str.contains('Face ID')) == is_face_id) |
        ((df['Security & Privacy'].str.contains('In-Display Fingerprint')) == is_in_display) |
        ((df['Security & Privacy'].str.contains('Side-Mounted Fingerprint')) == is_side_mounted) |
        ((df['Security & Privacy'].str.contains('Rear-Mounted Fingerprint')) == is_rear_mounted)
    ]

    # Display the filtered data
    if st.button('Filter'):
        if not filtered_data.empty:
            st.write("Phone Models that meet the criteria:")
            st.dataframe(filtered_data['Phone Model'])
        else:
            st.write("No Phone Models meet the criteria.")

    if st.button('Reset'):
        st.session_state.clear()  # Clear all session state variables
        st.experimental_rerun()  # Rerun the app

if __name__ == '__main__':
    main()
