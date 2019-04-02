students = []

class Student:
    def __init__(self,name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)
       # self.add_student()    -- self usage
    def __str__(self):
        return students
    


# student = Student()
new_name=Student("Nimmetry",1)
print(students)