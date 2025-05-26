from faker import Faker
import pandas as pd

fake = Faker()
data = [
    {
        "stock_id": fake.random_element(["AAPL", "GOOGL", "MSFT"]),
        "date": fake.date(),
        "price": fake.random_int(50, 500),
        "volume": fake.random_int(1000, 10000)
    }
    for _ in range(1000)
]
pd.DataFrame(data).to_csv("data/stocks.csv", index=False)
print("Generated 1000 stock records in data/stocks.csv")
