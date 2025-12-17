# Product Demand Prediction Using Machine Learning

## Project Overview
This project focuses on predicting product demand using historical sales data and
external influencing factors such as promotions, holidays, pricing, inventory,
competitor pricing, and seasonality. The objective is to build a realistic and
scalable machine learning solution that can support inventory planning and
demand forecasting decisions.

The project is implemented end-to-end using Python and follows a structured
machine learning workflow including feature engineering, model training,
evaluation, and visualization.

---

## Dataset Description
The dataset is a synthetic but realistic multi-product and multi-store sales
dataset generated programmatically to simulate real-world demand patterns.

Key characteristics:
- Daily sales data
- Multiple products and stores
- Promotions and holidays
- Pricing and discount information
- Inventory levels
- Competitor pricing
- Seasonal and temporal features

Target variable:
- units_sold (daily product demand)

---

## Technologies Used
Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
Jupyter Notebook  
Git and GitHub  

---

## Project Workflow
1. Generate a realistic sales dataset programmatically  
2. Perform data loading and preprocessing  
3. Engineer time-based, lag, and rolling window features  
4. Build an end-to-end machine learning pipeline using ColumnTransformer  
5. Train a Random Forest regression model  
6. Evaluate model performance using MAE and RMSE  
7. Visualize actual vs predicted demand and model errors  
8. Save outputs and version control the project using GitHub  

---

## Feature Engineering
The following advanced features were created:
- Lag features (previous day and previous week demand)
- Rolling averages (7-day, 14-day, 30-day)
- Price difference compared to competitor
- Profit margin
- Day of week, week of year, and month
- Promotion and holiday indicators

These features help capture temporal patterns and demand behavior.

---

## Model and Evaluation
Model used:
- RandomForestRegressor with an end-to-end preprocessing pipeline

Evaluation metrics:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Final results:
- Average demand: approximately 92 units
- MAE: approximately 30 units
- RMSE: approximately 37 units

This corresponds to roughly 33 percent error, which is realistic for noisy,
product-store-day level demand forecasting.

---

## Visualizations
The project includes the following visualizations:
- Actual vs Predicted demand scatter plot
- Prediction error distribution
- Demand trends over time for sample product-store combinations

These visualizations help validate model performance and interpret prediction
behavior.

---

## Business Use Case
This solution can be used to:
- Improve inventory planning
- Reduce overstocking and stockouts
- Support demand-driven pricing strategies
- Assist decision-makers with data-driven forecasts

---

## How to Run the Project
1. Clone the repository
```bash
git clone https://github.com/UjjwalPamecha/Product-Demand-Prediction.git
