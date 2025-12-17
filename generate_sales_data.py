import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2022-01-01", end="2024-12-31")
products = ["P101", "P102", "P103", "P104", "P105"]
stores = ["S1", "S2", "S3"]
categories = {
    "P101": "Electronics",
    "P102": "Electronics",
    "P103": "Grocery",
    "P104": "Fashion",
    "P105": "Fashion"
}

rows = []

for date in dates:
    for product in products:
        for store in stores:
            base_demand = np.random.randint(20, 120)

            price = np.random.uniform(20, 100)
            cost = price * np.random.uniform(0.6, 0.8)

            discount_pct = np.random.choice([0, 5, 10, 15, 20])
            is_promotion = 1 if discount_pct > 0 else 0
            is_holiday = np.random.choice([0, 1], p=[0.9, 0.1])

            inventory = np.random.randint(50, 500)
            competitor_price = price * np.random.uniform(0.9, 1.1)
            weather_temp = np.random.uniform(10, 40)

            seasonal_boost = 1 + 0.2 * (date.month in [10, 11, 12])
            promo_boost = 1 + 0.3 * is_promotion
            holiday_boost = 1 + 0.4 * is_holiday

            units_sold = int(
                base_demand
                * seasonal_boost
                * promo_boost
                * holiday_boost
                *  np.random.uniform(0.95, 1.05)
            )

            rows.append([
                date,
                product,
                store,
                categories[product],
                units_sold,
                round(price, 2),
                round(cost, 2),
                discount_pct,
                is_promotion,
                is_holiday,
                inventory,
                round(competitor_price, 2),
                round(weather_temp, 1),
                date.dayofweek,
                date.week,
                date.month
            ])

df = pd.DataFrame(rows, columns=[
    "date","product_id","store_id","category","units_sold",
    "price","cost","discount_pct","is_promotion","is_holiday",
    "inventory_level","competitor_price","weather_temp",
    "day_of_week","week_of_year","month"
])

df.to_csv("sales_data.csv", index=False)
print("sales_data.csv created with", len(df), "rows")

