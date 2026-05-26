# ================================
# FILE: load_bigquery.py
# PATH: task-2-data-pipeline/src/load_bigquery.py
# ================================

from google.cloud import bigquery
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_to_bigquery(dataframe):

    try:

        logging.info("Connecting to BigQuery...")

        client = bigquery.Client()

        # REPLACE THIS WITH YOUR PROJECT ID
        table_id = "YOUR_PROJECT_ID.crypto_pipeline.crypto_market_data"

        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE"
        )

        logging.info("Uploading dataframe to BigQuery...")

        job = client.load_table_from_dataframe(
            dataframe,
            table_id,
            job_config=job_config
        )

        job.result()

        logging.info("BigQuery upload completed successfully.")

    except Exception as e:

        logging.error(f"BigQuery upload failed: {e}")