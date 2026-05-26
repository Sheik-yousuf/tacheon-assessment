# ================================
# FILE: main.py
# PATH: task-2-data-pipeline/src/main.py
# ================================

from fetch_data import fetch_crypto_data
from transform_data import transform_crypto_data
from load_bigquery import load_to_bigquery

import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    # Create data directory automatically
    os.makedirs("task-2-data-pipeline/data", exist_ok=True)

    # Step 1: Fetch data
    raw_data = fetch_crypto_data()

    if raw_data:

        # Step 2: Transform data
        transformed_df = transform_crypto_data(raw_data)

        if transformed_df is not None:

            print("\nTransformed Data Preview:\n")

            print(transformed_df.head())

            # Step 3: Save CSV locally
            output_path = "task-2-data-pipeline/data/crypto_market_data.csv"

            transformed_df.to_csv(output_path, index=False)

            logging.info(f"CSV saved successfully to {output_path}")

            # Step 4: Upload to BigQuery
            load_to_bigquery(transformed_df)


if __name__ == "__main__":

    main()