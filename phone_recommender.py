import re
import pandas as pd
import streamlit as st

# Load the phone specifications data from the Excel file
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')

# Extract the numeric part from the storage string and convert it to an integer
df['Storage'] = df['Storage'].str.extract('(\d+)').astype(int)

# Create sidebar components for user input
operating_system = st.selectbox('Select Operating System', df['Operating System'].unique())
storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=df['Storage'].max(), step=1)
connectivity_5g = st.checkbox('5G')
connectivity_4g = st.checkbox('4G')
connectivity_wifi = st.checkbox('Wi-Fi')
connectivity_nfc = st.checkbox('NFC')
design_glass = st.checkbox('Glass')
design_stainless_steel = st.checkbox('Stainless Steel')
design_metal = st.checkbox('Metal')
design_aluminium = st.checkbox('Aluminium')
design_polycarbonate = st.checkbox('Polycarbonate')
design_plastic = st.checkbox('Plastic')
design_gorilla_glass = st.checkbox('Gorilla Glass')
security_face_id = st.checkbox('Face ID or Facial Recognition')
security_rear_mounted = st.checkbox('Rear-Mounted')
security_in_display = st.checkbox('In-Display')
ip_rating = st.slider('Select IP Rating', min_value=0, max_value=8, step=1)
stylus_pen_support = st.checkbox('Stylus Pen Support')
magsafe_compatibility = st.checkbox('MagSafe Compatibility')
display_amoled_oled = st.slider('Select Display Type (AMOLED & OLED)', min_value=0, max_value=1, step=1)
pop_up_camera = st.checkbox('Pop-up Camera')
vr_support = st.checkbox('VR Support')
optical_image_stabilization = st.checkbox('Optical Image Stabilization')
usb_type_c = st.slider('Select USB Type (Type C)', min_value=0, max_value=1, step=1)
price_range = st.slider('Select Price Range', min_value=0, max_value=int(df['Price'].str.replace('$', '').astype(int).max()), step=100)

# Filter the data based on user input
filtered_df = df[
    (df['Operating System'] == operating_system) &
    (df['Storage'] >= storage_space) &
    (df['Connectivity (5G)'] == connectivity_5g) &
    (df['Connectivity (4G)'] == connectivity_4g) &
    (df['Connectivity (Wi-Fi)'] == connectivity_wifi) &
    (df['Connectivity (NFC)'] == connectivity_nfc) &
    (df['Design & Build Quality (Glass)'] == design_glass) &
    (df['Design & Build Quality (Stainless Steel)'] == design_stainless_steel) &
    (df['Design & Build Quality (Metal)'] == design_metal) &
    (df['Design & Build Quality (Aluminium)'] == design_aluminium) &
    (df['Design & Build Quality (Polycarbonate)'] == design_polycarbonate) &
    (df['Design & Build Quality (Plastic)'] == design_plastic) &
    (df['Design & Build Quality (Gorilla Glass)'] == design_gorilla_glass) &
    (df['Security & Privacy (Face ID or Facial Recognition)'] == security_face_id) &
    (df['Security & Privacy (Rear-Mounted Fingerprint Sensor)'] == security_rear_mounted) &
    (df['Security & Privacy (In-Display Fingerprint Sensor)'] == security_in_display) &
    (df['IP Rating'] >= ip_rating) &
    (df['Stylus Pen Support'] == stylus_pen_support) &
    (df['MagSafe Compatibility'] == magsafe_compatibility) &
    (df['Display Type (AMOLED & OLED)'] == display_amoled_oled) &
    (df['Pop-up Camera'] == pop_up_camera) &
    (df['VR Support'] == vr_support) &
    (df['Optical Image Stabilization'] == optical_image_stabilization) &
    (df['USB Type (Type C)'] == usb_type_c) &
    (df['Price'].str.replace('$', '').astype(int) <= price_range)
]

# Display the filtered results
if filtered_df.empty:
    st.warning('No phones match your criteria.')
else:
    st.dataframe(filtered_df)
