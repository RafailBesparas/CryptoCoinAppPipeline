# Project Title: Crypto Market ETL Pipeline – Real-time Cryptocurrency Data Monitor

# Project Description
This project automates the process of extracting live cryptocurrency data from the CoinGecko API, transforming it to fit analytical needs, and loading it into a PostgreSQL database.
The goal is to create a system that tracks cryptocurrency prices and volumes, similar to monitoring platforms like Coinbase.

# 🎯 Objectives:
1. Automate cryptocurrency data collection at regular intervals.
2. Clean and transform the data to ensure consistency and accuracy.
3. Store the transformed data in a PostgreSQL database for further analysis or reporting.
4. Build a scalable ETL process that can handle increasing amounts of data.

# Workflow
### Extract Phase (extract.py):
1. Fetch live cryptocurrency market data from the CoinGecko API.
2. Convert the API response (JSON) to a pandas DataFrame for easy manipulation.
3. Handle API errors gracefully to ensure system reliability.

## Transform Phase (transform.py):
1. Select essential fields such as price, market cap, and volume.
2. Convert timestamps to proper datetime formats.
3. Rename columns to align with database schema standards.

## Load Phase (load.py):
1. Use SQLAlchemy to connect to a PostgreSQL database.
2. Create or append the transformed data to a table (crypto_prices).
3. Handle connection issues or insertion errors to ensure data integrity.

# Technical Stack
1. Python – Main programming language for the ETL pipeline.
2. PostgreSQL – Database to store the transformed data.
3. SQLAlchemy – ORM for database connection and management.
4. pandas – Data manipulation and transformation.
5. requests – API data extraction.
