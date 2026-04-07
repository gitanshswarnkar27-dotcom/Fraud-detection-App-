import streamlit as st
import pandas as pd
import joblib

st.title("💳 Fraud Detection App")
st.write("Enter transaction details:")

amount = st.number_input("Transaction Amount:", min_value=0.0)

oldbalanceOrg = st.number_input("Old Balance Sender:", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Sender:", min_value=0.0)

oldbalanceDest = st.number_input("Old Balance Receiver:", min_value=0.0)
newbalanceDest = st.number_input("New Balance Receiver:", min_value=0.0)

model = joblib.load("model.pkl")

if st.button("Predict"):

    # 🔥 SAME FEATURE ENGINEERING
    balance_diff = oldbalanceOrg - newbalanceOrig

    data = pd.DataFrame([[amount, oldbalanceOrg, newbalanceOrig,
                          oldbalanceDest, newbalanceDest,
                          balance_diff]],
                        columns=[
                            "amount",
                            "oldbalanceOrg",
                            "newbalanceOrig",
                            "oldbalanceDest",
                            "newbalanceDest",
                            "balance_diff"
                        ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("🚨 Fraud Transaction Detected!")
    else:
        st.success("✅ Safe Transaction")