import streamlit as st
import pandas as pd

# Load the phone specifications from the Excel file
url = 'https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx'
df = pd.read_excel(url)

# Create dropdown for operating system
operating_system = st.selectbox('Select Operating System', df['Operating System'].unique())

# Create slider for storage space
storage_space = st.slider('Select Storage Space (GB)', min_value=0, max_value=df['Storage'].max(), step=1)

# Create checkboxes for connectivity
connectivity_options = ['5G', '4G', 'Wi-Fi', 'NFC']
connectivity_selected = st.multiselect('Select Connectivity', connectivity_options, connectivity_options)

# Create checkboxes for design and build quality
design_options = ['Glass', 'Stainless Steel', 'Metal', 'Aluminium', 'Polycarbonate', 'Plastic', 'Gorilla Glass']
design_selected = st.multiselect('Select Design & Build Quality', design_options, design_options)

# Create checkboxes for security and privacy
security_options = ['Face ID', 'Facial Recognition', 'Rear-Mounted', 'In-Display']
security_selected = st.multiselect('Select Security & Privacy Features', security_options, security_options)

# Create slider for IP rating
ip_rating = st.slider('Select IP Rating (IP67 or IP68)', min_value=67, max_value=68, step=1)

# Create checkboxes for additional features
additional_features = ['Stylus Pen Support', 'Magsafe Compatibility', 'AMOLED & OLED Display', 'Pop-up Camera', 'VR Support', 'Optical Image Stabilization']
additional_selected = st.multiselect('Select Additional Features', additional_features, additional_features)

# Create slider for USB type
usb_type = st.slider('Select USB Type (USB Type-C or Type-B)', min_value=0, max_value=1, step=1)

# Create slider for price range
price_range = st.slider('Select Price Range', min_value=0, max_value=df['Price'].max(), step=100)

# Filter the dataframe based on the selected criteria
filtered_df = df[
    (df['Operating System'] == operating_system) &
    (df['Storage'] >= storage_space) &
    (df['Connectivity'].apply(lambda x: all(option in x for option in connectivity_selected))) &
    (df['Design & Build Quality'].apply(lambda x: all(option in x for option in design_selected))) &
    (df['Security & Privacy'].apply(lambda x: all(option in x for option in security_selected))) &
    (df['IP Rating'] >= ip_rating) &
    (df['Additional Features'].apply(lambda x: all(option in x for option in additional_selected))) &
    (df['USB Type'] == usb_type) &
    (df['Price'] <= price_range)
]

# Display the filtered phones
if len(filtered_df) > 0:
    st.table(filtered_df)
else:
    st.warning('No phones match the selected criteria.')


