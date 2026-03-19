# Data Utilities - Reusable Python Library for Data Engineering

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![PyPI](https://img.shields.io/badge/PyPI-Utilities-blue?style=flat-square)
![SQL](https://img.shields.io/badge/SQL-Queries-blue?style=flat-square)
![PySpark](https://img.shields.io/badge/PySpark-Transform-orange?style=flat-square)

A collection of reusable Python utilities designed for data engineering workflows. This library provides production-ready connectors, transformations, data validators, and automation scripts that accelerate ETL development and maintain consistent coding standards across teams.

---

## Features

- **Database Connectors**: Unified interface for PostgreSQL, MySQL, Snowflake, BigQuery, and Redshift
- **Data Transformations**: PySpark and Pandas-based transformation utilities with type safety
- **Data Validation**: Schema validation, null checks, and statistical profiling using Pandera
- **File Handlers**: S3, GCS, and local file I/O with automatic compression and partitioning
- **Query Templates**: Pre-built SQL templates for common data operations and aggregations
- **Logging & Monitoring**: Structured logging with CloudWatch/Stackdriver integration
- **CLI Tools**: Command-line utilities for quick data profiling and ETL testing

---

## Installation

```bash
pip install data-utilities
```

Or from source:
```bash
git clone https://github.com/saiteja996688/data-utilities
cd data-utilities
pip install -e .
```

---

## Project Structure

```
data-utilities/
├── src/
│   ├── connectors/
│   │   ├── __init__.py
│   │   ├── postgresql.py
│   │   ├── snowflake.py
│   │   ├── bigquery.py
│   │   └── redshift.py
│   ├── transformers/
│   │   ├── __init__.py
│   │   ├── spark_transforms.py
│   │   └── pandas_transforms.py
│   ├── validators/
│   │   ├── __init__.py
│   │   ├── schema_validator.py
│   │   └── quality_checks.py
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── s3_handler.py
│   │   └── gcs_handler.py
│   ├── queries/
│   │   ├── templates/
│   │   └── query_builder.py
│   └── utils/
│       ├── logging_utils.py
│       └── config_loader.py
├── tests/
│   ├── test_connectors/
│   ├── test_transforms/
│   └── test_validators/
├── examples/
│   └── usage_examples.ipynb
├── requirements.txt
├── setup.py
└── README.md
```

---

## Quick Start

### Database Connection
```python
from data_utilities.connectors import SnowflakeConnector

conn = SnowflakeConnector(
    account="your-account",
    database="PROD",
    warehouse="ETL_WH"
)
conn.execute_query("SELECT * FROM users LIMIT 10")
```

### Data Validation
```python
from data_utilities.validators import DataValidator

validator = DataValidator(df)
validator.check_nulls()
validator.validate_schema(expected_schema)
validator.run_quality_checks()
```

### PySpark Transformation
```python
from data_utilities.transformers import SparkTransforms

st = SparkTransforms(spark)
df_clean = st.remove_duplicates(df)
df_enriched = st.join_and_transform(df, lookup_df)
```

---

## Supported Technologies

- **Databases**: PostgreSQL, MySQL, Snowflake, BigQuery, Redshift, Oracle
- **Big Data**: Apache Spark, PySpark, Delta Lake
- **Cloud Storage**: AWS S3, Google Cloud Storage, Azure Blob
- **Data Formats**: Parquet, Avro, JSON, CSV, ORC, Delta
- **Orchestration**: Apache Airflow, Prefect, Dagster

---

## Running Tests

```bash
pytest tests/ -v --cov=src
```

---

## License

MIT License - feel free to use and modify for your projects.

---

_Built to accelerate data engineering development with reusable, tested utilities._
