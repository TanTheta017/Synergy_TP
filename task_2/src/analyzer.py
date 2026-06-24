import csv
import json
import os

def read_submissions(file_path: str) -> list:
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def get_submitted_students(data: list) -> list:
    return [row for row in data if row["submitted"] == "yes"]

def calculate_average_score(data: list) -> float:
    submitted = get_submitted_students(data)

    if not submitted:
        return 0

    total = sum(int(row["score"]) for row in submitted)
    return round(total / len(submitted), 2)

def get_domain_wise_average(data: list) -> dict:
    domains = {}

    for row in data:
        if row["submitted"] == "yes":
            domain = row["domain"]

            if domain not in domains:
                domains[domain] = []

            domains[domain].append(int(row["score"]))

    return {
        domain: round(sum(scores) / len(scores), 2)
        for domain, scores in domains.items()
    }

def get_missing_submissions(data: list) -> list:
    return [
        row["name"]
        for row in data
        if row["submitted"] == "no"
    ]

def write_summary(summary: dict, output_file: str) -> None:
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as file:
        json.dump(summary, file, indent=4)