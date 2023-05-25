import streamlit as st
import pandas as pd
from forex_python.converter import CurrencyRates

# Define the appliances and their power ratings
appliances = {
    'Television': 150,
    'Mobile Phone': 10,
    'Fridge': 200,
    'Iron Box': 1000,
    'Electric Kettle': 1500,
    'Radio Woofer': 80,
    'Microwave': 1000,
    'Mixer': 500,
    'Cooking Appliances': 1500,
    'Washers': 800,
    'Dryers': 1500,
    'Water Dispensers': 120,
    'Chapati Maker': 1000
}

# Create Streamlit application
st.title("Electricity Cost Calculator")

# Multiselect for selecting the user's country of residence
selected_countries = st.multiselect("Select your country of residence:", pd.read_csv('https://countrycode.org/api/csv/all')['ISO2'].to_list())

# Checkbox for selecting appliances
selected_appliances = st.multiselect("Select the appliances you own:", list(appliances.keys()))

total_cost = 0

# Iterate over selected appliances
for appliance in selected_appliances:
    # Get power rating for the selected appliance
    power_rating = appliances[appliance]

    # Slider for selecting the number of hours the appliance is turned on
    hours_per_day = st.slider(f"Select the number of hours {appliance} is turned on:", 0, 24, 1, key=appliance)

    # Input for the rate of electricity in dollars/kWhr
    rate_per_kwhr = st.number_input(f"Enter the rate of electricity in dollars/kWhr for {appliance}:", min_value=0.0, step=0.01, value=0.12, key=appliance+"_rate")

    # Calculate electricity cost for the selected appliance
    electricity_cost = (power_rating / 1000) * hours_per_day * rate_per_kwhr
    total_cost += electricity_cost

    # Display the calculated electricity cost
    st.write(f"The electricity cost for {appliance} is: ${electricity_cost:.2f}")

# Display the total electricity cost
st.subheader(f"Total Electricity Cost: ${total_cost:.2f}")

# Currency conversion using forex-python
if selected_countries:
    c = CurrencyRates()
    
    for currency in selected_countries:
        converted_cost = c.convert("USD", currency, total_cost)
        st.subheader(f"Total Electricity Cost in {currency}: {converted_cost:.2f}")
