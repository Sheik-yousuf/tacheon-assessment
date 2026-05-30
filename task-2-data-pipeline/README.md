# fetch-data
CoinGecko API
      ↓
fetch_data.py
      ↓
raw JSON data


Raw API Data
        ↓
Cleaned DataFrame
        ↓
Derived Insights

# Cryptocurrency Data Pipeline

## Project Overview

This project is a small ETL-style data pipeline built using Python and the CoinGecko public API.

The main goal of the project is to automate the process of collecting external data, transforming it into a cleaner analytical format, and preparing it for storage and reporting.

The pipeline was designed as part of the Tacheon Data & AI Product Engineer assessment.

---

# Why I Chose CoinGecko API

I selected the CoinGecko API because:

- it provides structured real-time market data
- it does not require an API key
- the JSON response is suitable for transformation and analysis
- cryptocurrency data allows interesting analytical fields to be derived easily

The API returns information such as:

- cryptocurrency name
- market cap
- price
- trading volume
- 24-hour price change

---

# Current Pipeline Flow
CoinGecko API
      ↓
fetch_data.py
      ↓
transform_data.py
      ↓
main.py
      ↓
CSV Output
      ↓
BigQuery
      ↓
SQL Analysis