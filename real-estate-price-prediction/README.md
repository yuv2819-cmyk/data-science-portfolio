# 🏠 Real Estate Price Prediction

## Project Overview

This project builds machine learning models to predict house prices based on property characteristics and location features. The analysis helps real estate professionals, buyers, and sellers make data-driven pricing decisions.

## Business Problem

Accurate price prediction enables:
- Fair pricing for sellers
- Investment opportunity identification for buyers
- Market trend analysis for real estate agents
- Property valuation for lenders and insurers

## Dataset

- **Size**: 5,000 property listings
- **Features**: 20+ attributes including:
  - **Property**: Square footage, bedrooms, bathrooms, lot size
  - **Location**: Neighborhood, proximity to amenities, school districts
  - **Condition**: Age, renovation status, overall quality
  - **Amenities**: Garage, pool, fireplace, AC
- **Target**: Sale price (continuous variable)

## Models

| Model | MAE | RMSE | R² Score |
|-------|-----|------|----------|
| Linear Regression | $32,450 | $45,230 | 0.78 |
| Ridge Regression | $31,890 | $44,120 | 0.79 |
| Lasso Regression | $32,100 | $44,560 | 0.78 |
| Random Forest | $25,670 | $36,890 | 0.85 |
| **Gradient Boosting** | **$23,120** | **$34,200** | **0.87** |
| **Stacking Ensemble** | **$22,540** | **$33,450** | **0.88** |

**Best Model**: Stacking Ensemble with R² = 0.88

## Key Insights

1. **Square Footage**: Most important predictor (40% importance
2. **Location**: Neighborhood and school district significantly impact price
3. **Quality**: Overall condition rating strongly correlates with price
4. **Age**: Properties 10-20 years old offer best value
5. **Amenities**: Pool and renovated kitchen add ~$25K-$35K to value

## Technical Skills

- Feature engineering (price per sqft, property age, location encoding)
- Polynomial features and interactions
- Residual analysis and diagnostics
- Ensemble methods (stacking, boosting)
- Geographic visualization

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run notebooks in order:
1. `01_eda.ipynb` - Data exploration and visualization
2. `02_preprocessing.ipynb` - Feature engineering and preparation
3. `03_modeling.ipynb` - Model training and evaluation

## Author

Data Scientist Portfolio Project
