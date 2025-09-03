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
