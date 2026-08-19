import math

def sum_numbers(nums):  # normal function
    return sum(nums) 

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
#print(result)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in countries:
#     print(i)

def upper_case(string):
    return string.upper()

upper_countries = map(upper_case, countries)
#print(list(upper_countries))

def square(num):
    return num*num

squared_numbers = map(square, numbers)
#print(list(squared_numbers))

upper_names = map(upper_case, names)
#print(list(upper_names))

def land_filter(country):
    if 'land' in country:
        return False
    return True

filtered_countries = filter(land_filter, countries)
#print(list(filtered_countries))

def is_six_lettered(country):
    if len(country) == 6:  
        return False
    return True

non_six_lettered = filter(is_six_lettered, countries)
#print(list(non_six_lettered))
