import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

# 1. Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "Womens Clothing E-Commerce Reviews.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 2. Load
df = pd.read_csv(DATA_PATH)

# 3. Keep only columns we need
cols = [
    "Clothing ID",
    "Age",
    "Title",
    "Review Text",
    "Rating",
    "Recommended IND",
    "Positive Feedback Count",
    "Division Name",
    "Department Name",
    "Class Name",
]
df = df[cols]

# 4. Drop rows without review text
df = df.dropna(subset=["Review Text"])

# 5. Fill missing titles with empty string
df["Title"] = df["Title"].fillna("")

# 6. Sentiment using VADER
sia = SentimentIntensityAnalyzer()
df["sentiment_score"] = df["Review Text"].astype(str).apply(
    lambda x: sia.polarity_scores(x)["compound"]
)

def label_sentiment(score: float) -> str:
    if score > 0.05:
        return "positive"
    elif score < -0.05:
        return "negative"
    return "neutral"

df["sentiment"] = df["sentiment_score"].apply(label_sentiment)

# 7. Demand score (simple heuristic)
df["demand_score"] = (
    df["Rating"].fillna(0) * 15
    + df["Positive Feedback Count"].fillna(0) * 10
    + df["Recommended IND"].fillna(0) * 50
)

# 8. Aggregate per Class Name (category)
category_summary = (
    df.groupby("Class Name")
    .agg(
        avg_rating=("Rating", "mean"),
        avg_demand_score=("demand_score", "mean"),
        total_reviews=("Review Text", "count"),
        positive_share=("sentiment", lambda x: (x == "positive").mean()),
    )
    .reset_index()
    .sort_values("avg_demand_score", ascending=False)
)

# 9. Save outputs
cleaned_path = os.path.join(OUTPUT_DIR, "cleaned_reviews_with_sentiment.csv")
summary_path = os.path.join(OUTPUT_DIR, "category_summary.csv")

df.to_csv(cleaned_path, index=False)
category_summary.to_csv(summary_path, index=False)

print("Saved:")
print(" -", cleaned_path)
print(" -", summary_path)
