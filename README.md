# financial-scoring-model
This project evaluates a family's financial health using a scoring mechanism. The score is calculated based on multiple financial factors, and the model provides actionable insights and recommendations to improve financial well-being.

**Features**
Financial Scoring Model:
Calculates a financial score (range: 0–100) for each family based on provided financial data.
FastAPI Deployment:
Exposes the model as an API to accept family-level data and return scores with insights.
Streamlit Dashboard (Bonus):
Allows users to interact with the model and view financial insights.

**Scoring Model Logic**
The financial score is calculated based on the following factors:

Savings-to-Income Ratio (Weight: 25%):
Higher savings relative to income improve the score.
Monthly Expenses as a Percentage of Income (Weight: 20%):
Lower expenses relative to income improve the score.
Loan Payments as a Percentage of Income (Weight: 15%):
Lower loan payments relative to income improve the score.
Credit Card Spending Trends (Weight: 10%):
Excessive credit card spending negatively impacts the score.
Financial Goals Met (Weight: 30%):
A direct measure of financial goals achieved.

**Calculation Steps**
Normalization: Each factor is normalized to a 0–100 scale.
Example: A savings-to-income ratio of 0.25 maps to a score of 25.
Weight Application: Each factor's score is multiplied by its weight.
Aggregation: The weighted scores are summed and normalized to 100.

**Setup Instructions**
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-repo/financial-scoring-model.git
cd financial-scoring-model
2. Create a Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the FastAPI Application
bash
Copy code
uvicorn main:app --reload
FastAPI will start on http://127.0.0.1:8000.
5. Interact with the API
Test the API Locally
Use tools like Postman, cURL, or your browser to send a POST request to the /score/ endpoint.

Example request body:

json
Copy code
{
    "Family_ID": "F123",
    "Income": 100000,
    "Savings": 20000,
    "Monthly_Expenses": 50000,
    "Loan_Payments": 10000,
    "Credit_Card_Spending": 5000,
    "Financial_Goals_Met": 80
}
Example response:

json
Copy code
{
    "Financial_Score": 75.5,
    "Detailed_Scores": {
        "Savings_Score": 20.0,
        "Expenses_Score": 50.0,
        "Loan_Score": 90.0,
        "Credit_Score": 95.0,
        "Goals_Score": 80
    },
    "Insights": "Savings are below recommended levels, which affects your score negatively."
}

**Bonus: Streamlit Dashboard**
Run the Streamlit App
bash
Copy code
streamlit run dashboard.py
The dashboard will open in your default web browser.
Input family data to calculate the financial score and view recommendations.

**Explanation of Weights and Insights**
**Weights**
Savings-to-Income (25%): A key measure of financial stability.
Expenses-to-Income (20%): High expenses reduce savings potential and impact the score.
Loan Payments-to-Income (15%): Excessive loan payments lead to financial strain.
Credit Card Spending (10%): Overuse of credit can indicate poor financial planning.
Financial Goals Met (30%): Meeting goals reflects positive financial habits.

**Insights**
The model provides recommendations based on key factors:

Example: "Increase savings to at least 20% of your income to improve your score by 10 points."

**Future Enhancements**
Add more financial factors (e.g., retirement savings, insurance coverage).
Extend API to support batch scoring for multiple families.
Enhance dashboard visualizations with trend analysis.
License
This project is licensed under the MIT License. See the LICENSE file for details.
