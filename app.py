import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('frauddetection.pkl')

# Define the Streamlit app
st.title("Credit Card Fraud Detection Web App")

# Description of the app
st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App aims to detect fraudulent credit card transactions based on transaction details such as amount, sender/receiver information, and transaction type.** 

""")

# Input features of the transaction
st.sidebar.header('Input Features of The Transaction')
step = st.sidebar.slider("Number of Hours it took the Transaction to complete", 0, 100)
amount = st.sidebar.number_input("Amount in $", min_value=0.0, max_value=110000.0)
oldbalanceOrg = st.sidebar.number_input("Old Balance Orig", min_value=0.0, max_value=110000.0)
newbalanceOrig = st.sidebar.number_input("New Balance Orig", min_value=0.0, max_value=110000.0)
oldbalanceDest = st.sidebar.number_input("Old Balance Dest", min_value=0.0, max_value=110000.0)
newbalanceDest = st.sidebar.number_input("New Balance Dest", min_value=0.0, max_value=110000.0)
transaction_type = st.sidebar.selectbox("Type of Transfer Made", ("CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"))
sender_id = st.sidebar.text_input("Input Sender ID")
receiver_id = st.sidebar.text_input("Input Receiver ID")

# Prediction function
def predict(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, transaction_type, sender_id, receiver_id):
    # Here you would encode the transaction_type, sender_id, and receiver_id, if needed
    # Make sure to preprocess the input features in the same way as during model training
    # Then, create a feature array with the same format as used during training
    # For simplicity, let's assume all input features are numerical and don't need encoding
    features = np.array([[step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, transaction_type, sender_id, receiver_id]])
    prediction = model.predict(features)
    return "Fraudulent" if prediction == 1 else "Not Fraudulent"

# Detection result
if st.button("Detect Fraud"):
    result = predict(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, transaction_type, sender_id, receiver_id)
    st.write(f"The transaction is predicted as: {result}")
