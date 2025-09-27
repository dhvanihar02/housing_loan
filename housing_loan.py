# housing_loan_eda.py

# -------------------------------
# 1️⃣ Import Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: improve plot aesthetics
sns.set(style="whitegrid")

# -------------------------------
# 2️⃣ Load Dataset
# -------------------------------
df = pd.read_csv("housing_loan_data.csv")
print("First 5 rows:\n", df.head(), "\n")
print("Shape:", df.shape)
print("\nInfo:\n")
print(df.info())
print("\nSummary Statistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# -------------------------------
# 3️⃣ Univariate Analysis
# -------------------------------
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=15, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['ApplicantIncome'], bins=20, kde=True)
plt.title("Applicant Income Distribution")
plt.xlabel("Applicant Income")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['LoanAmount'], bins=20, kde=True)
plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Loan_Status', data=df)
plt.title("Loan Status Counts")
plt.xlabel("Loan Status")
plt.ylabel("Count")
plt.show()

# -------------------------------
# 4️⃣ Bivariate Analysis
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x='Credit_History', hue='Loan_Status', data=df)
plt.title("Loan Status by Credit History")
plt.xlabel("Credit History")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Property_Area', hue='Loan_Status', data=df)
plt.title("Loan Status by Property Area")
plt.xlabel("Property Area")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='ApplicantIncome', y='LoanAmount', hue='Loan_Status', data=df)
plt.title("Loan Amount vs Applicant Income")
plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")
plt.show()

plt.figure(figsize=(6,4))
df.groupby('Employment_Type')['LoanAmount'].mean().plot(kind='bar')
plt.title("Average Loan Amount by Employment Type")
plt.xlabel("Employment Type")
plt.ylabel("Average Loan Amount")
plt.show()

# -------------------------------
# 5️⃣ Multivariate / Crosstabs
# -------------------------------
print("\nApproval % by Credit History:\n")
print(pd.crosstab(df['Credit_History'], df['Loan_Status'], normalize='index')*100)

plt.figure(figsize=(6,4))
sns.heatmap(pd.crosstab(df['Property_Area'], df['Loan_Status'], normalize='index')*100,
            annot=True, cmap="Blues")
plt.title("Loan Status % by Property Area")
plt.show()

# -------------------------------
# 6️⃣ Boxplots and Correlation (numeric only)
# -------------------------------
plt.figure(figsize=(6,4))
sns.boxplot(x='Loan_Status', y='LoanAmount', data=df)
plt.title("Loan Amount by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Loan Amount")
plt.show()

plt.figure(figsize=(8,6))
numeric_cols = df.select_dtypes(include=np.number)
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix (Numeric Features)")
plt.show()

# -------------------------------
# 7️⃣ Example Insights (print)
# -------------------------------
approved_ratio = df[df['Loan_Status']=='Approved'].shape[0] / df.shape[0] * 100
print(f"Overall Loan Approval Rate: {approved_ratio:.2f}%")
credit_approved = pd.crosstab(df['Credit_History'], df['Loan_Status'], normalize='index')*100
print("\nApproval % by Credit History:\n", credit_approved)
