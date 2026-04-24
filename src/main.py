from ingest import load_data
from transform import clean_data
from validate import row_count_check, schema_check, null_check
from report import generate_report
from logger import log

print("Starting pipeline...")

# Step 1: Load data
log("Pipeline started")
source = load_data("../data/raw.csv")
log("Data loaded")

# Step 2: Clean data
target = clean_data(source)
log("Data cleaned")

# Step 3: Validation checks
results = {
    "Row Count": row_count_check(source, target),
    "Schema": schema_check(target, list(source.columns)),
    "Null Check": null_check(target)
}
log("Validation completed")

# Step 4: Generate report
generate_report(results)

log("Pipeline finished successfully")