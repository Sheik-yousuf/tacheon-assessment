from google.cloud import bigquery
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_to_bigquery(dataframe):

    try:

        logging.info("Connecting to BigQuery...")

        # Explicitly pass project ID
        client = bigquery.Client(
            project="crypto-pipeline-project28003"
        )

        table_id = "crypto-pipeline-project28003.crypto_pipeline.crypto_market_data"

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