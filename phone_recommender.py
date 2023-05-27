import re
import pandas as pd
import streamlit as st

# Load the phone specifications data from the Excel file
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

# Sidebar components for user input
operating_system = st.selectbox('Select Operating System', df['Operating System'].unique())
storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=int(df['Storage'].str.rstrip('GB').max()), step=1)

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
        col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
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

st.subheader('Additional Features')
with st.beta_expander('Additional Features Options'):
    with st.beta_container():
        amoled_oled_display = st.slider('AMOLED & OLED Display', min_value=0, max_value=1, step=1)
        stylus_pen_support = st.checkbox('Stylus Pen Support')
        magsafe_compatibility = st.checkbox('MagSafe Compatibility')
        ip_rating = st.slider('IP Rating (IP67 & IP68)', min_value=0, max_value=1, step=1)
        pop_up_camera = st.checkbox('Pop-up Camera')
        vr_support = st.checkbox('VR Support')
        optical_image_stabilization = st.checkbox('Optical Image Stabilization')
        usb_type_c = st.slider('USB Type (Type C)', min_value=0, max_value=1, step=1)
        price_range = st.slider('Select Price Range', min_value=0, max_value=int(df['Price'].str.replace('$', '').str.replace(',', '')).max(), step=100)

# Filter the data based on user input
filtered_df = df[
    (df['Operating System'] == operating_system) &
    (df['Storage'].str.rstrip('GB').astype(int) >= storage_space) &
    (df['5G'] == is_5g) &
    (df['4G'] == is_4g) &
    (df['Wi-Fi'] == is_wifi) &
    (df['NFC'] == is_nfc) &
    (df['Glass'] == is_glass) &
    (df['Stainless Steel'] == is_stainless_steel) &
    (df['Metal'] == is_metal) &
    (df['Aluminium'] == is_aluminium) &
    (df['Polycarbonate'] == is_polycarbonate) &
    (df['Plastic'] == is_plastic) &
    (df['Gorilla Glass'] == is_gorilla_glass) &
    (df['Face ID or Facial Recognition'] == is_face_id) &
    (df['Rear-Mounted'] == is_rear_mounted) &
    (df['In-Display'] == is_in_display) &
    (df['AMOLED & OLED Display'] >= amoled_oled_display) &
    (df['Stylus Pen Support'] == stylus_pen_support) &
    (df['MagSafe Compatibility'] == magsafe_compatibility) &
    (df['IP Rating (IP67 & IP68)'] >= ip_rating) &
    (df['Pop-up Camera'] == pop_up_camera) &
    (df['VR Support'] == vr_support) &
    (df['Optical Image Stabilization'] == optical_image_stabilization) &
    (df['USB Type (Type C)'] >= usb_type_c) &
    (df['Price'].str.replace('$', '').str.replace(',', '').astype(int) <= price_range)
]

# Display the filtered results
st.subheader('Filtered Results')
if filtered_df.empty:
    st.write('No matching phones found.')
else:
    st.dataframe(filtered_df)
