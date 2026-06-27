import json
def read_csv_manual(file_path: str) -> list[dict]:
    rows = []
    with open(file_path, "r") as file:
        lines = file.readlines()
    if not lines:
        return rows
    headers = lines[0].strip().split(",")
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        values = line.split(",")
        if len(values) != len(headers):
            continue
        row = {}
        for i in range(len(headers)):
            row[headers[i]] = values[i]
        rows.append(row)
    return rows


def convert_types(rows: list[dict]) -> list[dict]:
    for row in rows:
        row["score"] = int(row["score"])
        row["submitted"] = row["submitted"].strip().lower()
    return rows


def calculate_summary(rows: list[dict]) -> dict:
    total_students = len(rows)
    submitted_students = [row for row in rows if row["submitted"] == "yes"]
    missing_students = [row for row in rows if row["submitted"] == "no"]
    average_score = (
        sum(row["score"] for row in rows) / total_students
        if total_students > 0
        else 0
    )
    highest_scorer = max(rows, key=lambda x: x["score"])
    lowest_submitted = min(submitted_students, key=lambda x: x["score"])
    domain_scores = {}
    for row in rows:
        domain = row["domain"]
        if domain not in domain_scores:
            domain_scores[domain] = []
        domain_scores[domain].append(row["score"])
    domain_average = {}
    for domain, scores in domain_scores.items():
        domain_average[domain] = sum(scores) / len(scores)
    summary = {
        "total_students": total_students,
        "submitted_students": len(submitted_students),
        "missing_submissions": len(missing_students),
        "average_score": round(average_score, 2),
        "highest_scorer": highest_scorer["name"],
        "lowest_submitted_scorer": lowest_submitted["name"],
        "domain_average_score": domain_average,
        "students_not_submitted": [
            row["name"] for row in missing_students
        ],
        "students_below_5": [
            row["name"] for row in rows if row["score"] < 5
        ],
    }
    return summary


def write_json(data: dict, output_path: str) -> None:
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)