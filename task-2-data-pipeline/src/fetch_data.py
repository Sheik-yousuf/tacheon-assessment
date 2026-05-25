import requests
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1,
    "sparkline": False
}


def fetch_crypto_data():
    try:
        logging.info("Fetching cryptocurrency market data...")

        response = requests.get(
            API_URL,
            params=PARAMS,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        logging.info(f"Successfully fetched {len(data)} records.")

        return data

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None


if __name__ == "__main__":
    crypto_data = fetch_crypto_data()

    if crypto_data:
        print(crypto_data[:2])