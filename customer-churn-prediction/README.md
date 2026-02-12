# 🎯 Customer Churn Prediction

## Project Overview

This project analyzes customer churn patterns in a telecommunications company and builds machine learning models to predict which customers are likely to cancel their subscriptions. The predictive models enable proactive retention strategies and help reduce revenue loss.

## Business Problem

Customer churn is a critical challenge for subscription-based businesses. Identifying at-risk customers early allows companies to:
- Implement targeted retention campaigns
- Optimize pricing and service offerings
- Improve customer satisfaction and loyalty
- Reduce customer acquisition costs

## Dataset

- **Size**: 10,000 customer records
- **Features**: 23 attributes organized into:
  - **Demographics**: Age, Gender, Senior Citizen status
  - **Account Information**: Tenure, Contract Type, Payment Method
  - **Services**: Phone, Internet, Security, Backup, Streaming
  - **Financial**: Monthly Charges, Total Charges
  - **Engagement**: Satisfaction Score, Support Tickets
- **Target**: Binary churn indicator (Churned = 1, Retained = 0)
- **Churn Rate**: ~27%

## Project Structure

```
customer-churn-prediction/
├── data/
│   ├── raw/                    # Original dataset
│   └── processed/              # Cleaned and preprocessed data
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb # Data preprocessing & feature engineering
│   └── 03_modeling.ipynb      # Model training & evaluation
├── models/                     # Saved trained models
├── visualizations/             # Generated charts and plots
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Key Findings

### Churn Drivers

1. **Contract Type** ⚡
   - Month-to-month contracts: ~45% churn rate
   - Long-term contracts (1-2 years): ~10-15% churn rate

2. **Customer Tenure** 📅
   - New customers (0-12 months): Highest churn risk
   - Established customers (24+ months): Significantly lower churn

3. **Service Adoption** 🛡️
   - Customers with security, backup, and tech support: Lower churn
   - Service count inversely correlated with churn

4. **Pricing** 💰
   - Higher monthly charges (>$70): Increased churn probability
   - Price sensitivity is a major factor

5. **Customer Satisfaction** ⭐
   - Strong negative correlation between satisfaction and churn
   - Support ticket volume predicts dissatisfaction

## Machine Learning Models

### Models Implemented

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.79 | 0.67 | 0.73 | 0.70 | 0.83 |
| Random Forest | 0.81 | 0.71 | 0.76 | 0.73 | 0.86 |
| Gradient Boosting | 0.82 | 0.73 | 0.77 | 0.75 | 0.87 |
| **XGBoost** | **0.84** | **0.75** | **0.80** | **0.77** | **0.88** |

**Best Model**: XGBoost with 88% ROC-AUC score

### Model Features

- ✅ Handles class imbalance using SMOTE
- ✅ Feature engineering (RFM analysis, service utilization)
- ✅ Multiple algorithm comparison
- ✅ SHAP values for model interpretability
- ✅ Business impact analysis and ROI calculation

## Business Impact

Using the XGBoost model with a targeted retention campaign:

- **Customers Identified**: ~500 high-risk customers
- **Expected Customers Saved**: ~150 (30% campaign success rate)
- **Revenue Saved**: ~$300,000 (@ $2,000 LTV per customer)
- **Campaign Cost**: $50,000 (@ $100 per customer)
- **Net Benefit**: $250,000
- **ROI**: 500%

## Visualizations

The project includes 13 professional visualizations:

1. Churn distribution analysis
2. Demographic patterns (age, gender, senior status)
3. Contract and tenure analysis
4. Service adoption impact
5. Financial metrics (monthly/total charges)
6. Customer engagement (satisfaction, support tickets)
7. Feature correlation heatmap
8. Model performance comparison
9. Confusion matrices
10. ROC curves
11. Feature importance
12. SHAP feature importance
13. SHAP value distribution

## Installation & Usage

### Prerequisites

```bash
Python 3.9 or higher
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Analysis

Execute the notebooks in order:

1. **01_eda.ipynb**: Explore the data, understand churn patterns, generate insights
2. **02_preprocessing.ipynb**: Clean data, engineer features, prepare train/test sets
3. **03_modeling.ipynb**: Train models, evaluate performance, interpret results

## Key Recommendations

### Strategic Actions

1. **Contract Incentives** 📝
   - Offer discounts for 1-2 year commitments
   - Target month-to-month customers with upgrade offers

2. **Early Retention Program** 🎯
   Focus retention efforts on customers in first 6-12 months

3. **Service Bundling** 📦
   - Promote security + backup + support packages
   - Highlight value-add services to increase stickiness

4. **Pricing Optimization** 💲
   - Review high-cost plans for competitive positioning
   - Offer loyalty discounts to long-term customers

5. **Customer Success** 🌟
   - Proactive support outreach for low satisfaction scores
   - Reduce support ticket incidents through quality improvements

6. **Automated Scoring** 🤖
   - Deploy model to score all customers monthly
   - Create automated alerts for churn probability > 70%
   - Segment campaigns by risk level (high/medium/low)

## Technical Skills Demonstrated

- ✅ **Data Analysis**: Pandas, NumPy, comprehensive EDA
- ✅ **Visualization**: Matplotlib, Seaborn, publication-quality plots
- ✅ **Machine Learning**: Scikit-learn, XGBoost, ensemble methods
- ✅ **Model Evaluation**: ROC-AUC, confusion matrices, cross-validation
- ✅ **Interpretability**: SHAP values, feature importance
- ✅ **Class Imbalance**: SMOTE oversampling technique
- ✅ **Feature Engineering**: Domain-driven feature creation
- ✅ **Business Acumen**: ROI calculation, stakeholder insights

## Future Enhancements

- [ ] Deep learning model (Neural Network)
- [ ] Real-time scoring API (FastAPI/Flask)
- [ ] A/B testing framework for retention campaigns
- [ ] Customer lifetime value (CLV) prediction
- [ ] Interactive dashboard (Streamlit/Plotly Dash)
- [ ] Survival analysis for time-to-churn prediction

## Author

Data Scientist Portfolio Project

---

**Note**: This project uses synthetic data generated for demonstration purposes. The patterns and insights are designed to reflect realistic business scenarios in the telecommunications industry.
