import pandas as pd

# Create a New Column 'Rating Category' with function
def rating_category(avg_rating):
    if avg_rating >= 4.0:
        return 'High'
    elif avg_rating >= 3.0:
        return 'Medium'
    else:
        return 'Low'


def data_manipulation(df):

    # Sort ID Column (Ascending Order) but to do descending then change it to False.
    df.sort_values(by='ID', ascending=True, inplace=True)

    # Convert Delivery Time to Readable Format (e.g., "58 mins")
    df['Delivery time'] = df['Delivery time'].astype(str) + ' mins'

    # Replace specific values in a column
    df.loc[df['City'] == 'Mumbai', 'City'] = 'Bombay'

    # Convert 'Food type' column to lowercase
    df['Food type'] = df['Food type'].str.lower()

    # Normalize Address by removing extra whitespace and converting to title case
    df['Address'] = df['Address'].str.strip().str.title()

    # Extract the column you want to move
    column_to_move = df.pop('Area')
    # Re-insert the column at the desired position (last position in this case)
    df['Area'] = column_to_move

    # Extract the column you want to move
    column_to_move2 = df.pop('Food type')
    # Insert the column at the desired position (index 2 in this case)
    df.insert(2, 'Food type', column_to_move2)

    # Create a New Column 'Rating Category' with function
    df['Rating Category'] = df['Avg ratings'].apply(rating_category)

    # Calculate Total Ratings per Area
    total_ratings_per_area = df.groupby('Area')['Total ratings'].sum()
    df['Total Ratings per Area'] = df['Area'].map(total_ratings_per_area)

    return df



def cal_avg_price(df):
    return df['Price'].mean()

def cal_avg_ratings(df):
    return df['Avg ratings'].mean()

def cal_highest_rated_restaurants(df, num_restaurants=5):
    return df.nlargest(num_restaurants, 'Avg ratings')[['Restaurant', 'Avg ratings']]

def cal_popular_food_types(df):
    return df['Food type'].value_counts()

def cal_delivery_time_range(df):
    pass

def cal_avg_total_ratings_per_food_type(df):
    return df.groupby('Food type')['Total ratings'].mean()
    
def filter_high_rated_restaurants(df, min_avg_ratings):
    return df[df['Avg ratings'] >= min_avg_ratings]








