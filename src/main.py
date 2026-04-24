from ingest import load_data
from transform import clean_data
from validate import row_count_check, schema_check, null_check
from report import generate_report
from logger import log
from config import DATA_PATH


def main_pipeline():
    log("Pipeline started")

    # Load data
    source = load_data(DATA_PATH)
    log("Data loaded")

    # Transform data
    target = clean_data(source)
    log("Data cleaned")

    # Validation checks
    results = {
        "Row Count": row_count_check(source, target),
        "Schema": schema_check(target, list(source.columns)),
        "Null Check": null_check(target)
    }

    log("Validation completed")

    # Generate report
    generate_report(results)

    log("Pipeline finished successfully")


if __name__ == "__main__":
    main_pipeline()