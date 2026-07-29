# set1 = {1, 2, 3, 4}
# set2 = {5, 6, 7, 8}
# set3 = set1.union(set2)
# print(set3)

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

len_it_companies = len(it_companies)
it_companies.add('Twitter')
it_companies.update(['Mohara', 'Three', 'Samsung', 'Nvidia'])
it_companies.remove('Three')
print(it_companies)

Union = A.union(B)
Intersection = A.intersection(B)
print(A.symmetric_difference(B))
IsSubset = A.issubset(B)
IsDisjoint = A.isdisjoint(B)
A = A.union(B)
B = B.union(A)
Sym_diff = A.symmetric_difference(B)
print(Union, Intersection, IsSubset, IsDisjoint, A, B, Sym_diff )
A.discard(44)
A.remove(44) #returns an error
del A, B

age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print(len(ages),'\n',len(age))

set1 = {'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.'}
#set2 = {'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.'}
print(set1)
string = "I am a teacher and I love to inspire and teach people."
setString = set(string.split())
print(setString)