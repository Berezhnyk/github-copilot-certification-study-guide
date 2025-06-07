# Data Analysis Prompt Patterns for GitHub Copilot

## Overview
This guide contains proven prompt patterns specifically designed for data analysis tasks with GitHub Copilot. These patterns will help you get better, more contextual suggestions for your data science work.

## Table of Contents
1. [Data Loading Patterns](#data-loading-patterns)
2. [Exploratory Data Analysis Patterns](#exploratory-data-analysis-patterns)
3. [Statistical Analysis Patterns](#statistical-analysis-patterns)
4. [Machine Learning Patterns](#machine-learning-patterns)
5. [Visualization Patterns](#visualization-patterns)
6. [Performance Optimization Patterns](#performance-optimization-patterns)

## Data Loading Patterns

### Pattern 1: Context-Rich Data Loading
```python
# Load e-commerce customer data with 1000+ records
# Columns: customer_id, name, email, registration_date, age, segment (Bronze/Silver/Gold/Platinum)
# Handle missing values and convert dates to datetime
# Expected file: customers.csv with standard e-commerce customer attributes
customers_df = pd.read_csv('customers.csv')
```

### Pattern 2: Multi-Dataset Loading with Relationships
```python
# Load related e-commerce datasets for comprehensive analysis
# customers: customer demographics and segmentation
# orders: transaction data with customer_id foreign key
# products: product catalog with pricing and categories
# order_items: detailed line items linking orders to products
# Data integrity: all foreign keys should have matching records

def load_ecommerce_datasets():
    # Let Copilot implement robust data loading with validation
```

## Exploratory Data Analysis Patterns

### Pattern 3: Comprehensive Dataset Overview
```python
# Generate comprehensive data profiling report for e-commerce dataset
# Include: shape, dtypes, missing values %, unique counts, basic stats
# Identify potential data quality issues and relationships
# Output formatted summary with recommendations for next steps
# Dataset context: B2C e-commerce with customers, orders, products

def profile_ecommerce_data(df, dataset_name):
    # Let Copilot create detailed profiling function
```

### Pattern 4: Business-Specific EDA
```python
# Analyze customer purchase behavior patterns for e-commerce business
# Focus on: customer lifetime value, purchase frequency, seasonal trends
# Segment analysis: compare Bronze/Silver/Gold/Platinum customers
# Geographic insights: identify high-value regions
# Time-based patterns: monthly/quarterly revenue trends

def analyze_customer_behavior(customers_df, orders_df, order_items_df):
    # Let Copilot generate business-focused analysis
```

## Statistical Analysis Patterns

### Pattern 5: Hypothesis Testing with Context
```python
# Test hypothesis: Premium customers (Gold/Platinum) have significantly higher order values
# Use appropriate statistical test for the data distribution
# Include effect size calculation and practical significance
# Handle assumptions: normality, equal variance, sample size
# Report results with business interpretation

def test_premium_customer_hypothesis(customers_df, orders_df):
    # Let Copilot implement proper statistical testing
```

### Pattern 6: Correlation Analysis with Business Meaning
```python
# Analyze correlations between customer characteristics and business metrics
# Variables: age, registration_tenure, order_frequency, avg_order_value, support_tickets
# Use appropriate correlation method based on data types
# Filter out spurious correlations and focus on actionable insights
# Visualize with annotated heatmap showing business implications

def analyze_customer_correlations(merged_customer_data):
    # Let Copilot create meaningful correlation analysis
```

## Machine Learning Patterns

### Pattern 7: Customer Segmentation with Domain Knowledge
```python
# Perform customer segmentation using RFM analysis (Recency, Frequency, Monetary)
# Use K-means clustering with optimal number of clusters (elbow method)
# Features: days_since_last_purchase, total_orders, total_spent, avg_order_value
# Interpret clusters with business labels: Champions, Loyal Customers, At Risk, etc.
# Validate segments with business metrics and actionable recommendations

def segment_customers_rfm(customers_df, orders_df):
    # Let Copilot implement business-driven segmentation
```

### Pattern 8: Predictive Model with Feature Engineering
```python
# Build customer churn prediction model for e-commerce platform
# Features: purchase history, website engagement, support interactions, demographics
# Target: customers who haven't purchased in 90+ days (define churn threshold)
# Use ensemble methods: Random Forest, XGBoost, compare performance
# Include feature importance analysis and model interpretability
# Handle class imbalance and validate with business metrics

def build_churn_prediction_model(customers_df, orders_df, analytics_df, support_df):
    # Let Copilot create comprehensive ML pipeline
```

## Visualization Patterns

### Pattern 9: Business Dashboard Creation
```python
# Create executive dashboard for e-commerce business performance
# Include: revenue trends, customer acquisition, top products, geographic distribution
# Use plotly for interactivity: filters, drill-down capabilities, hover details
# Color scheme: professional blue/gray with accent colors for alerts
# Layout: 2x2 grid with clear titles and business context
# Export options: HTML, PNG for presentations

def create_executive_dashboard(customers_df, orders_df, products_df):
    # Let Copilot build professional interactive dashboard
```

### Pattern 10: Statistical Visualization with Annotations
```python
# Create cohort analysis visualization showing customer retention patterns
# X-axis: months since first purchase, Y-axis: cohort month
# Heatmap with retention percentages as values
# Add trend lines and statistical significance markers
# Include business insights as text annotations
# Professional styling with company brand colors

def visualize_cohort_analysis(cohort_data):
    # Let Copilot create publication-ready cohort heatmap
```

## Performance Optimization Patterns

### Pattern 11: Vectorized Operations
```python
# Optimize customer summary calculation using pandas vectorized operations
# Original approach uses slow iterrows(), target: 10x performance improvement
# Calculate: total_spent, order_count, avg_order_value, days_since_last_order
# Use groupby, agg, merge operations instead of loops
# Memory efficient for datasets with 100K+ customers
# Include timing comparison with original implementation

def optimize_customer_summary(customers_df, orders_df):
    # Let Copilot create high-performance vectorized solution
```

### Pattern 12: Memory-Efficient Large Dataset Processing
```python
# Process large e-commerce dataset (1M+ orders) with memory constraints
# Use chunking for file reading, optimize dtypes, avoid data copies
# Implement streaming aggregations for real-time metrics
# Memory usage should stay under 2GB throughout processing
# Include progress bars and memory monitoring
# Output: daily/weekly/monthly business summaries

def process_large_dataset_efficiently(filepath, chunk_size=10000):
    # Let Copilot implement memory-efficient processing
```

## Advanced Prompt Engineering Tips

### Tip 1: Layer Context Gradually
Start with basic context, then add business domain, then technical requirements:
```python
# Basic: "Analyze customer data"
# Better: "Analyze e-commerce customer segmentation"
# Best: "Analyze e-commerce customer segments (Bronze/Silver/Gold/Platinum) 
#       focusing on purchase behavior differences and revenue impact"
```

### Tip 2: Specify Expected Outputs
```python
# Return dictionary with segment_analysis results:
# {
#   'segment_summary': DataFrame with metrics by segment,
#   'statistical_tests': dict with p-values for segment differences,
#   'visualizations': list of matplotlib/plotly figures,
#   'recommendations': list of actionable business insights
# }
```

### Tip 3: Include Error Handling Context
```python
# Handle common data issues: missing customer_ids, negative order values,
# future dates, duplicate transactions
# Raise informative exceptions with suggested fixes
# Log data quality issues for monitoring
```

### Tip 4: Specify Libraries and Versions
```python
# Use pandas 2.0+ features, scikit-learn 1.3+, plotly 5.14+
# Prefer vectorized operations over loops
# Use type hints for better code documentation
```

### Tip 5: Business Context Over Technical Details
```python
# Focus on business impact: "identify customers at risk of churning"
# Rather than technical: "find customers with low purchase frequency"
# Include business thresholds: "customers with no purchase in 90+ days"
```

## Example Workflow: Complete Analysis

```python
# Complete e-commerce customer analysis workflow
# 1. Load and validate all datasets
# 2. Perform data quality assessment
# 3. Calculate key business metrics (CLV, churn risk, segment performance)
# 4. Generate statistical insights with hypothesis testing
# 5. Create predictive models for churn and CLV
# 6. Build interactive dashboard for stakeholders
# 7. Export automated reports with recommendations

def complete_customer_analysis():
    # Let Copilot orchestrate the entire analysis pipeline
```

This approach provides Copilot with rich context about your intentions, expected outputs, and business requirements, leading to more relevant and sophisticated suggestions.
