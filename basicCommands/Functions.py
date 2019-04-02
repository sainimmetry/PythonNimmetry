#Functions
print("Functions sample")
str(3)
print(str(4))
print(int("15"))
#username = input("Enter username:")


#Sample Function call

students =[]

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase =student.title()
        return students_titlecase



def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name,student_id=332):
    student ={"name":name,"student_id":student_id}
    students.append(students)


student_list = get_students_titlecase()

add_student("sai pavan",15)


#def var_args(name, *args):
#    print(name)
#    print(args)

def var_args(name,**kwargs):
    print(name)
    print(kwargs["description"],kwargs["feedback"])



var_args("sai pavan",description="This is sample description",feedback=None,Nimmetry_employee=True)

#How to assign exception handling in functions


#Refer Functions video once again for perfection.
