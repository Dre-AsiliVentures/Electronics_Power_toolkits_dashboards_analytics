import streamlit as st
import pandas as pd
import pycountry
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

# Fetch country codes and names using pycountry
countries = [(country.alpha_2, country.name) for country in pycountry.countries]

# Sort countries by name
countries = sorted(countries, key=lambda x: x[1])

# Multiselect for selecting the user's country of residence
selected_countries = st.multiselect("Select your country of residence:", [name for _, name in countries])

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
    
    for country in selected_countries:
        currency_code = pycountry.countries.get(name=country).alpha_3
        converted_cost = c.convert("USD", currency_code, total_cost)
        st.subheader(f"Total Electricity Cost in {country}: {converted_cost:.2f}")
