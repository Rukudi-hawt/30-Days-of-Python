import math
def process_numbers(numbers, operation):
     new_list = []
     for i in range(0, len(numbers), 1):
          new_list.append(operation(numbers[i]))
     return new_list

# list = [1, 2, 3, 4 ,5]
# print(process_numbers(list, math.sqrt)) 

def calculate(numbers, operation):
     sum = numbers[0]
     for i in range(1, len(numbers), 1):
          sum = operation(sum, numbers[i])
     return sum

def add(x, y):
     return (x + y)

def multiply(x, y):
     return (x * y)

numbers = [2, 4, 6, 8]

# print(calculate(numbers, add))
# print(calculate(numbers, multiply))

def find_duplicates(numbers):
     trimmed_list = []

     for i in range(0, len(numbers), 1):
          count = 0
          for y in range(0, len(numbers), 1):
               if numbers[i] == numbers[y]:
                    count += 1

          if numbers[i] not in trimmed_list and count > 1:
                    trimmed_list.append(numbers[i])

     return trimmed_list

numbers = [1, 3, 4, 3, 5, 1, 6, 4, 4]
print(find_duplicates(numbers))