# AI Data Validation Platform

## Overview

Modern data pipelines often fail silently due to issues like missing values, schema changes, or incomplete data loads. These problems can lead to incorrect analytics, flawed business decisions, and loss of trust in data systems.

This project focuses on solving that problem by building a lightweight data validation framework that performs automated quality checks on datasets as they move through a pipeline.

## Problem Statement

In real-world data workflows, data is constantly ingested, transformed, and consumed — but validation is often overlooked.

Common challenges include:

* Unexpected schema changes
* Missing or null values
* Duplicate or inconsistent records
* Mismatched row counts after transformation

Without validation, these issues can silently impact downstream systems.

## Why This Project

This project was built to simulate a real-world gap in data engineering — ensuring **data quality before consumption**.

Instead of focusing only on transformation or modeling, this project emphasizes:

* Data reliability
* Pipeline validation
* Production-like thinking

## Approach

The pipeline follows a modular structure:

1. **Data Ingestion**
   Load raw dataset

2. **Data Transformation**

   * Remove duplicates
   * Handle missing values

3. **Data Validation**

   * Row count validation
   * Schema consistency check
   * Null value detection

4. **Reporting**
   Generate pass/fail validation results

5. **Visualization (Streamlit UI)**
   Interactive dashboard to view processed data and validation insights

## Key Features

* Modular pipeline design
* Automated validation checks
* Streamlit-based dashboard
* Real-time validation reporting
* Production-oriented structure

## Tech Stack

* Python
* Pandas
* Streamlit
* Pytest

## Project Structure

```
data-validation-platform/
│
├── data/
├── src/
├── tests/
├── requirements.txt
├── README.md
```

## Running the Pipeline

```bash
python src/main.py
```

### Sample Execution Output

![Pipeline Output](../pipeline_run.png)

✔ Shows step-by-step pipeline execution
✔ Displays validation results (PASS / FAIL)
✔ Highlights data quality issues

## Streamlit Dashboard

Run:

```bash
streamlit run dashboard.py
```

### Dashboard View

![Dashboard](../dashboard.png.png)

✔ Displays processed dataset
✔ Shows validation status for each record
✔ Provides statistical summary
✔ Highlights null values


## Processed Data Example

![Processed Data](../cleaned_data.png)

✔ Validation status added per record
✔ Highlights failed validations
✔ Shows real-world data issues (nulls, duplicates)


## Validation Insights

From the sample run:

* ❌ Row Count Check → FAIL
* ✅ Schema Check → PASS
* ✅ Null Check → PASS

This demonstrates how the system detects inconsistencies in transformed data.


## Future Improvements

* Logging for pipeline monitoring
* Alert system for failures
* Integration with orchestration tools
* Database support (Postgres, etc.)
* Advanced validation rules


## Impact

This project demonstrates:

* Data pipeline design
* Data quality validation techniques
* Real-world problem solving
* Building reliable data systems


## Conclusion

Ensuring data quality is critical in modern data systems. This project highlights how automated validation can prevent silent failures and improve trust in data pipelines.

