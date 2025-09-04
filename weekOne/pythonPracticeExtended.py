print("=====SECTION 1=====")
age = 16
is_student = False
if age >= 18 and not is_student:
    print("Sorry, you aren't a student, and you're too old to be here")
elif age < 18 and is_student:
    print("Get to class, student!")
elif age < 18 and not is_student:
    is_student = True
    print("Get to class, student! We enrolled you!")
else:
    print("Not in our system")

print("=====SECTION 2=====")
def describe_type(value):
    if type(value) == int:
        print("Integer")
    elif type(value) == float:
        print("Float")
    elif type(value) == str:
        print("String")
    elif type(value) == bool:
        print("Boolean")

print(describe_type(25))