import statistics

# List of universities with their student count and tuition fees
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    """Extracts student enrollments and tuition fees from university data."""
    students = [uni[1] for uni in universities]
    tuition_fees = [uni[2] for uni in universities]
    return students, tuition_fees

def mean(values):
    """Calculates the mean (average) of a list of numbers."""
    return round(statistics.mean(values), 2)

def median(values):
    """Calculates the median of a list of numbers."""
    return round(statistics.median(values), 2)

def main():
    # Get student enrollments and tuition fees
    students, tuition_fees = enrollment_stats(universities)

    # Compute totals
    total_students = sum(students)
    total_tuition = sum(tuition_fees)

    # Compute mean and median values
    student_mean = mean(students)
    student_median = median(students)
    tuition_mean = mean(tuition_fees)
    tuition_median = median(tuition_fees)

    # Print formatted output
    print("*" * 30)
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}\n")
    print(f"Student mean: {student_mean:,}")
    print(f"Student median: {student_median:,}\n")
    print(f"Tuition mean: $ {tuition_mean:,}")
    print(f"Tuition median: $ {tuition_median:,}")
    print("*" * 30)