print("=====SECTION 21=====")
def word_lengths(words):
    return {w: len(w) for w in words}
words = ["Python", "Is", "Fun"]
print(word_lengths(words))

print("=====SECTION 22=====")
even_nums = [n**2 for n in range(1, 21) if n % 2 == 0]
print(even_nums)

print("=====SECTION 23=====")
people = [
    {
        "name":"Bob",
        "age": 22,
    },
    {
        "name":"Alice",
        "age": 22,
    },
    {
        "name":"Dan",
        "age": 26,
    }
]
def average_age(list):
    ages = [person["age"] for person in people]
    return sum(ages) / len(ages) if ages else 0
print(average_age(people))