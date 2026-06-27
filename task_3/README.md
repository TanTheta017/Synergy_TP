# Task 3 - Manual CSV Parser and Pandas Comparison

## Objective

The objective of this task is to manually read a CSV file using Python file handling and compare the results with a pandas-based implementation.

## Folder Structure

```
task_3/
│── README.md
│
├── data/
│   └── submissions.csv
│
├── output/
│   ├── manual_summary.json
│   ├── pandas_summary.json
│   └── comparison_report.md
│
└── src/
    ├── manual_parser.py
    ├── pandas_parser.py
    └── main.py
```

## Required Packages

- Python 3
- pandas

Install pandas using:

```bash
pip install pandas
```

## Setup Instructions

1. Open the Synergy_TP repository.
2. Install pandas.
3. Make sure `submissions.csv` is inside the `data` folder.

## Run Command

Run the following command from the repository root:

```bash
python task_3/src/main.py task_3/data/submissions.csv
```

## Expected Output Files

- manual_summary.json
- pandas_summary.json
- comparison_report.md

## Implementation

- `manual_parser.py` reads the CSV manually using Python file handling.
- `pandas_parser.py` performs the same analysis using pandas.
- `main.py` runs both parsers, saves the summaries, and generates the comparison report.