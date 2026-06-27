import pandas as pd
import matplotlib.pyplot as plt
def load_cleaned_data(file_path: str):
    return pd.read_csv(file_path)

def plot_domain_average_score(df, output_path: str):
    average_scores = df.groupby("domain")["score"].mean()
    plt.figure(figsize=(6, 4))
    plt.bar(average_scores.index, average_scores.values)
    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig(f"{output_path}/domain_average_score.png")
    plt.close()

def plot_attendance_vs_score(df, output_path: str):
    plt.figure(figsize=(6, 4))
    plt.scatter(df["attendance_percent"], df["score"])
    plt.title("Attendance vs Score")
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig(f"{output_path}/attendance_vs_score.png")
    plt.close()

def plot_submission_status_count(df, output_path: str):
    submission_counts = df["submitted"].value_counts()
    plt.figure(figsize=(6,4))
    plt.bar(submission_counts.index, submission_counts.values)
    plt.title("Submission Status Count")
    plt.xlabel("Submission Status")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(f"{output_path}/submission_status_count.png")
    plt.close()

def write_plot_summary(output_path: str):
    summary_file = f"{output_path}/plot_summary.md"
    with open(summary_file, "w") as file:
        file.write("# Plot Summary\n\n")
        file.write("## Domain Average Score\n")
        file.write("This bar chart shows the average score of students in each domain.\n")
        file.write("It helps compare the overall performance of different domains.\n\n")
        file.write("## Attendance vs Score\n")
        file.write("This scatter plot shows the relationship between attendance percentage and score.\n")
        file.write("Each point represents one student.\n\n")
        file.write("## Submission Status Count\n")
        file.write("This bar chart shows how many students submitted and did not submit the task.\n")
        file.write("It provides a quick overview of submission participation.\n")