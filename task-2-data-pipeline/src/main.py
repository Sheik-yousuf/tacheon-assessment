from fetch_data import fetch_crypto_data
from transform_data import transform_crypto_data
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    # Step 1: Fetch raw data
    raw_data = fetch_crypto_data()

    if raw_data:

        # Step 2: Transform data
        transformed_df = transform_crypto_data(raw_data)

        if transformed_df is not None:

            print("\nTransformed Data Preview:\n")

            print(transformed_df.head())

            # Step 3: Save transformed data locally
            output_path = "task-2-data-pipeline/data/crypto_market_data.csv"

            transformed_df.to_csv(output_path, index=False)

            logging.info(f"Data saved successfully to {output_path}")


if __name__ == "__main__":
    main()