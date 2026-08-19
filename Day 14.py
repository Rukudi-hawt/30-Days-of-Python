
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
print(list(upper_countries))