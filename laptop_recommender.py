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
        df_filtered = df[df['Backlight Keyboard Availability'] == 'Yes']
    else:
        df_filtered = df
    if st.checkbox('Touchscreen Compatibility'):
        df_filtered = df_filtered[df_filtered['Touchscreen Compatibility'] == 'Yes']
    generation_version = st.selectbox('Select Generation Version', list(df_filtered['Generation Version'].unique()))
    with st.expander('Display Features'):
        display_type = st.selectbox('Display Type', list(df_filtered['Display Type'].unique()))
        display_quality = st.selectbox('Display Quality', list(df_filtered['Display Quality'].unique()))
    if st.checkbox('Sim Card Slot Availability'):
        df_filtered = df_filtered[df_filtered['Sim Card Slot Availability'] == 'Yes']
    if st.checkbox('Fingerprint/Face ID Availability'):
        df_filtered = df_filtered[df_filtered['Fingerprint/Face ID Availability'] == 'Yes']
    if st.checkbox('Bluetooth Availability'):
        df_filtered = df_filtered[df_filtered['Bluetooth Availability'] == 'Yes']
    no_of_usb = st.selectbox('No. of USB Ports', list(df_filtered['No. of USB Ports'].unique()))
    if st.checkbox('Filter by Weight'):
        weight_unit = st.radio("Select weight unit:", ('Pounds', 'Kgs'))
        if weight_unit == 'Pounds':
            weight = st.selectbox('Laptop Weight in Pounds', list(df_filtered['Weight in Pounds'].unique()))
            df_filtered = df_filtered[df_filtered['Weight in Pounds'] == weight]
        else:
            weight = st.selectbox('Laptop Weight in Kgs', list(df_filtered['Weight in Kgs'].unique()))
            df_filtered = df_filtered[df_filtered['Weight in Kgs'] == weight]
    price = st.slider('Price', min_value=500, max_value=5000, value=300)

    if st.button('Recommend Laptops'):
        df_filtered['Price'] = pd.to_numeric(df_filtered['Price'], errors='coerce')
        recommended_df = df_filtered[(df_filtered['Intel Core Version'] == intel_core_version) &
                                     (df_filtered['RAM Storage Capacity'].apply(convert_storage_capacity) >= ram) &
                                     (df_filtered['Internal Storage Capacity'].apply(convert_storage_capacity) >= internal_storage) &
                                     (df_filtered['Price'] <= price)]
        st.dataframe(recommended_df[['Laptop Model Name', 'Price']])
        #st.success(f"Recommended Laptop Models:\n\n{', '.join(laptop_models)}")
        if st.button('Clear Recommendations'):
            #st.caching.clear_cache()  # Clear the cache
            st.experimental_rerun()  # Rerun the app

if __name__ == "__main__":
    main()
