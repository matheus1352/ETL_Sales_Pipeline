from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    # Extract data
    data = extract_data()
    
    # Transform data
    transformed_data = transform_data(data)
    
    # Load data
    load_data(transformed_data)

if __name__ == "__main__":
    main()
