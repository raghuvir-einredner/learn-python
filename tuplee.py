# tuple built in data type shown with () and are not changeable
tup=(9,0,4,4,5,6,7)
print(tup)
print(type(tup))
print(tup[2])
# slicing is possible in tuple
print((tup[2:5]))

# inbuilt functions of tuple
# .index( ) gives index number of data of tuple
print(tup.index(5))
#.count() gives count of occurence of given data in tuple
print(tup.count(4))