import streamlit as st
import pandas as pd

# Load the laptop specifications table
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/06/Laptop-Specifications.xlsx')

# Load the laptop specifications table
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/06/Laptop-Specifications.xlsx')

# Create a sidebar
st.sidebar.markdown('**Laptop Recommendations**')

# Create a slider for the Intel Core version
intel_core_version = st.sidebar.slider('Intel Core Version', min_value=1, max_value=12, value=1)

# Create a checkbox for fingerprint/face ID
fingerprint_face_id = st.sidebar.checkbox('Fingerprint/Face ID')

# Create a slider for the RAM
ram = st.sidebar.slider('RAM', min_value=4, max_value=64, value=8)

# Create a slider for the internal storage
internal_storage = st.sidebar.slider('Internal Storage', min_value=32, max_value=2048, value=512)

# Convert the internal storage slider value to GB
internal_storage_gb = int(internal_storage.split('GB')[0])

# Create a slider for the price
price = st.sidebar.slider('Price', min_value=500, max_value=5000, value=1000)

# Create a main area
st.markdown('**Laptop Recommendations**')

# If the user has entered any requirements, filter the table and display the results
if intel_core_version != 1 or fingerprint_face_id or ram != 8 or internal_storage_gb != 512 or price != 1000:
    filtered_df = df[(df['Intel Core Version'] == intel_core_version) & (df['Fingerprint/Face ID'].isin(['Yes'])) & (df['RAM'] >= int(ram.split('GB')[0])) & (df['Internal Storage Capacity'] >= int(internal_storage_gb.split('GB')[0])) & (df['Price'] <= price)]
    st.table(filtered_df)

# Otherwise, display all the laptops in the table
else:
    st.table(df)





