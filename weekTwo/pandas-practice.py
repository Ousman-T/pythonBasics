import numpy as np
import pandas as pd
print("=====SECTION 1=====")
arr = np.array([1,2,3,4,5])
print(arr)

print("=====SECTION 2=====")
twod_arr = np.arange(12)
print(twod_arr)
arr_3x4 = twod_arr.reshape(3,4)
print(arr_3x4)
print(" 9")
arr_4x3 = twod_arr.reshape(4,3)
print(arr_4x3)

print("=====SECTION 3=====")
a = np.array([1,2,3])
b = np.array([4,5,6])
add_result = a + b
print(add_result)
mult_result = a * b
print(mult_result)

print("=====SECTION 4=====")
slice = np.array([10,20,30,40,50])
middle = slice[2:4]
print(middle)

print("=====SECTION 5=====")
arr = np.array([4,8,15,16,23,42])
mean_val = np.mean(arr)
print("Mean: ", mean_val)
sum = np.sum(arr)
print("Sum: ", sum)
std_val = np.std(arr)
print("Standard Deviation: ", std_val)

print("=====SECTION 6=====")
tup = (7,14,21)
conv_tup = np.array(tup)
print(conv_tup)
def_list = [conv_tup]
print(def_list)

print("=====SECTION 7=====")
df = pd.read_csv("../data/students.csv")
print(df.head())

print("=====SECTION 8=====")
dict = {"Name":["Daniel"], "Age": [18], "Grade": [100]}
dict_df = pd.DataFrame(dict)
print(dict_df)

print("=====SECTION 9=====")
grades = dict_df["Grade"]
print(grades)
avg_grades = dict_df["Grade"].mean()
print("Average Grade:", avg_grades)