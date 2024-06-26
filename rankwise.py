class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = sum(marks) / len(marks)
    
    def _repr_(self):
        return f"Student(name={self.name}, marks={self.marks}, average={self.average:.2f})"

def get_student_details():
    students = []
    for _ in range(10):
        name = input("Enter the student's name: ")
        marks = list(map(float, input("Enter the student's marks separated by space: ").split()))
        student = Student(name, marks)
        students.append(student)
    return students

def print_min_max_avg(students):
    min_avg_student = min(students, key=lambda student: student.average)
    max_avg_student = max(students, key=lambda student: student.average)
    print(f"Student with minimum average: {min_avg_student.name}, Average: {min_avg_student.average:.2f}")
    print(f"Student with maximum average: {max_avg_student.name}, Average: {max_avg_student.average:.2f}")

def print_rankwise(students):
    ranked_students = sorted(students, key=lambda student: student.average, reverse=True)
    print("Students in rank-wise order based on their average marks:")
    for rank, student in enumerate(ranked_students, start=1):
        print(f"Rank {rank}: {student.name}, Average: {student.average:.2f}")

def main():
    students = get_student_details()
    print_min_max_avg(students)
    print_rankwise(students)

if __name__ == "_main_":
    main()