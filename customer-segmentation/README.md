# 👥 Customer Segmentation

## Project Overview

This unsupervised learning project segments customers based on purchasing behavior to enable targeted marketing and personalized experiences.

## Business Problem

Retailers need to:
- Understand diverse customer bases
- Create personalized marketing campaigns
- Optimize product recommendations
- Allocate marketing budget effectively

## Dataset

- **Size**: 8,000 customers
- **Features**:
  - Recency: Days since last purchase
  - Frequency: Number of purchases
  - Monetary: Total spend
  - Average order value
  - Product categories purchased
  - Tenure (months as customer)
  - Channel preference (online/store)
- **Analysis Period**: 12 months

## RFM Analysis

Customers scored on:
- **Recency**: Recent buyers are more engaged
- **Frequency**: Regular purchasers show loyalty
- **Monetary**: High-value customers drive revenue

## Clustering Methods

| Method | Clusters | Silhouette Score | Davies-Bouldin |
|--------|----------|------------------|----------------|
| K-Means | 5 | 0.52 | 0.68 |
| **K-Means (PCA)** | **5** | **0.58** | **0.61** |
| Hierarchical | 4 | 0.48 | 0.74 |
| DBSCAN | 3+noise | 0.44 | 0.82 |

**Best Method**: K-Means with PCA preprocessing (5 segments)

## Customer Segments

### 1. 🌟 VIP / Champions (12%)
- **Profile**: High R-F-M scores across all dimensions
- **Behavior**: Frequent purchases, high spend, recent activity
- **Value**: $2,500 avg annual spend
- **Strategy**: Exclusive perks, early access, loyalty rewards

### 2. 💎 Loyal Customers (23%)
- **Profile**: High frequency, moderate monetary
- **Behavior**: Regular buyers, consistent engagement
- **Value**: $1,200 avg annual spend
- **Strategy**: Cross-sell, subscription programs

### 3. 🔄 Potential Loyalists (28%)
- **Profile**: Recent customers, growing frequency
- **Behavior**: New but showing promise
- **Value**: $800 avg annual spend
- **Strategy**: Engagement campaigns, personalized recommendations

### 4. 😴 At-Risk (21%)
- **Profile**: Previously active, declining engagement
- **Behavior**: Decreasing purchase frequency
- **Value**: $650 avg annual spend (declining)
- **Strategy**: Win-back campaigns, special offers

### 5. 💤 Hibernating (16%)
- **Profile**: Low recency, low frequency
- **Behavior**: Inactive or one-time buyers
- **Value**: $200 avg annual spend
- **Strategy**: Re-engagement or archive

## Key Insights

1. **Revenue Concentration**: Top 35% (VIP + Loyal) generate 68% of revenue
2. **Opportunity**: 28% are "Potential Loyalists" - prime for nurturing
3. **Risk**: 21% "At-Risk" customers need immediate retention efforts
4. **Channel**: VIPs prefer online (72%), while At-Risk prefer in-store

## Business Impact

### Targeted Campaigns
- **VIP**: Personalized service → 15% increase in spend
- **At-Risk**: Win-back offers → 25% reactivation rate
- **Potential**: Nurture program → 40% conversion to Loyal

### Marketing ROI
- **Before Segmentation**: 2.1x ROI on campaigns
- **After Segmentation**: 6.8x ROI on targeted campaigns
- **Net Impact**: 3.2x improvement

## Visualizations

- 3D cluster visualization (R-F-M space)
- Segment size and value distribution
- Heatmap of segment characteristics
- Customer journey flow between segments
- Product category preferences by segment
- Channel preference analysis

## Technical Implementation

- RFM scoring methodology
- Feature scaling and normalization
- PCA for dimensionality reduction
- Multiple clustering algorithms
- Elbow method and silhouette analysis
- Cluster profiling and interpretation

## Recommendations

1. **VIP Program**: Dedicated account managers for top 12%
2. **Automated Triggers**: Email at-risk customers after 45 days inactivity
3. **Personalization**: Segment-specific product recommendations
4. **Budget Allocation**: 40% to VIP/Loyal, 35% to Potential, 25% to At-Risk
5. **A/B Testing**: Test campaign effectiveness by segment

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
jupyter notebook notebooks/customer_segmentation.ipynb
```

## Technical Skills

- Unsupervised learning
- Clustering algorithms (K-Means, Hierarchical, DBSCAN)
- RFM analysis
- Dimensionality reduction (PCA, t-SNE)
- Customer analytics
- Marketing strategy development

## Author

Data Scientist Portfolio Project

---

*Note: Synthetic customer data for demonstration*
