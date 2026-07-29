# Dict1 = {'Number1' : '1', 'Number2' : '2', 'Number3' : '3', 'NumberSet1' : '4 5 6 7', 'NumberSet2' : ['8', '9', '10']}
# print(Dict1['NumberSet1'], '\n', Dict1['NumberSet2'])
# Dict1['Number11'] = '11'
# print(Dict1['Number11'])
# print(Dict1.items())

dictDog = dict()
dictDog['Name:'] = 'Spike'
dictDog['Colour:'] = 'Golden-Brown'
dictDog['Breed:'] = 'Belgian Malinois'
dictDog['Legs:'] = 'Medium'
dictDog['Age:'] = 'Em...'
# print(dictDog)
# print(list(dictDog))
dictStudent_Dictionary = {'first_name' : 'Amber', 'last_name' : 'Heard', 'gender' : 'Female', 'age' : '18', 'marital status' : 'Divorced', 'skills' : ['Actor','Criminal','Celebrity'], 'country' : 'USA', 'city and address' : 'Beverly Hills, Hollywood, LA'}
# print(len(dictStudent_Dictionary))
# print(dictStudent_Dictionary)
# print(dictStudent_Dictionary['skills'], type(dictStudent_Dictionary['skills']))
dictStudent_Dictionary['skills'].append(['Singer', 'Dancer'])
# print(dictStudent_Dictionary['skills'], type(dictStudent_Dictionary['skills']))
# print(list(dictStudent_Dictionary), '\n', list(dictStudent_Dictionary.values()))
print(tuple(dictStudent_Dictionary.items()))
del dictStudent_Dictionary['skills']
print(dictStudent_Dictionary)
del dictDog
