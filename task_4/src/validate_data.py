def validate_cleaned_data(df):
    "Validate the cleaned dataset."
    if df["student_id"].duplicated().any():
        print("Duplicate student IDs found!")
        return False
    if not df["attendance_percent"].between(0, 100).all():
        print("Invalid attendance values found!")
        return False
    valid_domains = ["ML", "Web", "Electronics", "Mechanical"]
    if not df["domain"].isin(valid_domains).all():
        print("Invalid domain names found!")
        return False
    if df["submitted"].isnull().any():
        print("Submitted column has missing values!")
        return False
    print("\nValidation Passed!")
    return True