''' set is collection of unique element where duplicate element not allowed
set is mutable but its elements are not , stores element randomnly and unordered
Indexing and slicing are not possible because there are no order '''

set1={3,4,5,6,7}
print(set1)
print(type(set1))
# .add() adds element to set and inserts randomnly at any location
set1.add(1000)
print(set1)
# .remove(data) removes data from set
set1.remove(1000)
print(set1)
# using .pop() removes any random data from set
set1.pop()
print(set1)
# .len(set) gives length of set
print(len(set1))
# .clear() clears the whole set
set1.clear()
print(set1)

# bonus point
# set doesnt allows list as a entry
'''
set1={3,4,5,6,[7,14,21]}}
print(set1) will give error'''

# dictionary allows list as values
dict2={"name":["Raghvuir","pratyush","ankit"],"marks":[23,45,67]}
print(dict2) #will not give error