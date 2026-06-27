# Task 5: Data Visualization using Matplotlib

## Objective

The aim of this task is to create simple visualizations from the cleaned dataset produced in Task 4. Using Matplotlib, different graphs are generated to better understand the data and identify patterns such as average scores, attendance trends, and submission status.

---

## Folder Structure

```
task_5/
│── README.md
│
├── output/
│   ├── domain_average_score.png
│   ├── attendance_vs_score.png
│   ├── submission_status_count.png
│   └── plot_summary.md
│
└── src/
    ├── visualize.py
    └── main.py
```

---

## Required Packages

- Python 3.x
- pandas
- matplotlib

---

## Setup Instructions

1. Clone the repository.
2. Open the project folder in your terminal.
3. Activate the virtual environment.
4. Install the required packages using:

```bash
pip install -r requirements.txt
```

If the packages are not already listed, install them manually:

```bash
pip install pandas matplotlib
```

---

## Run Command

Run the program from the root directory of the repository:

```bash
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

---

## Expected Output

After running the program successfully, the following files will be generated inside the `task_5/output` folder:

```
domain_average_score.png
attendance_vs_score.png
submission_status_count.png
plot_summary.md
```

---

## Implementation Overview

The program first loads the cleaned dataset created in Task 4 using Pandas. It then generates three different graphs using Matplotlib:

- A bar chart showing the average score for each domain.
- A scatter plot showing the relationship between attendance percentage and student scores.
- A bar chart showing the number of students who submitted and did not submit the task.

Finally, the program saves all the graphs as PNG files and creates a `plot_summary.md` file that briefly explains what each graph represents.