import os
import numpy as np
import pandas as pd


def load_datasets(data_dir="data"):
    ratings_path = os.path.join(data_dir, "ratings.csv")
    items_path = os.path.join(data_dir, "items.csv")

    ratings = pd.read_csv(ratings_path)
    items = pd.read_csv(items_path)
    return ratings, items


def create_user_item_matrix(ratings):
    # دستور پیاده‌سازی ماتریس پیوت تدریس‌شده در اسلاید جلسه ۳
    matrix = ratings.pivot(index="user_id", columns="item_id", values="rating")
    return matrix


def split_train_test(ratings, test_ratio=0.2, random_seed=42):
    rng = np.random.default_rng(random_seed)
    shuffled_indices = rng.permutation(len(ratings))
    test_size = int(len(ratings) * test_ratio)

    test_idx = shuffled_indices[:test_size]
    train_idx = shuffled_indices[test_size:]

    train_df = ratings.iloc[train_idx].copy().reset_index(drop=True)
    test_df = ratings.iloc[test_idx].copy().reset_index(drop=True)

    return train_df, test_df


def compute_statistics(ratings, items, matrix):
    num_users = ratings["user_id"].nunique()
    num_items = items["item_id"].nunique()
    num_ratings = len(ratings)
    total_possible = num_users * num_items
    sparsity = (1.0 - (num_ratings / total_possible)) * 100

    return {
        "کاربران": num_users,
        "اقلام": num_items,
        "تعداد کل امتیازها": num_ratings,
        "کمترین امتیاز": ratings["rating"].min(),
        "بیشترین امتیاز": ratings["rating"].max(),
        "میانگین امتیاز": round(ratings["rating"].mean(), 2),
        "درصد پراکندگی (Sparsity)": f"{round(sparsity, 2)}%",
    }


def main():
    print("=== اجرای پیش‌پردازش داده‌های گام دوم ===")
    ratings, items = load_datasets()

    matrix = create_user_item_matrix(ratings)
    print("\nماتریس کاربر-آیتم:")
    print(matrix.fillna(0))

    train_df, test_df = split_train_test(ratings, test_ratio=0.2)
    print(f"\nتعداد داده‌های آموزش: {len(train_df)}")
    print(f"تعداد داده‌های آزمون: {len(test_df)}")

    os.makedirs("data/processed", exist_ok=True)
    train_df.to_csv("data/processed/train.csv", index=False)
    test_df.to_csv("data/processed/test.csv", index=False)
    matrix.to_csv("data/processed/user_item_matrix.csv")

    stats = compute_statistics(ratings, items, matrix)
    print("\nآمار کلیدی:")
    for k, v in stats.items():
        print(f" - {k}: {v}")

    print("\n[OK] تمام فایل‌ها در پوشه data/processed ذخیره شدند.")


if __name__ == "__main__":
    main()