import streamlit as st
import pandas as pd

df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

def main():
    # Sidebar components for user input
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))
    storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=int(df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float).max()), step=1)

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
            col1, col2, col3, col4 = st.beta_columns(4)
            col5, col6, col7 = st.beta_columns(3)

            with col1:
                is_glass = st.checkbox('Glass')
            with col2:
                is_stainless_steel = st.checkbox('Stainless Steel')
            with col3:
                is_metal = st.checkbox('Metal')
            with col4:
                is_aluminium = st.checkbox('Aluminium')
            with col5:
                is_polycarbonate = st.checkbox('Polycarbonate')
            with col6:
                is_plastic = st.checkbox('Plastic')
            with col7:
                is_gorilla_glass = st.checkbox('Gorilla Glass')

    st.subheader('Security & Privacy')
    with st.beta_expander('Security & Privacy Options'):
        with st.beta_container():
            col1, col2, col3 = st.beta_columns(3)
            with col1:
                is_face_id = st.checkbox('Face ID or Facial Recognition')
            with col2:
                is_rear_mounted = st.checkbox('Rear-Mounted')
            with col3:
                is_in_display = st.checkbox('In-Display')

    # Filter the data based on the selected criteria
    filtered_data = df[
        (df['Operating System'] == operating_system) &
        (df['Storage Capacity'].str.split('/').str[1].str.rstrip('GB').astype(float) >= storage_space) &
        ((df['5G'] == is_5g) | (df['4G'] == is_4g) | (df['WiFi'] == is_wifi) | (df['NFC'] == is_nfc)) &
        ((df['Glass'] == is_glass) | (df['Stainless Steel'] == is_stainless_steel) | (df['Metal'] == is_metal) |
         (df['Aluminium'] == is_aluminium) | (df['Polycarbonate'] == is_polycarbonate) | (df['Plastic'] == is_plastic) |
         (df['Gorilla Glass'] == is_gorilla_glass)) &
        ((df['Face ID'] == is_face_id) | (df['Rear-Mounted'] == is_rear_mounted) | (df['In-Display'] == is_in_display))
    ]

    # Display the filtered data
    if not filtered_data.empty:
        st.write("Phone Models that meet the criteria:")
        st.dataframe(filtered_data)
    else:
        st.write("No Phone Models meet the criteria.")

if __name__ == '__main__':
    main()
