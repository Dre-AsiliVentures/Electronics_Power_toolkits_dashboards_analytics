import streamlit as st
import pandas as pd

# Load the laptop specifications table
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/06/Laptop-Specifications.xlsx')

def convert_storage_capacity(value):
    if value.endswith('GB'):
        return int(value.split('GB')[0])
    elif value.endswith('TB'):
        return int(value.split('TB')[0]) * 1024
    else:
        return 0

def main():
    intel_core_version = st.selectbox('Select Intel Core Version', list(df['Intel Core Version'].unique()))
    with st.expander('Capacity & Storage'):
        internal_storage = st.slider('Internal Storage (in GB)', min_value=32, max_value=2048, value=512)
        hdd_or_ssd = st.selectbox('HDD or SSD or eMMC', list(df['HDD/SSD Classification'].unique()))
        ram = st.slider('RAM (in GB)', min_value=4, max_value=64, value=8)
    # Create a checkbox for Backlight Keyboard
    if st.checkbox('Backlight Keyboard'):
        df = df[df['Backlight Keyboard Availability'] == 'Yes']
    if st.checkbox('Touchscreen Compatibility'):
        df = df[df['Touchscreen Compatibility'] == 'Yes']
    generation_version = st.selectbox('Select Generation Version', list(df['Generation Version'].unique()))
    with st.expander('Display Features'):
        display_type = st.selectbox('Display Type', list(df['Display Type'].unique()))
        display_quality = st.selectbox('Display Quality', list(df['Display Quality'].unique()))
    if st.checkbox('Sim Card Slot Availability'):
        df = df[df['Sim Card Slot Availability'] == 'Yes']
    if st.checkbox('Fingerprint/Face ID Availability'):
        df = df[df['Fingerprint/Face ID Availability'] == 'Yes']
    if st.checkbox('Bluetooth Availability'):
        df = df[df['Bluetooth Availability'] == 'Yes']
    no_of_usb = st.selectbox('No. of USB Ports', list(df['No. of USB Ports'].unique()))
    if st.checkbox('Filter by Weight'):
        weight_unit = st.radio("Select weight unit:", ('Pounds', 'Kgs'))
        if weight_unit == 'Pounds':
            weight = st.selectbox('Laptop Weight in Pounds', list(df['Weight in Pounds'].unique()))
            df = df[df['Weight in Pounds'] == weight]
        else:
            weight = st.selectbox('Laptop Weight in Kgs', list(df['Weight in Kgs'].unique()))
            df = df[df['Weight in Kgs'] == weight]
    price = st.slider('Price', min_value=500, max_value=5000, value=300)

    if st.button('Recommend Laptops'):
        recommended_df = df[(df['Intel Core Version'] == intel_core_version) &
                            (df['RAM Storage Capacity'].apply(convert_storage_capacity) >= ram) &
                            (df['Internal Storage Capacity'].apply(convert_storage_capacity) >= internal_storage) &
                            (df['Price'] <= price)]
        st.table(recommended_df[['Laptop Model Name']])

if __name__ == "__main__":
    main()
