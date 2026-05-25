import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def transform_crypto_data(raw_data):

    try:
        logging.info("Transforming cryptocurrency data...")

        transformed_data = []

        for coin in raw_data:

            price_change = coin.get("price_change_percentage_24h", 0)

            # Derived analytical field
            if price_change is None:
                trend = "Unknown"
            elif price_change > 5:
                trend = "Bullish"
            elif price_change < -5:
                trend = "Bearish"
            else:
                trend = "Stable"

            transformed_coin = {
                "coin_name": coin.get("name"),
                "symbol": coin.get("symbol"),
                "current_price": coin.get("current_price"),
                "market_cap": coin.get("market_cap"),
                "market_cap_rank": coin.get("market_cap_rank"),
                "total_volume": coin.get("total_volume"),
                "price_change_24h": price_change,
                "trend": trend
            }

            transformed_data.append(transformed_coin)

        df = pd.DataFrame(transformed_data)

        # Handle missing values
        df.fillna(0, inplace=True)

        logging.info("Data transformation completed successfully.")

        return df

    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        return None