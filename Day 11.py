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
     return f"{π * (r * r) : .2f}"


def add_all_nums(*args):
     Counter = 0
     
     for i in args:
          if not isinstance(i, (int, float)):
               Counter += 1

     if Counter >= 1:
          Answer = 'Parameter data types must be of type integer or float.'
     else:
          Answer = sum(args)
     return Answer
          

def convert_celsius_to_fahrenheit(celcius):
     return f'{celcius*(9/5) + 32: .2f}'


def check_season(month):
     if month in ('December', 'January', 'February'):
          return 'Summer'

     if month in ('March', 'April', 'May'):
          return 'Autumn'

     if month in ('June', 'July', 'August'):
          return 'Winter'

     if month in ('September', 'October', 'November'):
          return 'Spring'

def calculate_slope(pair1, pair2):
     x1 = pair1[0]
     x2 = pair2[0]

     y1 = pair1[1]
     y2 = pair2[1]  

     return (y2 - y1)/(x2 - x1) 

def solve_quadratic_eqn(a, b, c):
     delta =  (b**2) - 4*(a)*(c) 
     if delta >= 0:
          root1 = ( ( -b ) + ( math.sqrt( (b**2) - 4*(a)*(c) ) ) ) / (2 * a) 
          root2 = ( ( -b ) - ( math.sqrt( (b**2) - 4*(a)*(c) ) ) ) / (2 * a)
          return root1, root2
     else:
          return 'Delta is undefined.'

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
     item = ''
     counter = 0
     for i in lst:
          item = i
          item = item.capitalize()
          list[counter] = item
          item = ''
          counter += 1
     return list

print(capitalize_list_items(['potato', 'tomato', 'Mango', 'Milk']))


