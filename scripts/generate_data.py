import pandas as pd
import numpy as np
from faker import Faker
# faker for data
fake = Faker()

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
dates = pd.date_range(start="2020-01-01", end="2023-12-31", freq="B")  # Business days only

data = []
for stock in stocks:
    price = fake.random_int(50, 500)  # starting price
    for date in dates:
        # simulate random walk for price
        price += np.random.normal(0, 5)  # small daily change
        price = max(price, 1)  # ensure price > 0
        volume = fake.random_int(1000, 100000)
        data.append({
            "stock_id": stock,
            "date": date.strftime("%Y-%m-%d"),
            "price": round(price, 2),
            "volume": volume
        })

df = pd.DataFrame(data)
df.to_csv("data/stocks.csv", index=False)
print(f"Generated {len(df)} stock records in data/stocks.csv")
