def getstudents():
    students = ["Mark","james"]
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title())
            print(students_titlecase)
        return students_titlecase

    students_titlecase_names = getstudents()
    print(students_titlecase_names)
   