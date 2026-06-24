import csv
import json
import os

def read_submissions(file_path):
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_submitted_students(data):
    submitted = []

    for row in data:
        if row["submitted"] == "yes":
            submitted.append(row)

    return submitted


def calculate_average_score(data):
    submitted = get_submitted_students(data)

    if len(submitted) == 0:
        return 0

    total = 0

    for row in submitted:
        total += int(row["score"])

    return round(total / len(submitted), 2)


def get_domain_wise_average(data):
    domains = {}

    for row in data:
        if row["submitted"] == "yes":
            domain = row["domain"]
            score = int(row["score"])

            if domain not in domains:
                domains[domain] = []

            domains[domain].append(score)

    averages = {}

    for domain in domains:
        scores = domains[domain]
        avg = sum(scores) / len(scores)
        averages[domain] = round(avg, 2)

    return averages


def get_missing_submissions(data):
    missing = []

    for row in data:
        if row["submitted"] == "no":
            missing.append(row["name"])

    return missing


def write_summary(summary, output_file):
    folder = os.path.dirname(output_file)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(output_file, "w") as file:
        json.dump(summary, file, indent=4)