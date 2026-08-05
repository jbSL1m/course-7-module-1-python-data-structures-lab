# This module contains operations related to sets.
# A set is useful when you want unique values and do not want duplicates.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # Collect each major once, even if the same major appears many times.
    return {student[2] for student in student_list}
