# this code is copied and modified from https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/basic/1_1_populate.py

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
from gcp import Patient, InsuranceInfo
import os
import random 
from dotenv import load_dotenv

load_dotenv()

## Database credentials 
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string and creating the engine 
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")
engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Creating a session to populate the data
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Adding 10 records to the Patient table

# Creating a function to return a correct format for the contact number 
def contact_number():
    # Generate random numbers for each part of the contact number
    p1 = str(random.randint(1, 999)).zfill(3)
    p2 = str(random.randint(0, 999)).zfill(3)
    p3 = str(random.randint(0, 9999)).zfill(4)

    # Format the phone number as "000-000-0000"
    format = f"{p1}-{p2}-{p3}"
    return format

for _ in range(10):
    patient = Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=100),  
        gender=random.choice(["Male", "Female"]),
        phone_number=phone_number()
    )
    session.add(patient)

insurance_providers = [
    "Empire Blue Cross Blue Shield",
    "Anthem Blue Cross Blue Shield",
    "Aetna",
    "Humana",
    "Cigna",
    "United"
]

for _ in range(10):
    insuranceinfo = InsuranceInfo(
        patient_id=session.query(Patient).order_by(func.rand()).first().id,
        insurance_provider=random.choice(insurance_providers),  # Randomly selects an insurance provider from the list
        insurance_id_number=fake.random_number(digits=10),
        copay_amount=random.uniform(30.0, 100.0),
        deductible_amount=random.uniform(500.0, 1000.0)
    )
    session.add(insuranceinfo)

# Commit the changes to the database
session.commit()

# Close the session
session.close()