# Exercise 2: Data Processing
# Task: Analyze student grades and return statistics

# Function to analyze student grades
# Input: list of dictionaries with 'name', 'grade', 'subject' keys
# Output: dictionary with statistics (average, highest, lowest, pass_rate)
# Pass rate is percentage of grades >= 60
def analyze_student_grades(students):
    """
    Analyze a list of student records and calculate statistics.
    
    Args:
        students (list): List of student dictionaries with 'name', 'grade', 'subject'
    
    Returns:
        dict: Statistics including average, highest, lowest, pass_rate
    """
    # TODO: Let Copilot implement this analysis
    pass


# Sample test data
students = [
    {"name": "Alice", "grade": 85, "subject": "Math"},
    {"name": "Bob", "grade": 76, "subject": "Math"},
    {"name": "Charlie", "grade": 92, "subject": "Science"},
    {"name": "Diana", "grade": 58, "subject": "Math"},
    {"name": "Eve", "grade": 88, "subject": "Science"},
    {"name": "Frank", "grade": 72, "subject": "Math"},
    {"name": "Grace", "grade": 95, "subject": "Science"},
    {"name": "Henry", "grade": 65, "subject": "Math"}
]

if __name__ == "__main__":
    stats = analyze_student_grades(students)
    print("Student Grade Analysis:")
    print(f"Average: {stats}")
    
    # Expected output format:
    # {
    #     'average': 79.125,
    #     'highest': 95,
    #     'lowest': 58,
    #     'pass_rate': 87.5,
    #     'total_students': 8
    # }
