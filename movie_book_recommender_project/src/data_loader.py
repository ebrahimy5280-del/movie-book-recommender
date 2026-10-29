import pandas as pd
from pathlib import Path

# Create output folder
output_dir = Path("data")
output_dir.mkdir(exist_ok=True) 

# Sample data (fictional)
data = {
    "user_id": [
        1, 1, 1, 2, 2, 2, 3, 3, 3, 4,
        4, 4, 5, 5, 5, 6, 6, 6, 7, 7
    ],
    "item_id": [
        101, 102, 103, 101, 104, 105, 102, 103, 106, 101,
        105, 107, 102, 104, 106, 103, 105, 107, 101, 106
    ],
    "item_type": [
        "movie", "book", "movie", "book", "movie",
        "book", "movie", "book", "movie", "movie",
        "book", "movie", "book", "movie", "book",
        "movie", "book", "movie", "book", "movie"
    ],
    "rating": [
        5, 4, 3, 4, 5, 3, 4, 5, 2, 3,
        4, 5, 4, 2, 5, 5, 3, 4, 4, 5
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save raw data
df.to_csv(output_dir / "raw_data.csv", index=False)
print("Initial rows:", len(df))

# 1. Remove rows with missing essential values
df = df.dropna(subset=["user_id", "item_id", "rating"])

# 2. Convert ratings to numeric values
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df = df.dropna(subset=["rating"])

# Keep ratings between 1 and 5
df = df[(df["rating"] >= 1) & (df["rating"] <= 5)]

# 3. Remove duplicate user-item pairs
df = df.drop_duplicates(
    subset=["user_id", "item_id"],
    keep="first"
)

# 4. Sort and reset row indices
df = df.sort_values(
    by=["user_id", "item_id"]
).reset_index(drop=True)

# Save cleaned data
df.to_csv(output_dir / "cleaned_data.csv", index=False)

print("Rows after cleaning:", len(df))

# 5. Split data into training and testing sets
train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)

# Save train and test files
train_df.to_csv(output_dir / "train.csv", index=False)
test_df.to_csv(output_dir / "test.csv", index=False)

# 6. Validate the split
train_pairs = set(
    map(tuple, train_df[["user_id", "item_id"]].values)
)
test_pairs = set(
    map(tuple, test_df[["user_id", "item_id"]].values)
)

assert train_pairs.isdisjoint(test_pairs)

print("Training rows:", len(train_df))
print("Testing rows:", len(test_df))
print("Data preparation completed successfully!")
print("Output files are saved in the data folder.")
