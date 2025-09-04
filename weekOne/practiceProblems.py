# printing the number 42
print("=====SECTION 1=====")
print(42)
print("This is the number: " + str(42))

#printing type
print("=====SECTION 2=====")
print(type(42))
print(type("Hello World!"))
print(type(3.14))
print(type(True))
print(type(None))
print(type(b'hello'))

#TODO mental note, python is OOP like Java in the sense 42 is an instance of the int class

#adding numbers
print("=====SECTION 3=====")
num = 11 + 33
print(num)
print(type(num))

print("=====SECTION 4=====")
#adding ints to floats
numb = 42.8 + 11
print(numb)
print(type(numb))

print("=====SECTION 5=====")
print(True + True + False)
#mental note, the result is 2 because True has value of 1 and False value of 0 in boolean algebra. So 1+1+0=2

print("=====SECTION 6=====")
name = "Ousman"
print("Hello, " + name)
print("=====SECTION 7=====")
if (name == "Alice"):
    print("Hello, Alice")
else :
    print("Hello, not Alice")

print("=====SECTION 8=====")
age = 16
if (age < 18):
    print("You're a minor")
else :
    print("Hello adult")

print("=====SECTION 9=====")
none = None
print(type(none))

print("=====SECTION 10=====")
def greet(name):
    print("Hello, " + name)

greet("Momo")
print("=====SECTION 11=====")

def add_num(num1, num2):
    """ Takes two parameters
    adds them, an example of doctring for multi-line-comments """
    return num1 + num2
print(add_num(7,14))

print("=====SECTION 12=====")
help(greet("Momo"))
print("=====SECTION 13=====")
add = 5
subtract = 11
print(add + subtract)
multiply = 15
divide = 3
print(multiply * divide)
print (multiply / divide)
print(subtract - multiply)

print("=====SECTION 14=====")
#lambda function to multiply numbers. anonymous 1 line function
var = lambda a, b: a * b
print(var(3, 5))
print("=====SECTION 15=====")
#utilized the int method to convert the float into an int. It doesn't round, rather it floors the number to it's whole int.
float_num = 3.14
int_num = int(float_num)
print(int_num)
print("=====SECTION 16=====")
#in python you cannot concat a string and an int, int must be converted to string
print("Age: " + "18")
print("=====SECTION 17=====")
score = 22
if score < 50:
    print("Low")
elif 50 <= score < 80:
    print("Average")
else:
    print("High")

print("=====SECTION 18=====")
x = None
if x is None:
    print("No value")
else:
    print("Contains value")

print("=====SECTION 19=====")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))