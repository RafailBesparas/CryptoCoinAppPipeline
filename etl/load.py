from sqlalchemy import create_engine

def load_data(df, db_url, table_name='crypto_prices'):
    print("Loading data into PostgreSQL Local Database")

    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print("Data successfully loaded.")
