from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from datetime import datetime

POSTGRES_URL = "postgresql://postgres:2552085124rR!@localhost:5432/CoinDatabase"

if __name__ == "__main__":
    try:
        # Extract
        raw_data = extract_data()
        
        # Transform
        transformed_data = transform_data(raw_data)
        
        # Load
        load_data(transformed_data, POSTGRES_URL)
        
        print(f"ETL Process Completed at {datetime.now()}")
        
    except Exception as e:
        print(f"ETL Failed: {str(e)}")
