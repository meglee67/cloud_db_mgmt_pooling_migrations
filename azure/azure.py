# this code is copied and modified from https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/migrations/azure.py

"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey, BigInteger, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(15))

    insurance = relationship('InsuranceInfo', back_populates='patient')

class InsuranceInfo(Base):
    __tablename__ = 'insurance_info'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    insurance_provider = Column(String(200))
    insurance_id_number = Column(BigInteger, nullable=False)
    copay_amount = Column(Float, nullable=False)  
    deductible_amount = Column(Float) 

    patient = relationship('Patient', back_populates='insurance')


### Part 2 - initial sqlalchemy-engine to connect to db:

connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args)

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

### Running migrations 
# """ these steps are then performed in the terminal, outside of your python code

# 1. alembic init migrations
# ` alembic init migrations `

# 2. edit alembic.ini to point to your database
# ` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

# 3. edit env.py to point to your models
# `from db_schema import Base`
# `target_metadata = Base.metadata `

# 4. create a migration
# ` alembic revision --autogenerate -m "create tables" `

# 5. run the migration
# ` alembic upgrade head `

# in addition, you can run ` alembic history ` to see the history of migrations
# or you can run with the --sql flag to see the raw SQL that will be executed

# so it could be like:
# ` alembic upgrade head --sql `

# or if you then want to save it:
# ` alembic upgrade head --sql > migration.sql `

# 6. check the database

# 7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
# The downgrade command allows you to revert the database schema to a previous 
# migration version. Here's how you can use it:

# `alembic downgrade <target_revision>` 

# or if you want to roll back to the previous version, you can use the -1 flag:
# `alembic downgrade -1`