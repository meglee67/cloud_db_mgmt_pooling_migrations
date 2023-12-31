# Example code taken from https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/python_connectionExample.py
import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect
from flask import Flask, render_template
import pandas as pd

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)


def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)


# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM patients"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, db_engine)

sql_query2 = "SELECT * FROM insurance_info"  # Modify as per your table
df2 = execute_query_to_dataframe(sql_query2, db_engine)

app = Flask(__name__)

@app.route('/data')
def data(data=df, data2=df2):
    return render_template('data.html', data=data, data2=data2)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080
    )
