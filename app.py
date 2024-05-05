import streamlit as st
import joblib
import numpy as np

# Load the machine learning model
model = joblib.load('frauddetection.pkl')

# Define the Streamlit app
st.title("Credit Card Fraud Detection Web App")

# Description of the app
st.write("""
## About
Credit card fraud is a form of identity theft that involves an unauthorized taking of another's credit card information for the purpose of charging purchases to the account or removing funds from it.

**This Streamlit App utilizes a Machine Learning model served as an API in order to detect fraudulent credit card transactions based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.** 

The API was built with FastAPI and can be found [here.](https://credit-fraud-ml-api.herokuapp.com/)

The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) are available on [GitHub.](https://github.com/Nneji123/Credit-Card-Fraud-Detection)        

**Made by Group 3 Zummit Africa AI/ML Team**

**Contributors:** 
- **Hilary Ifezue(Group Lead)**
- **Nneji Ifeanyi**
- **Somtochukwu Ogechi**
- **ThankGod Omieje**
- **Kachukwu Okoh**
""")

# Input features of the transaction
st.sidebar.header('Input Features of The Transaction')
sender_name = st.sidebar.text_input("Input Sender ID")
receiver_name = st.sidebar.text_input("Input Receiver ID")
step = st.sidebar.slider("Number of Hours it took the Transaction to complete", 0, 100)
types = st.sidebar.selectbox("Type of Transfer Made", ("Cash In", "Cash Out", "Debit", "Payment", "Transfer"))
amount = st.sidebar.number_input("Amount in $", min_value=0.0, max_value=110000.0)
oldbalanceorig = st.sidebar.number_input("Old Balance Orig", min_value=0.0, max_value=110000.0)
newbalanceorig = st.sidebar.number_input("New Balance Orig", min_value=0.0, max_value=110000.0)
oldbalancedest = st.sidebar.number_input("Old Balance Dest", min_value=0.0, max_value=110000.0)
newbalancedest = st.sidebar.number_input("New Balance Dest", min_value=0.0, max_value=110000.0)

# Prediction function
def predict(step, types, amount, oldbalanceorig, newbalanceorig, oldbalancedest, newbalancedest):
    features = np.array([[step, types, amount, oldbalanceorig, newbalanceorig, oldbalancedest, newbalancedest]])
    predictions = model.predict(features)
    if predictions == 1:
        return "Fraudulent"
    else:
        return "Not Fraudulent"

# Set background color
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFE0; /* You can change this color code */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Detection result
if st.button("Detection Result"):
    values = {
        "step": step,
        "Type": types,
        "amount": amount,
        "oldbalanceorig": oldbalanceorig,
        "newbalanceorig": newbalanceorig,
        "oldbalancedest": oldbalancedest,
        "newbalancedest": newbalancedest,
    }

    st.write(f"""### These are the transaction details:
    Sender ID: {sender_name}
    Receiver ID: {receiver_name}
    1. Number of Hours it took to complete: {step}
    2. Type of Transaction: {types}
    3. Amount Sent: ${amount}
    4. Sender Balance Before Transaction: ${oldbalanceorig}
    5. Sender Balance After Transaction: ${newbalanceorig}
    6. Recipient Balance Before Transaction: ${oldbalancedest}
    7. Recipient Balance After Transaction: ${newbalancedest}
    """)

    # Detection result
    result = predict(step, types, amount, oldbalanceorig, newbalanceorig, oldbalancedest, newbalancedest)
    st.write(f"""### The '{types}' transaction is {result}.""")
