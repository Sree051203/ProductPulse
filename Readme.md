🛒 ProductPulse – E-Commerce Sentiment & Inventory Insights

A Python-based ETL + NLP project for analyzing product reviews and forecasting stock needs.

Overview

ProductPulse is a data analytics project that processes e-commerce product and review data using an ETL pipeline, performs sentiment analysis using NLP, and predicts inventory shortages using simple machine learning models.
The final output is displayed through an interactive Streamlit dashboard.

🔧 Tech Stack

Python, Pandas, NumPy

NLP: VADER Sentiment Analyzer

ML: Linear Regression / Basic Forecasting

Visualization: Streamlit, Plotly

Storage: CSV files (no database needed)

📂 Project Structure
ProductPulse/
│── data/
│   ├── products.csv
│   ├── reviews.csv
│
│── src/
│   ├── extract.py
│   ├── transform.py
│   ├── sentiment.py
│   ├── forecast.py
│   ├── dashboard_app.py
│
│── output/
│   ├── sentiment_output.csv
│   ├── forecast_output.csv
│
│── README.md

✨ Features

🧹 ETL Pipeline (Extract → Transform → Load)

💬 Sentiment Analysis of customer reviews

📉 Stock Forecasting to predict low inventory

📊 Interactive Dashboard using Streamlit

🔍 Keyword Insights for negative reviews

📁 Runs completely offline using CSV files

▶️ Running the Project

Install dependencies:

pip install -r requirements.txt


Run sentiment analysis:

python src/sentiment.py


Run inventory forecast:

python src/forecast.py


Launch dashboard:

streamlit run src/dashboard_app.py

