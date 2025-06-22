# imports
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# define input and outputs path
RAW_DATA_PATH = "data/raw/commands.csv"
PROCESSED_DIR = "data/processed"
TRAIN_PATH = os.path.join(PROCESSED_DIR, "train.csv")
TEST_PATH = os.path.join(PROCESSED_DIR, "test.csv")

# define function to load and split the dataset
def load_and_split_data():
    # Load raw dataset
    df = pd.read_csv(RAW_DATA_PATH)
    print("Raw data loaded!")
    print(df)

    # shuffle and split dataset into training(80%) and test(20%) set
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Check if processed folder exists
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Save train and test sets to processed folder
    train_df.to_csv(TRAIN_PATH, index=False)
    test_df.to_csv(TEST_PATH, index=False)

    print(f"Training set saved to : {TRAIN_PATH}")
    print(f"Test set saved to : {TEST_PATH}")

if __name__ == "__main__":
    load_and_split_data()




