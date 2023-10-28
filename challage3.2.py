class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students based on their CGPA in descending order
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the function with different input lists of students
students = [
  Student("Alice", "A001", 3.8),
  Student("Bob", "B002", 3.5),
  Student("Charlie", "C003", 4.0),
  Student("David", "D004", 3.9),
  Student("Eve", "E005", 3.7),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
