from operator import truediv

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

print(describe_type("howdy"))

print("=====SECTION 3=====")
print(3+3.3+False)
print("=====SECTION 4=====")
x = 222
if x >= 10 and x <= 20:
    if x % 2 == 0:
        print("Even")
    elif x % 2 == 1:
        print("Odd")
else:
    print("Number not within range")

print("=====SECTION 5=====")
logged_in = False
admin = False
if logged_in == True and admin == True:
    print("Welcome admin")
elif logged_in == True and admin == False:
    print("Welcome user")
else:
    print("Access Denied")

print("=====SECTION 6=====")
def get_username(name):
    if name == None:
        print("Guest")
    else:
        print(name)
print(get_username(None))

print("=====SECTION 7=====")
#Can not add a string to a bool or int because Python will treat it as if we are trying to do string concatenation
#print("38" + False)
#print(3.33 + "11")

print("=====SECTION 8=====")
def greet(name, is_morning):
    if is_morning == True:
        print(f"Good morning, {name}!")
    else:
        print(f"Hello, {name}!")
print(greet("Ousman", False))

print("=====SECTION 9=====")
username = ""
display_name = username or "Guest"
print(display_name)

print("=====SECTION 10=====")
def is_divisible(x,y):
    if x%y == 0:
        return True
    else:
        return False
print(is_divisible(20,5))
