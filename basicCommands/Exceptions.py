student = {
    "name" : "Sai Pavan",
    "student_id" : 12456,
    "feedback" : None
}


student ["last_name"] = "kowlaski"
try:
    last_name=student["last_name"]
    numbered_last_name = 3 + last_name
    print("name is "+last_name)
except KeyError:
    print("Error Finding last_name")
except TypeError:
    print("I can't add these two together")
except Exception as error:
    print("Unkown error"+error)


print("This code executes.. !!")

