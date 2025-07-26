def display_recommendations(df):
    for _, row in df.iterrows():
        print(f"{row['product_name']} ({row['category']} - {row['brand']}) - ${row['price']}")
