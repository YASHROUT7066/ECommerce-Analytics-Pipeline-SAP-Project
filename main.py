import logging
from pathlib import Path

from scripts.ingest import ingest_data
from scripts.load import load_data
from scripts.transform import transform_data


def setup_logging() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_dir / "pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def run_pipeline() -> None:
    setup_logging()
    logging.info("Pipeline started")

    logging.info("Ingest step started")
    raw_df = ingest_data()
    logging.info("Ingest step completed")

    logging.info("Transform step started")
    cleaned_df = transform_data(raw_df)
    logging.info("Transform step completed")

    logging.info("Load step started")
    load_data(cleaned_df)
    logging.info("Load step completed")

    logging.info("Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
