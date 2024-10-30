import pandas as pd
import streamlit as st
from datetime import datetime

# Load the dataset
def load_data():
    df = pd.read_csv('data/downloaded_data.csv')
    return df

# Load data
data = load_data()

# Keep the 'month' column in its original format
# Calculate the number of months passed since the transaction month
today = datetime.now()
current_year = today.year
current_month = today.month

# Calculate months passed directly without extracting year and month
data['months_passed'] = (
    (current_year - data['month'].str[:4].astype(int)) * 12 +
    (current_month - data['month'].str[5:7].astype(int))
)

# Streamlit application
st.title('HDB Past Resale Flat Prices')

# User input fields with multiple selection
selected_towns = st.multiselect('Select Towns:', data['town'].unique())
selected_flat_types = st.multiselect('Select Flat Types:', data['flat_type'].unique())
selected_storey_ranges = st.multiselect('Select Storey Ranges:', [
    '01 TO 03', '04 TO 06', '07 TO 09', '10 TO 12',
    '13 TO 15', '16 TO 18', '19 TO 21', '22 TO 24',
    '25 TO 27', '28 TO 30', '31 TO 33', '34 TO 36',
    '37 TO 39', '40 TO 42', '43 TO 45', '46 TO 48',
    '49 TO 51', '(blank)'
])
selected_flat_models = st.multiselect('Select Flat Models:', data['flat_model'].unique())

# Add a filter for months_passed
months_range = st.slider('Select months passed since last transaction:', 1, 12, (1, 12))

# Calculate price statistics based on user selections
if st.button('Calculate'):
    # Filter the data based on user inputs
    filtered_data = data[
        (data['town'].isin(selected_towns)) &
        (data['flat_type'].isin(selected_flat_types)) &
        (data['flat_model'].isin(selected_flat_models)) &
        (data['storey_range'].fillna('(blank)').isin(selected_storey_ranges)) &
        (data['months_passed'].between(months_range[0], months_range[1]))  # Filter by months_passed
    ]

    # Calculate statistics
    if not filtered_data.empty:
        highest_price = filtered_data['resale_price'].max()
        lowest_price = filtered_data['resale_price'].min()
        average_price = filtered_data['resale_price'].mean()
        median_price = filtered_data['resale_price'].median()
        
        st.subheader('Price Statistics:')
        st.write(f'Highest Price: ${highest_price:,.2f}')
        st.write(f'Lowest Price: ${lowest_price:,.2f}')
        st.write(f'Average Price: ${average_price:,.2f}')
        st.write(f'Median Price: ${median_price:,.2f}')
    else:
        st.write('No data available for the selected criteria.')

    # Show the filtered DataFrame with the new column
    st.subheader('Filtered DataFrame:')
    st.dataframe(filtered_data)  # Display the filtered data instead of the entire data
