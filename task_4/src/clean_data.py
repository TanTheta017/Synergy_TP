import pandas as pd
import json

def load_data(file_path: str):
    """Load the CSV file into a pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df

def inspect_data(df):
    """Display basic information about the dataset."""
    print("\nCOLUMNS")
    print(df.columns.tolist())

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    print("\nDUPLICATE ROWS")
    print(df.duplicated().sum())

    print("\nUNIQUE DOMAIN VALUES")
    print(df["domain"].unique())



def generate_summary(df):
    "Generate a summary of the dataset."
    summary = {
        "total_rows": int(len(df)),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": df.isnull().sum().to_dict(),
        "domains": df["domain"].unique().tolist()}
    return summary


def save_summary(summary, output_path):
    " Save summary as a JSON file."
    with open(output_path, "w") as file:
        json.dump(summary, file, indent=4)


def remove_duplicates(df):
   "Remove duplicate rows."
   df = df.drop_duplicates()
   return df

def standardize_domains(df):
    "Standardize all domain names."

    domain_mapping = {
        "ml": "ML",
        "ML": "ML",
        "MACHINE LEARNING": "ML",

        "web": "Web",
        "Web Dev": "Web",
        "web development": "Web",

        "electronics": "Electronics",
        "Electronics": "Electronics",

        "Mechanical": "Mechanical" }

    df["domain"] = df["domain"].replace(domain_mapping)

    print("\nSTANDARDIZED DOMAINS")
    print(df["domain"].unique())
    return df

def clean_attendance(df):
    "Clean attendance_percent column."
    df["attendance_percent"] = (
        df["attendance_percent"]
        .astype(str)
        .str.replace("%", "", regex=False) )

    df["attendance_percent"] = pd.to_numeric(
        df["attendance_percent"],
        errors="coerce" )

    median_attendance = df[
        (df["attendance_percent"] >= 0) &
        (df["attendance_percent"] <= 100)]["attendance_percent"].median()

    df["attendance_percent"] = df["attendance_percent"].fillna(median_attendance)

    df.loc[
        (df["attendance_percent"] < 0) |
        (df["attendance_percent"] > 100),
        "attendance_percent"
    ] = median_attendance

    print("\nCLEANED ATTENDANCE")
    print(df["attendance_percent"])
    return df

def clean_scores(df):
    " Clean the score column."
    score_mapping = {
        "nine": 9,
        "eight": 8,
        "seven": 7,
        "six": 6,
        "five": 5,
        "four": 4,
        "three": 3,
        "two": 2,
        "one": 1,
        "zero": 0}

    df["score"] = df["score"].replace(score_mapping)
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    median_score = df["score"].median()
    df["score"] = df["score"].fillna(median_score)
    print("\nCLEANED SCORES")
    print(df["score"])
    return df

def clean_study_hours(df):
    "Clean the study_hours column."
    hour_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10}
    df["study_hours"] = df["study_hours"].replace(hour_mapping)
    df["study_hours"] = pd.to_numeric(
        df["study_hours"],
        errors="coerce")
    median_hours = df["study_hours"].median()
    df["study_hours"] = df["study_hours"].fillna(median_hours)
    print("\nCLEANED STUDY HOURS")
    print(df["study_hours"])
    return df

def clean_height(df):
    "Convert height values to centimeters."
    def convert_height(value):
        if pd.isna(value):
            return None
        value = str(value).strip().lower()
        if "cm" in value:
            value = value.replace("cm", "").strip()
            return float(value)
        elif "m" in value:
            value = value.replace("m", "").strip()
            return float(value) * 100
        return None

    df["height_cm"] = df["height"].apply(convert_height)
    median_height = df["height_cm"].median()
    df["height_cm"] = df["height_cm"].fillna(median_height)
    print("\nCLEANED HEIGHT")
    print(df["height_cm"])
    return df

def clean_weight(df):
    "Convert weight values to kilograms."
    df["weight_kg"] = (
        df["weight"]
        .astype(str)
        .str.replace("kg", "", regex=False)
        .str.strip()
    )
    df["weight_kg"] = pd.to_numeric(
        df["weight_kg"],
        errors="coerce"
    )
    median_weight = df["weight_kg"].median()
    df["weight_kg"] = df["weight_kg"].fillna(median_weight)
    print("\nCLEANED WEIGHT")
    print(df["weight_kg"])
    return df

def clean_submitted(df):
    "Standardize submitted values to 'yes' or 'no'."
    mapping = {
        "yes": "yes",
        "Yes": "yes",
        "Y": "yes",
        "y": "yes",
        "no": "no",
        "No": "no",
        "N": "no",
        "n": "no" }
    df["submitted"] = df["submitted"].replace(mapping)
    print("\nCLEANED SUBMITTED")
    print(df["submitted"].unique())
    return df

def save_cleaned_data(df, output_path):
    "Save cleaned DataFrame to CSV."
    columns = [
        "student_id",
        "name",
        "domain",
        "attendance_percent",
        "score",
        "study_hours",
        "height_cm",
        "weight_kg",
        "submitted" ]
    df[columns].to_csv(output_path, index=False)
    return df