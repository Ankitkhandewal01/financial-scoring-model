from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np

# Initialize FastAPI app
app = FastAPI()


# Define request schema
class FamilyData(BaseModel):
    Family_ID: str
    Income: int
    Savings: int
    Monthly_Expenses: int
    Loan_Payments: int
    Credit_Card_Spending: int
    Financial_Goals_Met: int

# Scoring function (reuse from earlier)
def calculate_score(data):
    weights = {
        'Savings_to_Income_Ratio': 25,
        'Monthly_Expenses_to_Income': 20,
        'Loan_Payments_to_Income': 15,
        'Credit_Card_Spending_Ratio': 10,
        'Financial_Goals_Met': 30
    }

    # Factor calculations
    savings_to_income = data['Savings'] / data['Income']
    expenses_to_income = data['Monthly_Expenses'] / data['Income']
    loan_to_income = data['Loan_Payments'] / data['Income']
    credit_to_income = data['Credit_Card_Spending'] / data['Income']

    # Calculate scores
    scores = {
        'Savings_Score': np.clip(savings_to_income * 100, 0, 100),
        'Expenses_Score': np.clip(100 - expenses_to_income * 100, 0, 100),
        'Loan_Score': np.clip(100 - loan_to_income * 100, 0, 100),
        'Credit_Score': np.clip(100 - credit_to_income * 100, 0, 100),
        'Goals_Score': data['Financial_Goals_Met']
    }

    # Aggregate score
    financial_score = (
        scores['Savings_Score'] * weights['Savings_to_Income_Ratio'] +
        scores['Expenses_Score'] * weights['Monthly_Expenses_to_Income'] +
        scores['Loan_Score'] * weights['Loan_Payments_to_Income'] +
        scores['Credit_Score'] * weights['Credit_Card_Spending_Ratio'] +
        scores['Goals_Score'] * weights['Financial_Goals_Met']
    ) / sum(weights.values())

    return financial_score, scores

# Endpoint
@app.post("/score/")
async def get_score(data: FamilyData):
    try:
        # Prepare input
        family_data = data.dict()
        
        # Calculate score
        financial_score, detailed_scores = calculate_score(family_data)
        
        # Historical insights (optional)
        similar_families = df[
            (df['Income'] == family_data['Income']) & 
            (df['Dependents'] == df.loc[df['Family ID'] == family_data['Family_ID'], 'Dependents'].values[0])
        ]
        insights = {
            "Financial_Score": financial_score,
            "Detailed_Scores": detailed_scores,
            "Insights": "Savings are below recommended levels, which affects your score negatively.",
            "Similar_Families_Avg_Score": similar_families['Financial_Score'].mean() if not similar_families.empty else "No data available"
        }
        return insights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
