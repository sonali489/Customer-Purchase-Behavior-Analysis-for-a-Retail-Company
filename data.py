import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Generate Customers Data
customers = pd.DataFrame({
    'customer_id': range(1, 1001),
    'name': [fake.name() for _ in range(1000)],
    'email': [fake.email() for _ in range(1000)],
    'gender': [random.choice(['Male', 'Female']) for _ in range(1000)],
    'age': [random.randint(18, 70) for _ in range(1000)],
    'loyalty_status': [random.choice(['Gold', 'Silver', 'Bronze']) for _ in range(1000)],
    'signup_date': [fake.date_this_decade() for _ in range(1000)],
    'city': [fake.city() for _ in range(1000)],
    'state': [fake.state() for _ in range(1000)],
    'country': ['USA' for _ in range(1000)]
})

# Generate Products Data
products = pd.DataFrame({
    'product_id': range(1, 501),
    'product_name': [fake.word().capitalize() for _ in range(500)],
    'category': [random.choice(['Electronics', 'Clothing', 'Home', 'Beauty']) for _ in range(500)],
    'brand': [fake.company() for _ in range(500)],
    'price': [round(random.uniform(10, 500), 2) for _ in range(500)],
    'stock': [random.randint(0, 100) for _ in range(500)]
})

# Generate Stores Data
stores = pd.DataFrame({
    'store_id': range(1, 21),
    'store_name': [f'Store {i}' for i in range(1, 21)],
    'store_type': [random.choice(['Online', 'Physical']) for _ in range(20)],
    'location': [fake.city() for _ in range(20)],
    'manager_name': [fake.name() for _ in range(20)]
})

# Generate Promotions Data
promotions = pd.DataFrame({
    'promotion_id': range(1, 51),
    'promotion_name': [f'Promo {i}' for i in range(1, 51)],
    'start_date': [fake.date_this_year() for _ in range(50)],
    'end_date': [fake.date_this_year() for _ in range(50)],
    'promotion_type': [random.choice(['Discount', 'BOGO', 'Free Shipping']) for _ in range(50)]
})

# Generate Transactions Data
transactions = pd.DataFrame({
    'transaction_id': range(1, 5001),
    'customer_id': [random.randint(1, 1000) for _ in range(5000)],
    'product_id': [random.randint(1, 500) for _ in range(5000)],
    'store_id': [random.randint(1, 20) for _ in range(5000)],
    'date': [fake.date_this_year() for _ in range(5000)],
    'quantity': [random.randint(1, 5) for _ in range(5000)],
    'total_amount': [round(random.uniform(20, 1000), 2) for _ in range(5000)],
    'discount_amount': [round(random.uniform(0, 50), 2) for _ in range(5000)],
    'payment_method': [random.choice(['Credit Card', 'Cash', 'PayPal']) for _ in range(5000)],
    'promotion_id': [random.choice([None] + list(range(1, 51))) for _ in range(5000)]
})

# Save to CSV or Excel files
customers.to_csv('customers.csv', index=False)
products.to_csv('products.csv', index=False)
stores.to_csv('stores.csv', index=False)
promotions.to_csv('promotions.csv', index=False)
transactions.to_csv('transactions.csv', index=False)