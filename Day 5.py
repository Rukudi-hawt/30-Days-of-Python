# fruits = ['banana', 'orange', 'mango', 'lemon']  
# print('Fruits:', fruits)
# print('Number of fruits:', len(fruits))
# print(fruits[1])
# print(fruits[1][1])
# print(fruits[1::])
# print('guave' in fruits)
# fruits.append('guava')
# print(fruits)
# fruits.insert(3, 'kiwi')
# print(fruits)
# fruits.remove('guava')
# print(fruits)
# fruits.pop(3)
# print(fruits)
# del fruits[1]
# print(fruits)
# del fruits[0:2]
# print(fruits)

lst = [1, 2, 3, 4, 5]
print(len(lst))
First = lst[0]
Middle = lst[2]
Last = lst[4]
print(First, Middle, Last)
print(lst[0::2])
mixed_data_types = ['Rukudzo', 18, '5\'11', 'Single', '88 Gretna Green']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[len(it_companies)-1])
it_companies[1] = 'Ubuntu'
it_companies.append('Xiaomi')
it_companies.insert(len(it_companies)//2, 'Mozilla')
print(it_companies)
str.upper(it_companies[1])