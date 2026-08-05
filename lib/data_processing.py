# This module contains functions to process student data.
# These helpers turn student records into readable text for the console.

def format_student_data(student):
    # A student record is stored as a tuple: (id, name, major).
    # Unpacking it makes each part easy to use.
    student_id, student_name, major = student
    return f"ID: {student_id} | Name: {student_name} | Major: {major}"


def display_students(student_list):
    # Loop through each student and print the formatted version.
    for student in student_list:
        print(format_student_data(student))