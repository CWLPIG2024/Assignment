import streamlit as st 


st.title("Welcome!")
st.write("Navigate to the **HDB Past Resale Flat Prices** or **HDB Resale Flat Eligibility Checker** page using the sidebar to start.")

with st.expander("Disclaimer"):
    st.write ("""
        **IMPORTANT NOTICE**: This web application is a prototype developed for **educational purposes only**. The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**

Always consult with qualified professionals for accurate and personalized advice.

    """)