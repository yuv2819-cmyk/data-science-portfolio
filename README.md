# 📊 Data Science Portfolio

> **Author**: Yuvraj  
> **Role**: Data Scientist  
> **Contact**: [www.linkedin.com/in/yuv2819] | [https://github.com/yuv2819-cmyk] | [Yuv2819@gmail.com

---

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Welcome to my data science portfolio! This repository contains 5 industry-ready projects demonstrating various machine learning techniques and business applications.

> **⚡ Quick Start**: Jump to [Getting Started Guide](./GETTING_STARTED.md) | View [Project 1 (Fully Implemented)](./customer-churn-prediction/)

---

## 🎯 Projects Overview

### 1. Customer Churn Prediction
**Type**: Binary Classification | **Domain**: Telecommunications

Predicts customer churn using multiple ML algorithms (Logistic Regression, Random Forest, XGBoost). Includes SMOTE for class imbalance, SHAP for interpretability, and ROI analysis.

- **Best Model**: XGBoost (88% ROC-AUC)
- **Key Finding**: Month-to-month contracts have 3x higher churn rate
- **Business Impact**: $250K net benefit through targeted retention

[📁 View Project](./customer-churn-prediction/)

---

### 2. Real Estate Price Prediction
**Type**: Regression | **Domain**: Real Estate

Predicts house prices using property features and location data. Implements ensemble methods and stacking for optimal performance.

- **Best Model**: Stacking Ensemble (R² = 0.88)
- **Key Finding**: Square footage explains 40% of price variation
- **Use Case**: Automated property valuation for buyers/sellers

[📁 View Project](./real-estate-price-prediction/)

---

### 3. Product Review Sentiment Analysis
**Type**: NLP Classification | **Domain**: E-commerce

Analyzes customer sentiment from product reviews using both traditional ML (TF-IDF) and deep learning (LSTM) approaches.

- **Best Model**: LSTM (92% accuracy)
- **Key Finding**: 85% of negative reviews mention specific product defects
- **Use Case**: Automated review monitoring and quality insights

[📁 View Project](./sentiment-analysis/)

---

### 4. Customer Segmentation
**Type**: Unsupervised Learning | **Domain**: Retail

Segments customers using clustering algorithms (K-Means, Hierarchical, DBSCAN) with RFM analysis for targeted marketing.

- **Best Method**: K-Means with 5 clusters
- **Key Finding**: "VIP" segment (12%) generates 45% of revenue
- **Use Case**: Personalized marketing campaigns

[📁 View Project](./customer-segmentation/)

---

### 5. Sales Forecasting
**Type**: Time Series | **Domain**: Retail

Forecasts sales using traditional (ARIMA, SARIMA) and modern (Prophet, LSTM) time series methods.

- **Best Model**: Prophet (MAPE = 6.2%)
- **Key Finding**: 35% YoY growth with strong holiday seasonality
- **Use Case**: Inventory optimization and demand planning

[📁 View Project](./sales-forecasting/)

---

## 🛠️ Technical Skills Demonstrated

- **Languages**: Python
- **Data Analysis**: Pandas, NumPy, Statistical Analysis
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM
- **Deep Learning**: TensorFlow/Keras, LSTM Networks
- **NLP**: NLTK, SpaCy, TF-IDF, Word Embeddings
- **Time Series**: Statsmodels, Prophet, ARIMA/SARIMA
- **Model Interpretation**: SHAP, Feature Importance
- **Techniques**: Cross-validation, Hyperparameter tuning, Ensemble methods, Class imbalance handling

## 📈 Business Skills

- ROI and cost-benefit analysis
- A/B testing and experimental design
- Stakeholder communication
- Strategic recommendations
- KPI definition and tracking

## 🎓 Project Methodology

Each project follows industry best practices:

1. **Business Understanding**: Clear problem definition and success metrics
2. **Data Exploration**: Comprehensive EDA with visualizations
3. **Data Preparation**: Feature engineering and preprocessing
4. **Modeling**: Multiple algorithms with rigorous evaluation
5. **Evaluation**: Business-focused metrics and interpretation
6. **Deployment Considerations**: Production-ready code and documentation

## 📁 Repository Structure

```
portfolio/
├── customer-churn-prediction/
├── real-estate-price-prediction/
├── sentiment-analysis/
├── customer-segmentation/
└── sales-forecasting/
```

Each project contains:
- `notebooks/` - Jupyter notebooks with analysis
- `data/` - Raw and processed datasets
- `models/` - Trained model files
- `visualizations/` - Generated plots and charts
- `README.md` - Project documentation
- `requirements.txt` - Dependencies

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.9 or higher
```

### Installation
```bash
# Clone the repository
cd <project-folder>

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Running Projects
Each project can be run independently by executing the notebooks in numerical order (01, 02, 03).

## 📊 Results Summary

| Project | Model Type | Best Performance | Business Value |
|---------|-----------|------------------|----------------|
| Churn Prediction | XGBoost | 88% ROC-AUC | $250K savings |
| House Prices | Stacking | R² = 0.88 | ±$22K accuracy |
| Sentiment Analysis | LSTM | 92% accuracy | Real-time monitoring |
| Customer Segments | K-Means | 5 segments | 3x campaign ROI |
| Sales Forecasting | Prophet | 6.2% MAPE | Optimized inventory |

## 💡 Key Insights Across Projects

1. **Feature Engineering**: Drives 10-20% performance improvement
2. **Ensemble Methods**: Consistently outperform single models
3. **Domain Knowledge**: Essential for meaningful feature creation
4. **Business Context**: Metrics must align with business objectives
5. **Interpretability**: Critical for stakeholder trust and adoption

## 📬 Contact

Feel free to explore the projects and reach out with any questions!

---

## 📚 Additional Resources

- **[Getting Started Guide](./GETTING_STARTED.md)** - How to run and explore projects
- **[Setup & Deployment](./SETUP_AND_DEPLOYMENT.md)** - Git setup, deployment options, demo script
- **[Interview Prep](./INTERVIEW_PREP.md)** - Complete checklist and Q&A preparation

---

**Note**: All projects use synthetic data generated to demonstrate analytical capabilities and real-world business scenarios.

---
*Last Updated: February 2026*
