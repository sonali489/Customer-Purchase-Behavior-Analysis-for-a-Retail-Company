from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

# Initialize Faker and random seed
fake = Faker()
Faker.seed(0)
random.seed(0)

# Function to generate random date between the given range
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate customer IDs from 1 to 400 which can be duplicated
def generate_cust_ids(num_records):
    return [random.randint(1, 400) for _ in range(num_records)]

# Function to generate sample data with Faker and some anomalies
def generate_data(num_records, data_type):
    start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-12-31", "%Y-%m-%d")

    cust_ids = generate_cust_ids(num_records)

    data = []
    for cust_id in cust_ids:
        date = random_date(start_date, end_date)
        age = random.randint(18, 70)
        gender = random.choice(['Male', 'Female'])
        item = random.choice(['Electronics', 'Clothing', 'Grocery', 'Accessories'])
        quantity = random.randint(1, 10)  # Number of items purchased
        amount = round(random.uniform(5, 5000), 2)
        discount = f"{random.randint(0, 100)}%"  # Discount shown as a percentage
        rating = random.randint(1, 5)
        transaction_id = fake.uuid4()
        location = random.choice(['New York', 'California', 'Florida', 'Texas', 'Boston'])

        # Introduce anomalies and outliers
        if random.random() < 0.05:  # 5% chance to create an anomaly
            age = random.choice([120, -5])  # Impossible age values
            amount = random.choice([10000, -100])  # Outlier amount
            discount = f"{random.choice([110, -10])}%"  # Invalid discount percentages
            location = random.choice(['Unknown', 'N/A', 'Invalid Location'])  # Anomalous location values

        data.append({
            'cust_id': cust_id,
            'date': date,
            'age': age,
            'gender': gender,
            'item': item,
            'quantity': quantity,
            'amount': amount,
            'discount': discount,
            'rating': rating,
            'transaction_id': transaction_id,
            'location': location
        })

    return data

# Generate data for each schema
online_store_data = generate_data(600, 'online_store')
pos_system_data = generate_data(800, 'pos_system')
loyalty_program_data = generate_data(400, 'loyalty_program')

# Create DataFrames for each schema
online_store_df = pd.DataFrame(online_store_data)
pos_system_df = pd.DataFrame(pos_system_data)
loyalty_program_df = pd.DataFrame(loyalty_program_data)

# Save the DataFrames as CSV files locally
online_store_df.to_csv("online_store_schema.csv", index=False)
pos_system_df.to_csv("pos_system_schema.csv", index=False)
loyalty_program_df.to_csv("loyalty_program_schema.csv", index=False)

# Display messages indicating where the files were saved
print("CSV files saved successfully!")
print("Files generated:")
print("1. online_store_schema.csv")
print("2. pos_system_schema.csv")
print("3. loyalty_program_schema.csv")
