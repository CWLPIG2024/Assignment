import streamlit as st
import base64
from pathlib import Path

# Set the title of the Streamlit app
st.title("Methodology")

# Introduction Section
st.markdown("""
<h2>Introduction</h2>
<p>This methodology page provides a explanation of the data flows and implementation details.</p>
""", unsafe_allow_html=True)

# Data Flows Section
st.markdown("""
<h2>Data Flows</h2>

<h3>Data Collection and Processing</h3>
<p>Data is gathered via integration with HDB API for real-time data access and validation in CSV, which has been cleaned before analysis. Some fields for resale flat transaction data are:</p>
<ul>
    <li>Resale prices</li>
    <li>Flat types</li>
    <li>Towns</li>
    <li>Storey ranges</li>
    <li>Transaction dates</li>
</ul>

<p>The data is transformed and calculated (i.e. months since the last transaction().</p>

<h3>Data Storage</h3>
<p>Data is stored in DataFrame for easier manipulation using Python libraries such as Pandas.</p>

<h3>Data Output</h3>
<p>The application outputs data by providing users with insights into eligibility and past transaction prices. Users can also obtain statistics for informed decision-making.</p>
""", unsafe_allow_html=True)


st.markdown("""
<h2>Flowchart</h2>
<p>Below is the flowchart illustrating the process flow for each use case:</p>
""", unsafe_allow_html=True)

st.image ("pages/images/HDB Past Resale Flat Prices.jpg",caption = "HDB Past Resale Flat Prices")
st.image ("pages/images/HDB Resale Flat Eligibility Checker.jpg",caption = "HDB Resale Flat Eligibility Checker")