# 💬 Product Review Sentiment Analysis

## Project Overview

This NLP project analyzes customer product reviews to classify sentiment and extract actionable insights for product improvement and customer satisfaction monitoring.

## Business Problem

E-commerce companies need to:
- Monitor customer sentiment at scale
- Identify product issues quickly
- Prioritize customer feedback
- Automate review classification

## Dataset

- **Size**: 15,000 product reviews
- **Features**:
  - Review text (variable length)
  - Star rating (1-5)
  - Product category
  - Verified purchase status
  - Helpfulness votes
- **Target**: Sentiment (Positive, Neutral, Negative)
- **Distribution**: 60% positive, 25% neutral, 15% negative

## Approach

### 1. Text Preprocessing
- Lowercase conversion
- Remove special characters and URLs
- Tokenization and lemmatization
- Stop word removal
- Handle negations

### 2. Feature Extraction
- **TF-IDF**: Traditional approach
- **Word Embeddings**: Word2Vec, GloVe
- **Contextualized**: Pre-trained BERT representations

### 3. Models

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Naive Bayes (TF-IDF) | 0.84 | 0.82 | 0.84 | 0.83 |
| SVM (TF-IDF) | 0.87 | 0.86 | 0.87 | 0.86 |
| Random Forest (TF-IDF) | 0.85 | 0.84 | 0.85 | 0.84 |
| **LSTM (Word2Vec)** | **0.92** | **0.91** | **0.92** | **0.92** |
| BERT Fine-tuned | 0.94 | 0.93 | 0.94 | 0.93 |

**Best Model**: LSTM achieves 92% accuracy with efficient training time

## Key Insights

1. **Common Complaints**:
   - Quality issues: 45% of negative reviews
   - Shipping problems: 30% of negative reviews
   - Size/fit issues: 25% of negative reviews

2. **Positive Drivers**:
   - "Value for money" most common positive phrase
   - Fast shipping correlates with 4-5 star ratings
   - Product photos accuracy important

3. **Word Clouds**:
   - Negative: "disappointed", "poor quality", "waste money"
   - Positive: "love", "perfect", "recommend", "excellent"

4. **Aspect-Based Sentiment**:
   - Price: 75% positive sentiment
   - Quality: 65% positive sentiment
   - Service: 80% positive sentiment

## Technical Implementation

- **Preprocessing**: NLTK, SpaCy
- **Traditional ML**: Scikit-learn with TF-IDF
- **Deep Learning**: TensorFlow/Keras LSTM
- **Visualization**: Word clouds, n-gram analysis
- **Deployment Ready**: Saved tokenizer and model for real-time scoring

## Visualizations

- Sentiment distribution
- Word clouds (positive/negative)
- Bi-gram and tri-gram analysis
- Rating vs sentiment correlation
- Topic modeling visualization
- Confusion matrices
- ROC curves for multi-class

## Use Cases

1. **Automated Monitoring**: Flag negative reviews for immediate response
2. **Product Insights**: Identify recurring issues for product development
3. **Competitive Analysis**: Compare sentiment across product lines
4. **Customer Success**: Proactive outreach to dissatisfied customers

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

```bash
jupyter notebook notebooks/sentiment_analysis.ipynb
```

## Future Enhancements

- Real-time API for live review scoring
- Multi-language support
- Aspect-based sentiment extraction
- Trend analysis over time
- Integration with customer support systems

## Technical Skills

- Natural Language Processing (NLP)
- Text preprocessing and cleaning
- Feature extraction (TF-IDF, embeddings)
- Deep learning for NLP (LSTM, BERT)
- Multi-class classification
- Model deployment considerations

## Author

Data Scientist Portfolio Project

---

*Note: Synthetic reviews generated to demonstrate NLP capabilities*
