# Python Data Analysis - Copilot Practice Project

Practice using GitHub Copilot for data science and analysis tasks with Python, pandas, and visualization libraries.

## Setup Instructions

### Option 1: Using VS Code Tasks (Recommended)
1. Open the workspace in VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
3. Type "Tasks: Run Task"
4. Select "Setup Python Data Analysis Environment"
5. Once setup is complete, run "Generate Sample Data"

### Option 2: Manual Setup
1. Create a virtual environment: `python3 -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Generate sample data: `cd sample-data && python generate_sample_data.py`
5. Start Jupyter: `jupyter notebook`

## Learning Objectives

- Practice data manipulation with Copilot
- Learn to write effective prompts for data analysis
- Understand visualization suggestions
- Practice with statistical analysis patterns

## Datasets Included

The `generate_sample_data.py` script creates realistic e-commerce datasets:

- `customers.csv` - Customer demographics, segments, and preferences (1,000 records)
- `products.csv` - Product catalog with categories, brands, and pricing (500 records)
- `orders.csv` - Order transactions with dates and customer info (5,000 records)
- `order_items.csv` - Detailed order line items with quantities and prices (~13,000 records)
- `website_analytics.csv` - Web traffic and user behavior data (10,000 records)
- `support_tickets.csv` - Customer service interactions and resolutions (1,500 records)

## Analysis Tasks

### Phase 1: Data Exploration
- [ ] Load and inspect datasets
- [ ] Handle missing values
- [ ] Basic descriptive statistics
- [ ] Data type conversions

### Phase 2: Data Analysis
- [ ] Sales trends over time
- [ ] Customer segmentation
- [ ] Product performance analysis
- [ ] Correlation analysis

### Phase 3: Visualization
- [ ] Sales dashboard
- [ ] Customer behavior charts
- [ ] Geographic analysis
- [ ] Interactive plots

## Copilot Practice Tips

1. Start with clear comments about your analysis goals
2. Specify the expected data format and structure
3. Mention the libraries you want to use
4. Include example outputs when helpful

## Example Prompts to Try

```python
# Function to analyze sales trends by month and product category
# Parameters: sales_df (DataFrame with columns: date, product_id, category, amount, quantity)
# Returns: DataFrame with monthly aggregations by category
# Should handle missing dates and calculate growth rates
import pandas as pd
import numpy as np

def analyze_sales_trends(sales_df: pd.DataFrame) -> pd.DataFrame:
    # Let Copilot implement the analysis
```

```python
# Create a comprehensive sales dashboard with multiple visualizations
# Include: monthly revenue trend, top products, category breakdown, geographic sales
# Use plotly for interactive charts
# Parameters: sales_df, customer_df, product_df
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_sales_dashboard(sales_df, customer_df, product_df):
    # Let Copilot create the dashboard
```
