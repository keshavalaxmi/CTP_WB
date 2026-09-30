from dataclasses import dataclass


# Traditional class
class TraditionalStudent:

    def __init__(self, student_id: int, name: str, marks: float):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def __repr__(self) -> str:
        return (
            f"TraditionalStudent("
            f"student_id={self.student_id}, "
            f"name='{self.name}', "
            f"marks={self.marks})"
        )


# Dataclass
@dataclass
class DataStudent:
    student_id: int
    name: str
    marks: float


# Create objects
student1 = TraditionalStudent(101, "Sahithi", 85.5)
student2 = DataStudent(101, "Sahithi", 85.5)

print("Traditional Class:")
print(student1)

print("\nDataclass:")
print(student2)

print("\nStudent ID:", student2.student_id)
print("Student Name:", student2.name)
print("Marks:", student2.marks)
