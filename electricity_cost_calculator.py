import pandas as pd
import streamlit as st

# Read the Excel file
df = pd.read_excel('https://asiliventures.com/wp-content/uploads/2023/05/ElectricityPriceModel.xlsx')

# Create Streamlit application
st.title("Electricity Cost Calculator")

# Checkbox for selecting appliances
appliances = df['Appliance'].unique()
selected_appliances = st.multiselect("Select the appliances you own:", appliances)

total_cost = 0

# Iterate over selected appliances
for appliance in selected_appliances:
    # Get the row index for the next appliance category
    next_appliance_index = df[df['Appliance'] == appliance].index.max() + 1

    # Get the corresponding data for the selected appliance and previous appliances
    appliance_data = df.iloc[:next_appliance_index]

    # Check if the selected appliance is "Television"
    if appliance == "Television":
        # Get all appliance data up to the next category
        tv_data = appliance_data[appliance_data['Appliance'] == appliance]

        # Get all the brands and model names for Television
        tv_brands = tv_data['Brands'].unique()
        tv_models = tv_data['Model Name'].unique()

        # Checkbox for selecting brand
        selected_brands = st.multiselect(f"Select the brand for {appliance}:", tv_brands, key=f"{appliance}_brands")

        # Filter the TV data based on selected brands
        selected_tv_data = tv_data[tv_data['Brands'].isin(selected_brands)]

        # Get the model names for the selected brands
        selected_model_names = selected_tv_data['Model Name'].unique()

        # Dropdown menu for selecting model name
        selected_model_name = st.selectbox(f"Select the model name for {appliance}:", selected_model_names, key=f"{appliance}_model")

        # Check if selected model name exists in the filtered data
        if selected_model_name in selected_tv_data['Model Name'].values:
            # Get the power rating for the selected model name
            power_rating = selected_tv_data[selected_tv_data['Model Name'] == selected_model_name]['Power Rating (Watts)'].values[0]
        else:
            power_rating = 0

    else:
        # Checkbox for selecting brand
        brands = appliance_data['Brands'].unique().dropna()
        selected_brands = st.multiselect(f"Select the brand for {appliance}:", brands, key=f"{appliance}_brands")

        # Get corresponding data for the selected brands
        selected_appliance_data = appliance_data[appliance_data['Brands'].isin(selected_brands)]

        # Dropdown menu for selecting model name
        model_names = selected_appliance_data['Model Name'].unique()
        selected_model_name = st.selectbox(f"Select the model name for {appliance}:", model_names, key=f"{appliance}_model")

        # Check if selected model name exists in the filtered data
        if selected_model_name in selected_appliance_data['Model Name'].values:
            # Get the power rating for the selected model name
            power_rating = selected_appliance_data[selected_appliance_data['Model Name'] == selected_model_name]['Power Rating (Watts)'].values[0]
        else:
            power_rating = 0

    # Calculate electricity cost
    hours_per_day = st.slider(f"Select the number of hours {appliance} is turned on:", 0, 24, 1)
    rate_per_kwhr = st.number_input("Enter the rate of electricity in dollars/kWhr:", min_value=0.0, step=0.01, value=0.12)

    # Calculate electricity cost for the selected appliance
    electricity_cost = (power_rating / 1000) * hours_per_day * rate_per_kwhr
    total_cost += electricity_cost

    # Display the calculated electricity cost
    st.write(f"The electricity cost for {appliance} ({selected_model_name}) is: ${electricity_cost:.2f}")

# Display the total electricity cost
st.subheader(f"Total Electricity Cost: ${total_cost:.2f}")
