import streamlit as st
import pandas as pd

df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

def main():
    # Sidebar components for user input
    criteria = []
    
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))
    criteria.append(df['Operating System'] == operating_system)
    
    show_storage = st.checkbox('Filter by Storage Space')
    if show_storage:
        storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=int(df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float).max()), step=1)
        criteria.append(df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float) >= storage_space)

    st.subheader('Connectivity')
    with st.beta_expander('Connectivity Options'):
        with st.beta_container():
            is_5g = st.checkbox('5G')
            if is_5g:
                criteria.append(df['Connectivity'].str.contains('5G'))

            is_4g = st.checkbox('4G')
            if is_4g:
                criteria.append(df['Connectivity'].str.contains('4G'))

            is_wifi = st.checkbox('Wi-Fi')
            if is_wifi:
                criteria.append(df['Connectivity'].str.contains('Wi-Fi'))

            is_nfc = st.checkbox('NFC')
            if is_nfc:
                criteria.append(df['Connectivity'].str.contains('NFC'))

    st.subheader('Design & Build Quality')
    with st.beta_expander('Design & Build Quality Options'):
        with st.beta_container():
            is_glass = st.checkbox('Glass')
            if is_glass:
                criteria.append(df['Design and Build Quality'].str.contains('Glass'))

            is_stainless_steel = st.checkbox('Stainless Steel')
            if is_stainless_steel:
                criteria.append(df['Design and Build Quality'].str.contains('Stainless Steel'))

            is_aluminium = st.checkbox('Aluminium')
            if is_aluminium:
                criteria.append(df['Design and Build Quality'].str.contains('Aluminium'))

            is_ceramic = st.checkbox('Ceramic')
            if is_ceramic:
                criteria.append(df['Design and Build Quality'].str.contains('Ceramic'))

            is_polycarbonate = st.checkbox('Polycarbonate')
            if is_polycarbonate:
                criteria.append(df['Design and Build Quality'].str.contains('Polycarbonate'))

    st.subheader('Security & Privacy')
    with st.beta_expander('Security & Privacy Options'):
        with st.beta_container():
            is_face_id = st.checkbox('Face ID or Facial Recognition')
            if is_face_id:
                criteria.append(df['Security & Privacy'].str.contains('Face ID'))

            is_in_display = st.checkbox('In-Display Fingerprint')
            if is_in_display:
                criteria.append(df['Security & Privacy'].str.contains('In-Display Fingerprint'))

            is_side_mounted = st.checkbox('Side-Mounted Fingerprint')
            if is_side_mounted:
                criteria.append(df['Security & Privacy'].str.contains('Side-Mounted Fingerprint'))

            is_rear_mounted = st.checkbox('Rear-Mounted Fingerprint')
            if is_rear_mounted:
                criteria.append(df['Security & Privacy'].str.contains('Rear-Mounted Fingerprint'))

    # Filter the data based on the selected criteria
    filtered_data = df
    for criterion in criteria:
        filtered_data = filtered_data[criterion]

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
