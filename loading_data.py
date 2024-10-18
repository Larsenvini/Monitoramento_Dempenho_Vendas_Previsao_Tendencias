import pandas as pd
from sqlalchemy import create_engine

def load_data():
    # Load cleaned data from CSV
    df = pd.read_csv('vendas_clean.csv')

    # Load Data into PostgreSQL
    engine = create_engine('postgresql://viniciuslarsen:@localhost:5432/vendas_db')
    df.to_sql('vendas', engine, if_exists='replace', index=False)

    print("Data loaded into PostgreSQL successfully!")
