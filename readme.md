# Housing Loan Data Analysis (EDA Project)

## Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a housing loan dataset, inspired by India Shelter Homes.  
The goal is to understand patterns in loan approval, analyze applicant profiles, and extract actionable insights that can help in business decision-making.

---

## Dataset
The dataset consists of **300 mock applicants** with the following columns:

| Column Name       | Description |
|------------------|-------------|
| ApplicantID       | Unique ID of applicant |
| Age               | Age of applicant |
| Gender            | Male / Female |
| Marital_Status    | Married / Single |
| Education         | Graduate / Not Graduate |
| Employment_Type   | Salaried / Self Employed |
| ApplicantIncome   | Monthly income of applicant |
| LoanAmount        | Loan amount applied |
| Loan_Term_Months  | Loan tenure in months |
| Credit_History    | 1 = Good, 0 = Poor |
| Property_Area     | Urban / Semiurban / Rural |
| Loan_Status       | Approved / Rejected |

---

## Libraries Used
- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  

---

## EDA Steps
1. **Data Loading and Overview**
   - Checked shape, info, summary statistics, missing values.
2. **Univariate Analysis**
   - Plotted distributions of Age, Applicant Income, Loan Amount.
   - Count of Loan Status (Approved vs Rejected).
3. **Bivariate Analysis**
   - Examined relationships between Credit History, Property Area, Employment Type and Loan Status.
   - Scatter plot of Applicant Income vs Loan Amount.
4. **Multivariate Analysis**
   - Crosstab and heatmap to analyze Loan Status percentages across groups.
5. **Boxplots & Correlation**
   - Boxplots to see spread of Loan Amount by approval.
   - Correlation matrix for numeric features.
6. **Insights**
   - Applicants with good credit history had higher approval rates.
   - Urban areas had higher loan amounts; semiurban areas had higher approvals.
   - Self-employed applicants had slightly lower approval rates than salaried.

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/housing-loan-eda.git
