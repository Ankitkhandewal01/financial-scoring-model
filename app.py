import streamlit as st
from app1 import calculate_score
st.title("Financial Scoring Model")

# Input form
st.sidebar.header("Input Family Data")
income = st.sidebar.number_input("Monthly Income", min_value=0)
savings = st.sidebar.number_input("Savings", min_value=0)
monthly_expenses = st.sidebar.number_input("Monthly Expenses", min_value=0)
loan_payments = st.sidebar.number_input("Loan Payments", min_value=0)
credit_card_spending = st.sidebar.number_input("Credit Card Spending", min_value=0)
financial_goals_met = st.sidebar.slider("Financial Goals Met (%)", 0, 100, 50)

# Calculate score
if st.sidebar.button("Calculate Score"):
    family_data = {
        "Income": income,
        "Savings": savings,
        "Monthly_Expenses": monthly_expenses,
        "Loan_Payments": loan_payments,
        "Credit_Card_Spending": credit_card_spending,
        "Financial_Goals_Met": financial_goals_met,
    }
    score, details = calculate_score(family_data)
    st.subheader(f"Financial Score: {score}")
    st.json(details)

    # Recommendations
    st.write("**Recommendations:**")
    if family_data["Savings"] / family_data["Income"] < 0.2:
        st.write("Increase savings to at least 20% of your income.")
    if family_data["Monthly_Expenses"] / family_data["Income"] > 0.5:
        st.write("Reduce monthly expenses to below 50% of your income.")
