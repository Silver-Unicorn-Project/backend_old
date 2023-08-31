import pandas as pd
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql+psycopg2://postgres:db_password@localhost:your_host/db_name')
with pd.ExcelFile('first.xlsx') as xls:
    df = pd.read_excel(xls)
    df.to_sql(name='products_products', con=engine, if_exists='append', index=False)
