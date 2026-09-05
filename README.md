# Data Science Portfolio

Five end-to-end projects on synthetic data: classification, regression, NLP, clustering, and forecasting.

Built to show the full loop — problem, EDA, models, interpretation, business takeaway — not just a leaderboard score.

**Author:** Yuvraj · [LinkedIn](https://www.linkedin.com/in/yuv2819) · [GitHub](https://github.com/yuv2819-cmyk) · [yuv2819@gmail.com](mailto:yuv2819@gmail.com)

All datasets here are synthetic. Metrics describe the demo, not a production client.

## Projects

| Project | Type | Best result on this data | Takeaway |
|---|---|---|---|
| [Customer churn](./customer-churn-prediction/) | Classification · telecom | XGBoost, 88% ROC-AUC | Month-to-month contracts churn ~3× more |
| [House prices](./real-estate-price-prediction/) | Regression | Stacking ensemble, R² 0.88 | Square footage explains ~40% of price |
| [Review sentiment](./sentiment-analysis/) | NLP | LSTM, 92% accuracy | Most negative reviews name a specific defect |
| [Customer segments](./customer-segmentation/) | Clustering · RFM | K-Means, 5 groups | ~12% “VIP” drives ~45% of revenue |
| [Sales forecast](./sales-forecasting/) | Time series | Prophet, 6.2% MAPE | Holiday seasonality on a 35% YoY trend |

Churn project also includes SMOTE, SHAP, and a simple ROI sketch.

## Stack used across the set

`Python` `pandas` `scikit-learn` `XGBoost` `TensorFlow/Keras` `NLTK` `Prophet` `SHAP` `matplotlib` `seaborn`

## Run a project

```bash
cd customer-churn-prediction
pip install -r requirements.txt
jupyter notebook
```

Notebooks are numbered `01`, `02`, `03` inside each folder.

## More

- [GETTING_STARTED.md](./GETTING_STARTED.md)
- [SETUP_AND_DEPLOYMENT.md](./SETUP_AND_DEPLOYMENT.md)
- [INTERVIEW_PREP.md](./INTERVIEW_PREP.md)
