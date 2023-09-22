class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with sample input
if __name__ == "__main__":
    # Creating sample student objects
    student1 = Student("Alice", "A001", 3.8)
    student2 = Student("Bob", "B002", 3.5)
    student3 = Student("Charlie", "C003", 3.9)
    student4 = Student("David", "D004", 3.7)

    # Creating a list of student objects
    students = [student1, student2, student3, student4]

    # Sorting the list based on CGPA
    sorted_students = sort_students(students)

    # Printing the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
