students = []

class Student:
    def add_student(self,name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)
       # self.add_student()    -- self usage

student = Student()
student.add_student("Sai Pavan",123)

print(students)