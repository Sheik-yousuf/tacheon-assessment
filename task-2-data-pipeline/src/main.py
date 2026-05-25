from fetch_data import fetch_crypto_data
from transform_data import transform_crypto_data


def main():

    raw_data = fetch_crypto_data()

    if raw_data:

        transformed_df = transform_crypto_data(raw_data)

        if transformed_df is not None:

            print("\nTransformed Data Preview:\n")
            print(transformed_df.head())


if __name__ == "__main__":
    main()