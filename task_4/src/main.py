import sys

from clean_data import (
    load_data,
    inspect_data,
    generate_summary,
    save_summary,
    remove_duplicates,
    standardize_domains,
    clean_attendance,
    clean_scores,
    clean_study_hours,
    clean_height,
    clean_weight,
    clean_submitted,
    save_cleaned_data)

from validate_data import validate_cleaned_data

def main():
    if len(sys.argv) < 2:
        print("File used: main.py")
        return
    input_file = sys.argv[1]
    df = load_data(input_file)
    print("BEFORE CLEANING")
    inspect_data(df)
    summary_before = generate_summary(df)
    save_summary(summary_before, "task_4/output/summary_before.json")
    df = remove_duplicates(df)
    print("\nRows after removing duplicates:", len(df))
    df = standardize_domains(df)
    df = clean_attendance(df)
    df = clean_scores(df)
    df = clean_study_hours(df)
    df = clean_height(df)
    df = clean_weight(df)
    df = clean_submitted(df)
    summary_after = generate_summary(df)
    save_summary(summary_after, "task_4/output/summary_after.json")

    if validate_cleaned_data(df):
        save_cleaned_data(df,"task_4/output/cleaned_students.csv")
        
    print("\nCleaned dataset saved successfully!")
if __name__ == "__main__":
    main()