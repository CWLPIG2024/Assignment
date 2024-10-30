import streamlit as st

# Set the title of the Streamlit app
st.title("About Us")

# Define the HTML content
html_content = """
<h2>Project Scope</h2>
<p>The HDB Resale Flat Eligibility Checker and HDB Past Resale Flat Prices Application seeks to assist users in purchasing resale flats in Singapore. This application provides two main objectives:</p>
<ul>
    <li><strong>Eligibility Checker</strong>: Assesses user eligibility based on various criteria such as age, citizenship, marital status, and property ownership status.</li>
    <li><strong>Past Resale Transactions Analysis</strong>: For users to obtain historical resale flat prices, and explore past market trends.</li>
</ul>

<h2>Data Sources</h2>
<p><strong>HDB Transaction Data</strong>: Resale flat transaction data from the Housing and Development Board (HDB). This dataset includes information on resale prices, flat types, towns, storey ranges, and transaction dates.</p>

<h2>Features</h2>
<p>The application includes the following features:</p>
<h3>1. Eligibility Checker:</h3>
<ul>
    <li><strong>User Inputs</strong>: Gather essential information such as age, citizenship status, marital status, property ownership, and years as a Permanent Resident.</li>
    <li><strong>Conversational Interface</strong>: Enable users to ask follow-up questions and receive advice through a chatbot feature.</li>
</ul>
    
<h3>2. Past Resale Transactions Analysis</h3>
<ul>
    <li><strong>Dynamic Filtering</strong>: Users can filter past resale transactions based on criteria such as town, flat type, storey range, and months passed since the last transaction.</li>
    <li><strong>Price Statistics</strong>: Calculate and display key price metrics, including highest, lowest, average, and median resale prices.</li>
</ul>
"""

# Render the HTML content in the Streamlit app
st.markdown(html_content, unsafe_allow_html=True)
