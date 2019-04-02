students = []

def read_file():
    try:
        f = open("student.txt","r")
    #    for student in f.readlines():
        for student in read_students(f):
            students.append(student)
        f.close()

    except Exception as error:
        print(error)


def read_students(f):
    for line in f:
        yield line



read_file()
print(students)
