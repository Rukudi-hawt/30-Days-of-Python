import math
import functools

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

def is_six_lettered_or_more(country):
    if len(country) >= 6:  
        return False
    return True

non_six_lettered_or_more = filter(is_six_lettered_or_more, countries)
#print(list(non_six_lettered_or_more))

def has_E(country):
    if 'E' in country:  
        return False
    return True

non_has_E = filter(has_E, countries)
#print(list(non_has_E))

upper_non_E = map(upper_case, (filter(has_E, names)))
#print(list(upper_non_E))

def get_string_lists(lst):
    new_list = []
    for i in lst:
        new_list.append(str(i))
    return new_list

#print(get_string_lists(numbers))

def sum_two_numbers(x, y):
    return int(x) + int(y)

reduced_list = functools.reduce(sum_two_numbers, numbers)
#print(reduced_list)

def concatenate_countries(country1, country2):
    if country2 == countries[len(countries) - 1]:
        return country1 + ', and ' + country2
    return country1 + ', ' + country2

concatenated_countries = functools.reduce(concatenate_countries, countries)
print(concatenated_countries + ' are all countries in Europe.')