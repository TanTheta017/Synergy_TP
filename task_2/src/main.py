import sys
from analyzer import *

def main():

    if len(sys.argv) != 3:
        print("Usage: python main.py input.csv output.json")
        return

    data = read_submissions(sys.argv[1])

    submitted = get_submitted_students(data)

    summary = {
        "total_students": len(data),
        "submitted_students": len(submitted),
        "missing_submissions": len(get_missing_submissions(data)),
        "average_score": calculate_average_score(data),
        "highest_scorer": max(submitted, key=lambda x: int(x["score"]))["name"],
        "lowest_scorer": min(submitted, key=lambda x: int(x["score"]))["name"],
        "domain_wise_average": get_domain_wise_average(data),
        "not_submitted": get_missing_submissions(data),
        "below_five": [
            student["name"]
            for student in submitted
            if int(student["score"]) < 5
        ]
    }

    write_summary(summary, sys.argv[2])

    print("Summary written!")

if __name__ == "__main__":
    main()