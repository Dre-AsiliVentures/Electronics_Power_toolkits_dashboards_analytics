import streamlit as st
import pandas as pd

# Load the laptop specifications table
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/06/Laptop-Specifications.xlsx')

# Create a sidebar
st.sidebar.markdown('**Laptop Recommendations**')

# Create a slider for the Intel Core version
intel_core_version = st.sidebar.slider('Intel Core Version', min_value=1, max_value=12, value=1)

# Create a checkbox for touchscreen compatibility
touchscreen = st.sidebar.checkbox('Touchscreen')

# Create a dropdown menu for the display type
display_type = st.sidebar.selectbox('Display Type',
    options=['IPS', 'OLED', 'QHD', '4K'],
    default='IPS')

# Create a slider for the display resolution
display_resolution = st.sidebar.slider('Display Resolution', min_value=1080, max_value=4096, value=1920)

# Create a checkbox for fingerprint/face ID availability
fingerprint_face_id = st.sidebar.checkbox('Fingerprint/Face ID')

# Create a slider for the RAM
ram = st.sidebar.slider('RAM', min_value=4, max_value=64, value=8)

# Create a slider for the internal storage
internal_storage = st.sidebar.slider('Internal Storage', min_value=32, max_value=1024, value=512)

# Create a slider for the price
price = st.sidebar.slider('Price', min_value=500, max_value=5000, value=1000)

# Create a main area
st.markdown('**Laptop Recommendations**')

# If the user has entered any requirements, filter the table and display the results
if intel_core_version != 1 or touchscreen or display_type != 'IPS' or display_resolution != 1920 or fingerprint_face_id or ram != 8 or internal_storage != 512 or price != 1000:
    filtered_df = df[(df['Intel Core Version'] == intel_core_version) & (df['Touchscreen'] == touchscreen) & (df['Display Type'] == display_type) & (df['Display Resolution'] == display_resolution) & (df['Fingerprint/Face ID'] == fingerprint_face_id) & (df['RAM'] >= ram) & (df['Internal Storage'] >= internal_storage) & (df['Price'] <= price)]
    st.table(filtered_df)

# Otherwise, display all the laptops in the table
else:
    st.table(df)
