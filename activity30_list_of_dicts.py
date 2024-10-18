# Activity 30: Master Python List of Dictionaries Data Structure

import sys

# Redirect output to a file
sys.stdout = open("output.txt", "w")

# Step 1: Define a list of dictionaries
students = [
    {"name": "John", "age": 21, "major": "Computer Science"},
    {"name": "Alice", "age": 22, "major": "Mathematics"},
    {"name": "Bob", "age": 20, "major": "Physics"}
]

# Step 2: Print the list of dictionaries
print("Students List:")
for student in students:
    print(student)

# Step 3: Access specific elements
first_student_name = students[0]['name']
print(f"\nThe first student's name is: {first_student_name}")

# Step 4: Adding a new student
new_student = {"name": "Eve", "age": 23, "major": "Biology"}
students.append(new_student)
print("\nUpdated Students List after adding Eve:")
for student in students:
    print(student)

# Step 5: Updating a student's information
students[0]['major'] = 'Software Engineering'
print("\nUpdated Students List after changing John's major:")
for student in students:
    print(student)

# Step 6: Removing a student
students.remove(students[2])  # Removes Bob
print("\nUpdated Students List after removing Bob:")
for student in students:
    print(student)


