import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)

def clean_data(df):

    # Drop rows with missing values
    df.dropna(subset=['ID', 'Restaurant', 'Price', 'Avg ratings', 'Total ratings'], inplace=True)
    
    # Remove duplicate rows
    df.drop_duplicates(subset=['ID', 'Area', 'Restaurant'], inplace=True)


    # Replace NaN in multiple columns with different fill values
    fillna_values = {
        'Avg ratings': 0,
        'Total ratings': 0
    }

    df.fillna(value=fillna_values, inplace=True)

    # Remove rows with invalid or unreasonable data (e.g., Price <= 0)
    df = df[df['Price'] > 0]

    return df
    
    