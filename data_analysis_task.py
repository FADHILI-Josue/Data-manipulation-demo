import pandas as pd
import requests

USERS_API = "http://127.0.0.1:8000/api/users"
PRODUCTS_API = "http://127.0.0.1:8000/api/products"

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {api_url}. Status code: {response.status_code}")

# Task 1: Return 500,000 rows of data
def get_full_dataset():
    print("Fetching users dataset...")
    users = fetch_data(USERS_API)
    print("Fetching products dataset...")
    products = fetch_data(PRODUCTS_API)

    users_df = pd.DataFrame(users)
    products_df = pd.DataFrame(products)

    return users_df, products_df

# Task 2: Describe the dataset
def describe_dataset(df, dataset_name):
    print(f"\n--- Description of {dataset_name} Dataset ---")
    print(df.describe(include="all"))

# Task 3: Find and replace null values
def handle_null_values(df):
    print("\nHandling null values...")
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")
        elif pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("N/A")
    print("Null values handled.")
    return df

# Task 4: Perform basic data preprocessing
def preprocess_data(df):
    print("\nPerforming basic preprocessing...")
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    # Standardize column names (lowercase and replace spaces with underscores)
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    print("Basic preprocessing completed.")
    return df

# Task 5: Create new features
def create_features(users_df, products_df):
    print("\nCreating new features...")
    # Count of products owned by each user
    product_counts = products_df.groupby("owner_id").size().reset_index(name="product_count")
    users_df = users_df.merge(product_counts, left_on="id", right_on="owner_id", how="left")
    users_df["product_count"] = users_df["product_count"].fillna(0)

    # Average price of products owned by each user
    avg_prices = products_df.groupby("owner_id")["price"].mean().reset_index(name="avg_product_price")
    users_df = users_df.merge(avg_prices, left_on="id", right_on="owner_id", how="left")
    users_df["avg_product_price"] = users_df["avg_product_price"].fillna(0)

    print("New features created.")
    return users_df

# Main execution
if __name__ == "__main__":
    # Fetch datasets
    users_df, products_df = get_full_dataset()

    # Describe datasets
    describe_dataset(users_df, "Users")
    describe_dataset(products_df, "Products")

    # Handle null values
    users_df = handle_null_values(users_df)
    products_df = handle_null_values(products_df)

    # Perform basic preprocessing
    users_df = preprocess_data(users_df)
    products_df = preprocess_data(products_df)

    # Create features
    enriched_users_df = create_features(users_df, products_df)

    # Save the processed datasets to CSV
    users_df.to_csv("processed_users.csv", index=False)
    products_df.to_csv("processed_products.csv", index=False)
    enriched_users_df.to_csv("enriched_users.csv", index=False)

    print("\nData processing complete. Processed files saved as 'processed_users.csv', 'processed_products.csv', and 'enriched_users.csv'.")


    print("\n\n\n The shapes of Dataframes")
    print("Users dataset shape:", users_df.shape)
    print("Products dataset shape:", products_df.shape)
