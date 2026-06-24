import sys

from analyzer import (
    read_submissions,
    get_submitted_students,
    calculate_average_score,
    get_domain_wise_average,
    get_missing_submissions,
    write_summary,
)

def main():

    if len(sys.argv) != 3:
        print("Usage:")
        print("python main.py input.csv output.json")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_submissions(input_file)

    submitted = get_submitted_students(data)

    highest = max(submitted, key=lambda x: int(x["score"]))
    lowest = min(submitted, key=lambda x: int(x["score"]))

    summary = {
        "total_students": len(data),
        "submitted_students": len(submitted),
        "missing_submissions": len(get_missing_submissions(data)),
        "average_score": calculate_average_score(data),
        "highest_scorer": highest["name"],
        "lowest_scorer": lowest["name"],
        "domain_wise_average": get_domain_wise_average(data),
        "not_submitted": get_missing_submissions(data),
        "below_five": [
            row["name"]
            for row in submitted
            if int(row["score"]) < 5
        ]
    }

    write_summary(summary, output_file)

    print("Summary written!")

if __name__ == "__main__":
    main()