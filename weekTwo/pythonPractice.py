from functools import reduce

print("=====SECTION 1=====")
fav_color = ["red", "blue", "green", "yellow", "pink"]
print(fav_color[1])

print("=====SECTION 2=====")
tuple = (1,2,3,4)
print(tuple)
#tuples are immutable, can't change
#tuple[2] = 0

print("=====SECTION 3=====")
first_dictionary = {
    "name": "Ousman",
    "age": 25,
    "city":"East Orange"
}
print(first_dictionary.get("city"))

print("=====SECTION 4=====")
my_set = {'a','b','c','d'}
#can't add duplicates nor are sets mutable
print(my_set)

print("=====SECTION 5=====")
def greet(name):
    return f"Hello, {name}!"
print(greet("Jim"))

print("=====SECTION 6=====")
def multiply(num1, num2):
    return num1 * num2
print(multiply(3, 4))

print("=====SECTION 7=====")
def evens(num):
    return list(filter(lambda x: x % 2 == 0, num))
print(evens([1,2,3,4,5,6]))

print("=====SECTION 8=====")
nums = [1,2,3,4,5]
suared = list(map(lambda x: x ** 2, nums))
print(nums)
print(suared)

print("=====SECTION 9=====")
fruit = ["apple", "banana", "cherry"]
uppercase_fruit = [string.upper() for string in fruit]
print(fruit)
print(uppercase_fruit)

print("=====SECTION 10=====")
list_of_dictionaries = [
    {
        "name": "Jim",
        "score": 25,
    },
    {
        "name":"Harry",
        "score": 40,
    },
    {
        "name":"Henry",
        "score": 50,
    }
]
print(list_of_dictionaries)
print("=====SECTION 11=====")
def print_key_value(dictionary):
    for key, value in dictionary.items():
        print(key, value)
print_key_value({"lastName": "Jim", "score": 25})

print("=====SECTION 12=====")
def sum_prices(items):
    total = 0
    for key, value in items.items():
        total += value
    return total
shopping = {
    "apple": 3,
    "orange": 2,
    "cherry": 5
}
print(sum_prices(shopping))

print("=====SECTION 13=====")
hobbies = {
    "Jose": ["Gaming", "Working out"],
    "Michael": ["Eating", "Traveling"],
    "Elliot": ["Watching movies", "Reading books"]
}

def add_hobby(hobby_dict, name, new_hobby):
    if name in hobby_dict:
        hobby_dict[name].append(new_hobby)
    else:
        hobby_dict[name] = [new_hobby]
add_hobby(hobbies, "Jose", "hiking")
add_hobby(hobbies, "David", "chess")
print(hobbies)

print("=====SECTION 14=====")
def return_largest(list):
    try:
        return max(list)
    except ValueError:
        return "No input provided"
print(return_largest([]))

print("=====SECTION 15=====")
ran_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ran_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
my_list = list(ran_set)
print(my_list)
#they are two different data types list are like arrays and sets like objects, sets you can't use bracket notation to target an index. Built in methods to convert both

print("=====SECTION 16=====")
i = 1
while i <= 5:
    print(i)
    i+= 1

print("=====SECTION 17=====")
def average(*args):
    return sum(args) / len(args)
print(average(1,2,3,4,5,6,7,8,9,10,11,12))

print("=====SECTION 18=====")
try:
    x = 10/0
    print(x)
except ZeroDivisionError:
    print("Error: Can't divide by zero")

print("=====SECTION 19=====")
multiply_list = [2,3,4]
product = reduce(lambda x, y: x * y, multiply_list)
print(product)

print("=====SECTION 20=====")
length = lambda s: len(s)
print(length("Python"))



