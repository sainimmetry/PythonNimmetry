print("Hello World")
a = 10;
b = 20
c = a + b
print(c)


def add_numbers(a, b):
    print(a + b)


add_numbers(5, 6)

x = 'Hello World'
y = """Hello World"""
print(x)
print(y)
z = x = y
print(z)

abc = "hello"
xyz = abc.capitalize()
print(xyz)
print(xyz.replace("e", 'a'))
print(xyz.isalpha())
splitdata = "some,csv,values".split(",")
print(splitdata)

name = "PythonBo"
machine = "HAL"
print("Nice to meet you {0}. I am {1}".format(name, machine))
print(f"Nice to meet you {name}. I am {machine}")

python_course = True
java_course = False

print(int(python_course))

print(str(java_course))

aliens_found = None


number = 50
if number ==5:
    print("Number is 5")
else:
    print("Number is NOT 5")

#Thruty and falsy value

number = 5
if number:
    print("Value is correct..")

name="sai pavan"
if name:
    print("this is valid name")



if python_course:
    print("This will be print")

if aliens_found:
    print(" this data is not found..")
else:
    print("Something will be print")

number = 5
if number!=5:
    print("This will not execute")

if not python_course:
    print("this is not python course")

#List in python
student_names =["Mark",'Sai pavan','hello','Santhi','Anu','Sankar',"Krishna Kumari"]
print(student_names[1]+student_names[2])

student_names.append("Santhi")

print(student_names)

print(len(student_names))

print("Santhi1" in student_names)

del student_names[2]


print(student_names)

print(student_names[1:])

#lOOPS
#For Loops
for name in student_names:
    print("Student name is {0}".format(name))

x=0
for index in range(10):
    x +=10
    print("x value is {0}".format(x))