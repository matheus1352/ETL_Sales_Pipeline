def transform_data(data):
    # Perform data cleaning and transformation
    data.dropna(inplace=True)
    data['total'] = data['quantity'] * data['price']
    return data
