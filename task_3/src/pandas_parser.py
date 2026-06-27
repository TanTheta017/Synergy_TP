import pandas as pd
import json

def read_csv_pandas(file_path: str):
    df = pd.read_csv(file_path)
    return df

def calculate_summary_pandas(df) -> dict:
    submitted_students = df[df["submitted"].str.lower() == "yes"]
    missing_students = df[df["submitted"].str.lower() == "no"]
    domain_average = (
        df.groupby("domain")["score"]
        .mean()
        .round(2)
        .to_dict()
    )
    summary = {
        "total_students": len(df),
        "submitted_students": len(submitted_students),
        "missing_submissions": len(missing_students),
        "average_score": round(df["score"].mean(), 2),
        "highest_scorer": df.loc[df["score"].idxmax(), "name"],
        "lowest_submitted_scorer": submitted_students.loc[
            submitted_students["score"].idxmin(), "name"
        ],
        "domain_average_score": domain_average,
        "students_not_submitted": missing_students["name"].tolist(),
        "students_below_5": df[df["score"] < 5]["name"].tolist()
    }
    return summary

def write_json(data: dict, output_path: str) -> None:
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)