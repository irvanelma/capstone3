import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Model
with open("finalmodel_irvan.sav", "rb") as model_file:
    final_model = pickle.load(model_file)

st.title('Customer Lifetime Value Prediction App')

# ========= INPUTS =========

# SELECTBOX for categorical feature
vehicle_class = st.selectbox('Vehicle Class', ['Four-Door Car', 'Two-Door Car', 'SUV', 'Sports Car', 'Luxury SUV', 'Luxury Car'])
coverage = st.radio('Coverage', ['Extended', 'Basic', 'Premium'])
renew_offer_type = st.selectbox('Renew Offer Type', ['Offer1', 'Offer2', 'Offer3', 'Offer4'])
employment_status = st.selectbox('EmploymentStatus', ['Retired', 'Employed', 'Disabled', 'Medical Leave', 'Unemployed'])
marital_status = st.radio('Marital Status', ['Divorced', 'Married', 'Single'])
education = st.selectbox('Education', ['High School or Below', 'College', 'Master', 'Bachelor', 'Doctor'])

# NUMBERINPUT for numerical
number_of_policies = st.number_input('Number of Policies', min_value=1, max_value=9, value=1, step=1)
monthly_premium_auto = st.number_input('Monthly Premium Auto', min_value=0.0, value=0.0, step=0.1)
total_claim_amount = st.number_input('Total Claim Amount', min_value=0.0, value=0.0, step=0.1)
income = st.number_input('Income', min_value=0.0, value=0.0, step=0.1)

# ========= PREDICTION =========

# Predict Button
if st.button('Predict Lifetime Value'):
    
    input_df = pd.DataFrame([[vehicle_class, coverage, renew_offer_type, employment_status, marital_status, education, 
                              number_of_policies, monthly_premium_auto, total_claim_amount, income]], 
                            columns=['Vehicle Class', 'Coverage', 'Renew Offer Type', 'EmploymentStatus', 'Marital Status', 'Education', 
                                     'Number of Policies', 'Monthly Premium Auto', 'Total Claim Amount', 'Income'])
    


    # Prediction
    prediction = final_model.predict(input_df)
    
    # Display prediction
    st.write(f'Predicted Customer Lifetime Value: ${prediction[0]:.2f}')
