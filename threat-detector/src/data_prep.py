# imports
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# define inputs and outputs
RAW_DATA_PATH = "data/raw/commands.csv"
PROCESSED_DATA_PATH = "data/processed"
TRAIN_DS = os.path.join(PROCESSED_DATA_PATH,"train.csv")
TEST_DS = os.path.join(PROCESSED_DATA_PATH, "test.csv")

# define the function for loading and split the dataset
def load_and_split():
    # Load the dataset
    df = pd.read_csv(RAW_DATA_PATH)
    print("Loaded raw data")
    print(df)

    # split the data into training(80%) and test(20%) set
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    # Check if folder exists ( processed folder )
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    # Save to processed folder ( train.csv and test.csv)
    train_df = pd.to_csv(TRAIN_DS, index=False)
    test_df = pd.to_csv(TEST_DS, index=False)

    print(f"Training set saved to : {TRAIN_DS}")
    print(f"Test set saved to : {TEST_DS}")

if __name__ == __main__:
    load_and_split()

