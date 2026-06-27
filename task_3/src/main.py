import sys

from manual_parser import (
    read_csv_manual,
    convert_types,
    calculate_summary,
    write_json as write_manual_json,
)

from pandas_parser import (
    read_csv_pandas,
    calculate_summary_pandas,
    write_json as write_pandas_json,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <csv_file_path>")
        return

    csv_path = sys.argv[1]

    rows = read_csv_manual(csv_path)
    rows = convert_types(rows)
    manual_summary = calculate_summary(rows)

    write_manual_json(
        manual_summary,
        "task_3/output/manual_summary.json"
    )

    df = read_csv_pandas(csv_path)
    pandas_summary = calculate_summary_pandas(df)

    write_pandas_json(
        pandas_summary,
        "task_3/output/pandas_summary.json"
    )

    with open("task_3/output/comparison_report.md", "w") as file:
        file.write("# Comparison Report\n\n")

        if manual_summary == pandas_summary:
            file.write(
                "The manual parser and pandas parser produced identical results."
            )
        else:
            file.write(
                "The outputs are different."
            )

    print("Task 3 completed successfully!")


if __name__ == "__main__":
    main()