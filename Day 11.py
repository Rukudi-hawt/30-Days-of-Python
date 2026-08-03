import math

# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()

# def generate_full_name ():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# print(generate_full_name())

# def sum_of_numbers(n):
#     total = 0
#     for i in range(n+1):
#         total+=i
#     return total
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050


def add_two_numbers(x, y):
    return x + y


def area_of_circle(π, r):
    return f"{π * (r * r): .2f}"


def add_all_nums(*args):
    Counter = 0

    for i in args:
        if not isinstance(i, (int, float)):
            Counter += 1

    if Counter >= 1:
        Answer = "Parameter data types must be of type integer or float."
    else:
        Answer = sum(args)
    return Answer


def convert_celsius_to_fahrenheit(celcius):
    return f"{celcius * (9 / 5) + 32: .2f}"


def check_season(month):
    if month in ("December", "January", "February"):
        return "Summer"

    if month in ("March", "April", "May"):
        return "Autumn"

    if month in ("June", "July", "August"):
        return "Winter"

    if month in ("September", "October", "November"):
        return "Spring"


def calculate_slope(pair1, pair2):
    x1 = pair1[0]
    x2 = pair2[0]

    y1 = pair1[1]
    y2 = pair2[1]

    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    delta = (b**2) - 4 * (a) * (c)
    if delta >= 0:
        root1 = ((-b) + (math.sqrt((b**2) - 4 * (a) * (c)))) / (2 * a)
        root2 = ((-b) - (math.sqrt((b**2) - 4 * (a) * (c)))) / (2 * a)
        return root1, root2
    else:
        return "Delta is undefined."


def print_list(lst):
    Answer = []
    for i in lst:
        Answer.append(i)
    return Answer


def print_reverse_list(lst):
    Answer = []
    for i in range(len(lst)):
        if i > 0:
            Answer.append(lst[-i])
    Answer.append(lst[0])
    return Answer


def capitalize_list_items(lst):
    list = lst
    item = ""
    counter = 0
    for i in lst:
        item = i
        item = item.capitalize()
        list[counter] = item
        item = ""
        counter += 1
    return list


def add_item(lst, item):
    list = lst
    list.append(item)
    return list


# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_stuff, 'Meat'))


def remove_item(lst, item):
    list = lst
    # for i in range(len(lst)):
    #      if list[i-1] == item:
    list.remove(item)
    return list


# print(remove_item(food_stuff, 'Tomato'))


def sum_of_numbers(num):
    Add = 0
    for i in range(num):
        Add += i
    return Add


# print(sum_of_numbers(370))


def sum_of_odds(num):
    Add = 0
    for i in range(num + 1):
        if i % 2 > 0:
            Add += i
    return Add


# print(sum_of_odds(370))


def sum_of_even(num):
    Add = 0
    for i in range(0, num + 1, 2):
        Add += i
    return Add


# print(sum_of_even(370))


def evens_and_odds(num):
    Even = 0
    Odd = 0

    for i in range(0, num, 2):
        Even += 1
        Odd += 1
    print(f"{'The number of odds are:', Odd, 'The number of evens are:', Even}")


# evens_and_odds(150)


def factorial(num):
    Total = 1

    for i in range(0, num, 1):
        Total += Total * i
    return Total


# print(factorial(20))


def is_empty(item):
    Answer = ""
    if item:
        Answer = "The item is populated."

    if not item:
        Answer = "The item is empty."

    return Answer


# X = "Yahhhhhhhhhhhhhhhhh"
# print(is_empty(X))          

def mean(data):
     sum = 0
    
     for i in range(0, (len(data))):
           sum += data[i]
     return  sum/(len(data)) 

lst = [4, 6, 3, 7, 8, 8, 9, 10, 34, 16, 27, 22, 22, 22, 45, 10, 45, 11]
#print(mean())  

def median(data):
     answer = []
     half = len(data)//2

     if len(data) % 2 > 0:
          answer.append(data[half + 1])
     else:
          answer.append(data[half])
          answer.append(data[half + 1])
     return answer

#print(median(lst))

def mode(data):
    