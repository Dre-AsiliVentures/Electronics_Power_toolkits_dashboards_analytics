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

    # Checkbox for selecting brand
    brands = appliance_data['Brands'].unique().dropna()
    selected_brands = st.multiselect(f"Select the brand for {appliance}:", brands)

    # Iterate over selected brands
    for brand in selected_brands:
        # Get corresponding data for the selected brand
        brand_data = appliance_data[appliance_data['Brands'] == brand]

        # Dropdown menu for selecting model name
        model_names = brand_data['Model Name'].unique()
        selected_model_name = st.selectbox(f"Select the model name for {brand} {appliance}:", model_names)

        # Filter data for the selected model name
        model_data = brand_data[brand_data['Model Name'] == selected_model_name]

        if not model_data.empty:
            # Get the power rating for the selected model name
            power_rating = model_data['Power Rating (Watts)'].values[0]
        else:
            power_rating = 0

        # Calculate electricity cost
        hours_per_day = st.slider(f"Select the number of hours {brand} {appliance} is turned on:", 0, 24, 1)
        rate_per_kwhr = st.number_input("Enter the rate of electricity in dollars/kWhr:", min_value=0.0, step=0.01, value=0.12)

        # Calculate electricity cost for the selected appliance
        electricity_cost = (power_rating / 1000) * hours_per_day * rate_per_kwhr
        total_cost += electricity_cost

        # Display the calculated electricity cost
        st.write(f"The electricity cost for {brand} {appliance} ({selected_model_name}) is: ${electricity_cost:.2f}")

# Display the total electricity cost
st.subheader(f"Total Electricity Cost: ${total_cost:.2f}")
