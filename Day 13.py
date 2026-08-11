numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i <= 0]
#print(negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [sub_list[x] for sub_list in list_of_lists for x in range(0, len(sub_list), 1)]
#print(flattened_list)

# for sub_list in list_of_lists:
#      print(sub_list)
#      for x in range(0, len(sub_list), 1):
#           print(sub_list[x])
#           flattened_list.append(sub_list[x])
# print(flattened_list)

num_powers = []
powers = [num_powers for num in range(0, 11, 1) for power in range(0, 7, 1)]


# for num in range(0, 11, 1):
#      num_powers = []
#      num_powers.append(num)
#      for power in range(0, 7, 1):
#           num_powers.append(num**power)
#      powers.append(num_powers)
print(powers)