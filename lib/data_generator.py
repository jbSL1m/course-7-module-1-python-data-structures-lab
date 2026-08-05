# This module contains functions to lazily generate student data.
# A generator gives values one at a time, which is helpful when you do not want to create a full list.

def student_generator(student_list, major):
    # Go through each student and yield only the ones whose major matches the given major.
    # This is case-insensitive, so "Computer Science" and "computer science" both work.
    return (student for student in student_list if student[2].lower() == major.lower())
