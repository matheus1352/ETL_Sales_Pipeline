# ETL Sales Pipeline

This project is an ETL (Extract, Transform, Load) pipeline for processing sales data. It extracts data from different sources, transforms it, and loads it into a PostgreSQL database.

## Project Structure

- `main.py`: Main script to run the ETL process.
- `config.py`: Configuration file for database connection and file paths.
- `etl/`: Directory containing ETL scripts.
  - `extract.py`: Script to extract data.
  - `transform.py`: Script to transform data.
  - `load.py`: Script to load data.
- `data/`: Directory containing sample sales data in CSV and JSON formats.

## How to Run

1. Install the required packages:
pip install -r requirements.txt

2. Run the ETL process:
python main.py

## Requirements

- Python 3.6+
- PySpark
- psycopg2
- pandas