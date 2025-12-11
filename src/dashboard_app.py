print("=== Starting Dashboard ===")
import time
time.sleep(1)

import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="ProductPulse - EIST", layout="wide")

st.title("ProductPulse : E-Commerce Inventory & Sentiment Tracker (EIST-ETL)")

# Build path to outputs folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(os.path.dirname(BASE_DIR), "outputs")

cleaned_path = os.path.join(OUTPUT_DIR, "cleaned_reviews_with_sentiment.csv")
summary_path = os.path.join(OUTPUT_DIR, "category_summary.csv")

st.write("Looking for files in:", OUTPUT_DIR)

# Validate file existence
if not os.path.exists(cleaned_path) and not os.path.exists(summary_path):
    st.error("Output files not found. Please run `etl_sentiment.py` first.")
else:
    # Load files
    df = pd.read_csv(cleaned_path)
    summary = pd.read_csv(summary_path)

    # Show KPIs
    st.subheader("Key Performance Metrics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Reviews", len(df))
    with col2:
        st.metric("Positive Reviews %", f"{(df['sentiment']=='positive').mean()*100:.1f}%")
    with col3:
        st.metric("Neutral Reviews %", f"{(df['sentiment']=='neutral').mean()*100:.1f}%")
    with col4:
        st.metric("Negative Reviews %", f"{(df['sentiment']=='negative').mean()*100:.1f}%")

    st.divider()

    # Demand Score Chart
    st.subheader("Category-wise Demand Score")
    st.bar_chart(summary.set_index("Class Name")["avg_demand_score"])

    # Rating Chart
    st.subheader("Category-wise Average Rating")
    st.bar_chart(summary.set_index("Class Name")["avg_rating"])

    # Sentiment Dist
    st.subheader("Sentiment Distribution")
    st.bar_chart(df["sentiment"].value_counts())

    # Raw Data Preview
    st.subheader("Sample Data Preview")
    st.dataframe(df.head(50))
