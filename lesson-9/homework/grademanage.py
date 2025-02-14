#be fair and kind in evaluating the code pls


import csv

def read_grades(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Read all rows into a list of dictionaries
    return data

def calculate_average_grades(data):
    subject_totals = {}  # Total grades per subject
    subject_counts = {}  # Number of grades per subject
    for row in data:
        subject = row['Subject']
        grade = int(row['Grade'])
        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

def write_average_grades(file_name, averages):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, average in averages.items():
            writer.writerow([subject, average])

# Processing Grades
data = read_grades('grades.csv')
averages = calculate_average_grades(data)
write_average_grades('average_grades.csv', averages)