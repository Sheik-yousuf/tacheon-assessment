# Cryptocurrency Data Pipeline

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and the CoinGecko API.

The objective is to automate data collection, transformation, and storage so that external data can be analyzed efficiently.

---

# Architecture

CoinGecko API
↓
fetch_data.py
↓
transform_data.py
↓
main.py
↓
CSV Export
↓
BigQuery
↓
SQL Analysis

---

# Why CoinGecko?

I selected the CoinGecko API because:

- No API key required
- Structured JSON responses
- Reliable cryptocurrency market data
- Suitable for transformation and analytics

---

# Technologies Used

- Python
- Requests
- Pandas
- Google BigQuery
- SQL

---

# Pipeline Components

## 1. Data Extraction

Data is fetched from the CoinGecko API using the Requests library.

Features:

- Error handling
- Timeout configuration
- Logging

---

## 2. Data Transformation

Raw JSON data is transformed into a Pandas DataFrame.

Operations include:

- Field selection
- Data cleaning
- Null handling
- Analytical enrichment

---

## 3. Derived Field

A custom field called `trend` was created.

Logic:

- Bullish → Price change > 5%
- Bearish → Price change < -5%
- Stable → Between -5% and 5%
- Unknown → Missing values

This provides additional analytical value beyond the raw API response.

---

## 4. Data Storage

The transformed data is:

- Exported as CSV
- Loaded into Google BigQuery

Dataset:

crypto_pipeline

Table:

crypto_market_data

---

# Running the Pipeline

Install dependencies:

```bash
pip install -r requirements.txt