import streamlit as st
import pandas as pd
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/Phone-Specifications.xlsx')
def main():
    # Create a checkbox
    # Sidebar components for user input
    operating_system = st.selectbox('Select Operating System', list(df['Operating System'].unique()))
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
    # Filter the data based on the selected operating system
    #filtered_data = df[df['Operating System'] == operating_system]
    st.write(operating_system)
    st.write(storage_space)
    # Display the filtered data
    #st.write("Filtered Data:")
    #st.dataframe(filtered_data)
    # Display a message based on the checkbox state
    if operating_system:
        st.write("Checkbox is checked!")
    else:
        st.write("Checkbox is unchecked!")

if __name__ == '__main__':
    main()
