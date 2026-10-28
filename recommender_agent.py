
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# تنظیمات شبیه‌سازی
# =========================

N_ITEMS = 20
STEPS = 50
RUNS = 100

GENRES = ["Action", "Sci-Fi", "Drama", "Fantasy", "Comedy"]

AGENT_TYPES = ["random", "reflex", "model"]

AGENT_NAMES = {
    "random": "Random Agent",
    "reflex": "Reflex Agent",
    "model": "Model-Based Agent"
}


# =========================
# شبیه‌سازی عامل پیشنهاددهنده
# =========================

def simulate(agent_type, seed):
    rng = np.random.default_rng(seed)

    # تولید ژانر آیتم‌ها
    item_genres = rng.choice(GENRES, size=N_ITEMS)

    # علایق فرضی کاربر
    user_favorites = {"Sci-Fi", "Drama"}

    # مدل ساده ترجیحات کاربر
    user_profile_model = {genre: 0 for genre in GENRES}

    score = 0.0
    last_feedback = None

    for step in range(STEPS):

        # -------------------------
        # عامل تصادفی
        # -------------------------
        if agent_type == "random":
            recommended_item = rng.integers(0, N_ITEMS)

        # -------------------------
        # عامل واکنشی
        # -------------------------
        elif agent_type == "reflex":
            if last_feedback and last_feedback["liked"]:

                matching_items = [
                    idx
                    for idx, genre in enumerate(item_genres)
                    if genre == last_feedback["genre"]
                ]

                if matching_items:
                    recommended_item = rng.choice(matching_items)
                else:
                    recommended_item = rng.integers(0, N_ITEMS)

            else:
                recommended_item = rng.integers(0, N_ITEMS)

        # -------------------------
        # عامل مبتنی بر مدل
        # -------------------------
        elif agent_type == "model":

            best_genre = max(
                user_profile_model,
                key=user_profile_model.get
            )

            matching_items = [
                idx
                for idx, genre in enumerate(item_genres)
                if genre == best_genre
            ]

            if (
                matching_items
                and user_profile_model[best_genre] > 0
            ):
                recommended_item = rng.choice(matching_items)
            else:
                recommended_item = rng.integers(0, N_ITEMS)

        else:
            raise ValueError(
                f"Unknown agent type: {agent_type}"
            )

        # -------------------------
        # دریافت بازخورد کاربر
        # -------------------------
        recommended_genre = item_genres[recommended_item]

        user_liked = recommended_genre in user_favorites

        if user_liked:
            score += 1.0

            if agent_type == "model":
                user_profile_model[recommended_genre] += 1

        else:
            score -= 0.2

            if agent_type == "model":
                user_profile_model[recommended_genre] = max(
                    0,
                    user_profile_model[recommended_genre] - 0.5
                )

        # ذخیره آخرین بازخورد
        last_feedback = {
            "genre": recommended_genre,
            "liked": user_liked
        }

    return score


# =========================
# اجرای آزمایش‌ها
# =========================

def run_experiments():
    rows = []

    print("=" * 60)
    print("Movie and Book Recommender Agent Simulation")
    print("=" * 60)

    print(f"Number of items: {N_ITEMS}")
    print(f"Steps per run: {STEPS}")
    print(f"Runs per agent: {RUNS}")
    print(f"Total simulations: {len(AGENT_TYPES) * RUNS}")
    print()

    for agent in AGENT_TYPES:
        print(f"Running {AGENT_NAMES[agent]}...")

        for seed in range(RUNS):
            final_score = simulate(
                agent_type=agent,
                seed=seed
            )

            rows.append({
                "agent": agent,
                "agent_name": AGENT_NAMES[agent],
                "seed": seed,
                "score": final_score
            })

    results_df = pd.DataFrame(rows)

    # ذخیره نتایج تک‌تک اجراها
    results_df.to_csv(
        "recommender_results.csv",
        index=False
    )

    # محاسبه آمار هر عامل
    summary_df = (
        results_df
        .groupby(["agent", "agent_name"])["score"]
        .agg(
            mean_score="mean",
            std_score="std",
            min_score="min",
            max_score="max"
        )
        .reset_index()
    )

    summary_df["std_score"] = summary_df["std_score"].fillna(0)

    summary_df.to_csv(
        "recommender_summary.csv",
        index=False
    )

    # نمایش خلاصه نتایج
    print()
    print("=" * 60)
    print("Experiment Results")
    print("=" * 60)

    print(
        summary_df[
            [
                "agent_name",
                "mean_score",
                "std_score",
                "min_score",
                "max_score"
            ]
        ].round(2).to_string(index=False)
    )

    print()
    print("Detailed results saved to: recommender_results.csv")
    print("Summary saved to: recommender_summary.csv")

    return results_df, summary_df


# =========================
# رسم نمودار مقایسه
# =========================

def plot_results(results_df, summary_df):

    # نمودار میانگین امتیاز عامل‌ها
    plt.figure(figsize=(10, 6))

    plt.bar(
        summary_df["agent_name"],
        summary_df["mean_score"],
        yerr=summary_df["std_score"],
        capsize=5
    )

    plt.title("Comparison of Recommender Agents")
    plt.xlabel("Agent Type")
    plt.ylabel("Mean Cumulative Score")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()

    plt.savefig(
        "recommender_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    # نمودار توزیع امتیازها
    plt.figure(figsize=(10, 6))

    score_groups = [
        results_df.loc[
            results_df["agent"] == agent,
            "score"
        ].values
        for agent in AGENT_TYPES
    ]

    plt.boxplot(
        score_groups,
        tick_labels=[
            AGENT_NAMES[agent]
            for agent in AGENT_TYPES
        ]
    )

    plt.title("Score Distribution by Agent")
    plt.xlabel("Agent Type")
    plt.ylabel("Cumulative Score")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()

    plt.savefig(
        "recommender_score_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    print("Charts saved:")
    print("- recommender_comparison.png")
    print("- recommender_score_distribution.png")


# =========================
# نقطه شروع برنامه
# =========================

if __name__ == "__main__":

    results_df, summary_df = run_experiments()

    plot_results(
        results_df,
        summary_df
    )

    print()
    print("Simulation completed successfully.")
