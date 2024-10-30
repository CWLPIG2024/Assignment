import os
import streamlit as st
from helper_function import llm
from logic import eligibility_checker
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken
from helper_function.utility import check_password  

# Streamlit UI
st.title("HDB Resale Flat Eligibility Checker")

# Check if the password is correct.  
if not check_password():  
    st.stop()

age = st.number_input("Enter your age:", min_value=10, max_value=100)
citizenship = st.selectbox("Select your citizenship:", options=["Singapore Citizen", "Singapore Permanent Resident (SPR)", "Foreigner"])
years_as_pr = None

# Years as PR Input
if citizenship == "Singapore Permanent Resident (SPR)":
    # Set the max_value for years as PR to be the lesser of age and 100
    years_as_pr = st.number_input(
        "Enter the number of years as a Permanent Resident (PR):",
        min_value=0,
        max_value=age,  # Ensure max_value cannot exceed age
    )
else:
    st.write("You are not required to provide years as PR since you are either a Singapore Citizen or a Foreigner.")

# Display years_as_pr if applicable
if citizenship == "Singapore Permanent Resident (SPR)":
    st.write(f"Years as PR: {years_as_pr}")

marital_status = st.selectbox("Select your marital status:", options=["Single", "Married", "Widowed","Divorced"])

# Family Nucleus Input
if age >= 55:
    has_nucleus = st.selectbox("Select your buying status:", options=["Couples and Families", "Seniors (aged 55 years and above)", "Single"])
else:
    if marital_status in ["Married", "Widowed", "Divorced"]:
        has_nucleus = st.selectbox("Select your buying status:", options=["Couples and Families", "Single"])
    else:
        has_nucleus = st.selectbox("Select your buying status:", options=["Single"])  

# Property Ownership Input
owns_property = st.selectbox("Do you currently own any property?", options=["Yes", "No"])

# Non-Citizen Spouse Input
has_non_citizen_spouse = st.selectbox("Is your spouse a non-citizen?", options=["Yes", "No"])

if st.button("Check Inputs"):
    if citizenship == "Singapore Permanent Resident (SPR)" and (years_as_pr is None or years_as_pr > age):
        st.error("Years as PR cannot exceed your age.")
    else:
        eligibility_message = eligibility_checker.check_eligibility(
            age=age,
            citizenship=citizenship,
            marital_status=marital_status,
            has_nucleus=has_nucleus,
            has_non_citizen_spouse=has_non_citizen_spouse,
            owns_property=owns_property,
            years_as_pr=years_as_pr
        )
        st.success(eligibility_message)

# Initialize variables for the latest conversation
if 'last_user_query' not in st.session_state:
    st.session_state.last_user_query = None
    st.session_state.last_gpt_response = None

# Prepare the initial user query
if st.button("Chat with your data!"):
    user_query = (
        f"Age: {age}, Citizenship: {citizenship}, Marital Status: {marital_status}, "
        f"Years as PR: {years_as_pr if years_as_pr is not None else 'N/A'}, Has Nucleus: {has_nucleus}, "
        f"Non-Citizen Spouse: {has_non_citizen_spouse}, Owns Property: {owns_property}. "
        "List the eligibility conditions for buying a resale HDB flat."
    )
    
    # Call the get_completion function with the initial query
    try:
        gpt_response = llm.get_completion(user_query)
        st.session_state.last_user_query = user_query  # Save the last user query
        st.session_state.last_gpt_response = gpt_response  # Save the last GPT response
        
        # Display the assistant's response
        st.write("GPT-4o mini says:")
        st.info(gpt_response)

    except Exception as e:
        st.error(f"An error occurred while fetching advice: {e}")

# Input for user follow-up questions
if st.session_state.last_user_query is not None:
    user_input = st.text_input("Ask a follow-up question:", key="user_query")

    if st.button("Submit"):
        if user_input:
            # Prepare the context for the LLM with the last exchange
            conversation_context = f"User: {st.session_state.last_user_query}\nAssistant: {st.session_state.last_gpt_response}\nUser: {user_input}"
            
            try:
                # Call the get_completion function with the updated context
                gpt_response = llm.get_completion(conversation_context)
                st.session_state.last_user_query = user_input  # Update last user query
                st.session_state.last_gpt_response = gpt_response  # Update last GPT response
                
                # Display the assistant's response
                st.write("GPT-4o mini says:")
                st.info(gpt_response)
            except Exception as e:
                st.error(f"An error occurred while fetching advice: {e}")