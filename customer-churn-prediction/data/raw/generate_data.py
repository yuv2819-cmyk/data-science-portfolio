import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate 10,000 customer records
n_customers = 10000

# Customer IDs
customer_ids = [f'CUST{str(i).zfill(6)}' for i in range(1, n_customers + 1)]

# Demographics
genders = np.random.choice(['Male', 'Female'], n_customers, p=[0.52, 0.48])
ages = np.random.normal(42, 15, n_customers).clip(18, 80).astype(int)
senior_citizen = (ages >= 65).astype(int)

# Geographic data
states = np.random.choice(['CA', 'TX', 'FL', 'NY', 'PA', 'IL', 'OH', 'GA', 'NC', 'MI'], n_customers)
cities = [f'City_{random.randint(1, 50)}' for _ in range(n_customers)]

# Account information
tenure_months = np.random.exponential(24, n_customers).clip(0, 72).astype(int)
contract_types = np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], n_customers, 
                                   p=[0.55, 0.25, 0.20])

# Service features
phone_service = np.random.choice([0, 1], n_customers, p=[0.1, 0.9])
multiple_lines = np.where(phone_service == 1, 
                          np.random.choice([0, 1], n_customers, p=[0.5, 0.5]), 
                          0)

internet_service = np.random.choice(['No', 'DSL', 'Fiber Optic'], n_customers, 
                                     p=[0.2, 0.35, 0.45])
online_security = np.where(internet_service != 'No',
                           np.random.choice([0, 1], n_customers, p=[0.6, 0.4]),
                           0)
online_backup = np.where(internet_service != 'No',
                         np.random.choice([0, 1], n_customers, p=[0.55, 0.45]),
                         0)
device_protection = np.where(internet_service != 'No',
                             np.random.choice([0, 1], n_customers, p=[0.6, 0.4]),
                             0)
tech_support = np.where(internet_service != 'No',
                        np.random.choice([0, 1], n_customers, p=[0.65, 0.35]),
                        0)
streaming_tv = np.where(internet_service != 'No',
                        np.random.choice([0, 1], n_customers, p=[0.5, 0.5]),
                        0)
streaming_movies = np.where(internet_service != 'No',
                            np.random.choice([0, 1], n_customers, p=[0.5, 0.5]),
                            0)

# Billing information
paperless_billing = np.random.choice([0, 1], n_customers, p=[0.4, 0.6])
payment_methods = np.random.choice(['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card'],
                                    n_customers, p=[0.33, 0.15, 0.22, 0.30])

# Calculate monthly charges based on services
base_charge = 20
monthly_charges = base_charge + \
                  (phone_service * 10) + \
                  (multiple_lines * 5) + \
                  (np.where(internet_service == 'DSL', 30, 0)) + \
                  (np.where(internet_service == 'Fiber Optic', 50, 0)) + \
                  (online_security * 5) + \
                  (online_backup * 5) + \
                  (device_protection * 5) + \
                  (tech_support * 5) + \
                  (streaming_tv * 10) + \
                  (streaming_movies * 10)

# Add some variance
monthly_charges = monthly_charges + np.random.normal(0, 3, n_customers)
monthly_charges = monthly_charges.clip(20, 120).round(2)

# Total charges
total_charges = (monthly_charges * tenure_months).round(2)
total_charges = np.where(tenure_months == 0, 0, total_charges)

# Calculate churn with realistic patterns
churn_probability = 0.15  # Base churn rate

# Factors that increase churn
churn_score = np.zeros(n_customers)
churn_score += (contract_types == 'Month-to-Month') * 0.30  # Month-to-month more likely to churn
churn_score += (tenure_months < 6) * 0.25  # New customers churn more
churn_score += (monthly_charges > 70) * 0.15  # High price increases churn
churn_score += (online_security == 0) * 0.10  # No security service
churn_score += (tech_support == 0) * 0.10  # No tech support
churn_score += (payment_methods == 'Electronic Check') * 0.15  # Electronic check less reliable
churn_score += (internet_service == 'Fiber Optic') * 0.10  # Fiber customers have more options

# Factors that decrease churn
churn_score -= (contract_types == 'Two Year') * 0.25  # Long contracts reduce churn
churn_score -= (tenure_months > 24) * 0.20  # Loyal customers stay
churn_score -= (paperless_billing == 1) * 0.05  # Engaged customers
churn_score -= (payment_methods == 'Bank Transfer') * 0.05  # Auto payment reduces churn

# Add random noise
churn_score += np.random.normal(0, 0.1, n_customers)

# Convert to probability and generate churn
churn_prob_final = 1 / (1 + np.exp(-churn_score))  # Sigmoid to keep in [0,1]
churn = (np.random.random(n_customers) < churn_prob_final).astype(int)

# Customer satisfaction score (inversely related to churn)
satisfaction_score = (100 - churn_prob_final * 100 + np.random.normal(0, 10, n_customers)).clip(0, 100).round(1)

# Support tickets (churners have more tickets)
support_tickets = np.where(churn == 1,
                           np.random.poisson(3, n_customers),
                           np.random.poisson(1, n_customers))

# Create DataFrame
df = pd.DataFrame({
    'CustomerID': customer_ids,
    'Gender': genders,
    'Age': ages,
    'SeniorCitizen': senior_citizen,
    'State': states,
    'City': cities,
    'TenureMonths': tenure_months,
    'ContractType': contract_types,
    'PhoneService': phone_service,
    'MultipleLines': multiple_lines,
    'InternetService': internet_service,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'PaperlessBilling': paperless_billing,
    'PaymentMethod': payment_methods,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'SatisfactionScore': satisfaction_score,
    'SupportTickets': support_tickets,
    'Churn': churn
})

# Save to CSV
df.to_csv('customer_churn_data.csv', index=False)

print(f"Dataset generated successfully!")
print(f"Total records: {len(df)}")
print(f"Churn rate: {df['Churn'].mean():.2%}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nDataset info:")
print(df.info())
print(f"\nChurn distribution:")
print(df['Churn'].value_counts())
