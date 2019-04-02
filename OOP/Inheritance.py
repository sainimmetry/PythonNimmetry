students = []

class Student:

    student_school_name = "Nimmetry University"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
    #   student = {"name": name, "student_id": student_id}
        students.append(self)

    # self.add_student()    -- self usage
    def __str__(self):
        return " Student " + self.name

    def get_name_capitalize(self):
        return  self.name.capitalize()

    def get_school_name(self):
        return self.student_school_name

class HighSchoolStudent(Student):
    student_school_name ="Vikas High School"

    def get_school_name(self):
        return  "This is high school student.."

    def get_name_capitalize(self):
        originalValue = super().get_name_capitalize()
        return originalValue + "--HS"

james = HighSchoolStudent("james")
print(james.get_school_name())
print(james.get_name_capitalize())