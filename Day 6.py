tuple = (1,2,3,4)
tuple2 = (5,6,7,8)
tuple3 = tuple + tuple2
print(tuple3)

tplBrothers = ('Jack', 'Hansel', 'Jonah', 'Billy')
tplSisters = ('Jill', 'Grettel', 'Johanna', 'Heidi')
tplSiblings = tplBrothers + tplSisters
tplSiblings_Count = len(tplSiblings)
tplFamily_Members = tplSiblings + ('Prosper', 'Everjoyce')
print(tplBrothers, '\n', tplSisters, '\n', tplSiblings, '\n', tplSiblings_Count, '\n', tplFamily_Members)

*Siblings, Father, Mother = tplFamily_Members
tplFruits = ('banana', 'orange', 'mango', 'lemon')
tplVegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
tplAnimal_Products = ('Beef', 'Chicken', 'Lamb', 'Tuna')
tplFood_Stuff = tplFruits + tplVegetables + tplAnimal_Products
lstFood_Stuff = list(tplFood_Stuff)
Food_Stuff_Middle = tplFood_Stuff[1:(len(tplFood_Stuff) - 1)]
lstFirst_Last_Three_Food = list( tplFood_Stuff[0:3] + tplFood_Stuff[-3:len(tplFood_Stuff)] )
del tplFood_Stuff
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


