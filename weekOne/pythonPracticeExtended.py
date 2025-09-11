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

print("=====SECTION 11=====")
#The operation goes through but Python defaults to false, because they are different data types
print(12 == "Twelve")

print("=====SECTION 12=====")
is_even = lambda n: "even" if n % 2 == 0 else "odd"
print(is_even(22))

print("=====SECTION 13=====")
res = 0.1 + 0.2
def is_decimal(n):
    if n == 0.3:
        return True
    else:
        return False

print(is_decimal(res))

print("=====SECTION 14=====")
def make_loud(text):
    if type(text) == str:
        text += "!!!"
    return text
def shout(text):
    modified_text = make_loud(text)
    print(modified_text)
print(shout("Ousman"))

print("=====SECTION 15=====")
#Given x = 10, y = 5, z = 0, write a conditional that prints "Only x is positive" if only x is greater than 0.
x = 10
y = 5
z = 0
if x > 0 and y <= 0 and z <= 0:
    print("Only x is positive")

print("=====SECTION 16=====")
def print_something(something):
    print(something)
    return None
print(type(print_something("Hello")))

print("=====SECTION 17=====")
byytes = b'hello'
string_data = byytes.decode("UTF-8")
print(type(byytes))
print(string_data)
print(type(string_data))

print("=====SECTION 18=====")
password = "OpenSesame"
user_input = input("Enter a password: ")
if password == user_input:
    print("Access Granted")
else:
    print("Access Denied")

print("=====SECTION 19=====")
has_permission = True
status = "Allowed" if has_permission else "Denied"
print(status)

print("=====SECTION 20=====")
def make_adder(n):
    return lambda x: x + n
add5 = make_adder(5)
print(add5(3))

print("=====SECTION 21====")
def grade(score):
    match score:
        case _ if score >= 90:
            return "A"
        case _ if score >= 80:
            return "B"
        case _ if score >= 70:
            return "C"
        case _ if score >= 60:
            return "D"
        case _ :
            return "F"
print(grade(82))

print("=====SECTION 22====")
def calculate(operator, num_one, num_two):
    match operator:
        case _ if operator == "+":
            return num_one + num_two
        case _ if operator == "-":
            return num_one - num_two
        case _ if operator == "*":
            return num_one * num_two
        case _ if operator == "/":
            return num_one / num_two

print(calculate(operator="+", num_one=3, num_two=5))
print(calculate(operator="-", num_one=3, num_two=5))

