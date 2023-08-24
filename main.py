import pandas as pd


from scripts import data_processing, data_analysis



def main():
    data_file_path = 'swiggy.xlsx'    
    
    # Load data
    df = data_processing.load_data(data_file_path)
    
    # Clean Data
    data_processing.clean_data(df)


    # manipulated data
    manipulated_data = data_analysis.data_manipulation(df)

    
    # Perform analysis
    avg_price = data_analysis.cal_avg_price(df)
    avg_ratings = data_analysis.cal_avg_ratings(df)
    top_rated_restaurants = data_analysis.cal_highest_rated_restaurants(df)
    popular_food_types = data_analysis.cal_popular_food_types(df)
    avg_total_ratings_per_food_type = data_analysis.cal_avg_total_ratings_per_food_type(df)
    

    # Filter high-rated restaurants
    min_avg_ratings = 4.5
    high_rated_restaurants = data_analysis.filter_high_rated_restaurants(df, min_avg_ratings)
    
   

    # New destination file path
    destination_file_path = 'manipulated_swiggy_data.xlsx'

    with pd.ExcelWriter(destination_file_path) as writer:
        df.to_excel(writer, sheet_name='Original Data', index=False)
        high_rated_restaurants.to_excel(writer, sheet_name='High Rated Restaurants', index=False)
        manipulated_data.to_excel(writer, sheet_name='Manipulated Data', index=False)


    print(f"\nManipulated data saved to '{destination_file_path}'.")
    
    # Print insights
    print("\n")
    print(f"\nAvgerage Price: {avg_price:.2f}")
    print(f"\nAvgerage Ratings: {avg_ratings:.2f}")
    print("\nTop Rated Restaurants: ")
    print(top_rated_restaurants)
    print("\nPopular Food Types:")
    print(popular_food_types)
    print("\nAverage Total Ratings per Food Type:")
    print(avg_total_ratings_per_food_type)

    
if __name__ == "__main__":
    main()
    