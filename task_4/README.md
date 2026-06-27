# Task 4 - Data Cleaning and Validation

## About

In this task, I cleaned a messy student dataset using Python and Pandas. The program removes duplicate records, fixes inconsistent values, checks if the cleaned data is valid, and saves the final output along with summary reports.

## Folder Structure

```
task_4/
│
├── data/
│   └── messy_students.csv
│
├── output/
│   ├── cleaned_students.csv
│   ├── summary_before.json
│   └── summary_after.json
│
├── src/
│   ├── clean_data.py
│   ├── validate_data.py
│   └── main.py
│
└── README.md
```

## What the program does

- Reads the CSV file.
- Shows basic information about the dataset.
- Removes duplicate rows.
- Standardizes domain names.
- Cleans attendance values.
- Converts scores and study hours into numbers.
- Converts height to centimeters.
- Converts weight to kilograms.
- Standardizes submitted values to "yes" and "no".
- Creates summary reports before and after cleaning.
- Saves the cleaned dataset if it passes validation.

## Requirements

- Python 3
- Pandas

To install Pandas:

```bash
pip install pandas
```

## Running the program

Open the terminal in the project folder and run:

```bash
python task_4/src/main.py task_4/data/messy_students.csv
```

## Output

After the program finishes, the following files are created inside the `output` folder:

- `cleaned_students.csv`
- `summary_before.json`
- `summary_after.json`

## Author

Tanya Misra