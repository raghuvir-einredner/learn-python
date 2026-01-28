#list is a collection of diff data types , is changeable, represented by [] square brackets
ls=[24,67,90,"rohan","john"]
print(ls)
#slicing can be done on lists
print(ls[2:])
#list is mutable
ls[4]="sita"
print(ls)
# .append() function adds an new element at the last position
ls.append("ram")
print(ls)
# .insert(index no. , data to be updated) inserts value at the given index number
ls.insert(3,"lakshman")
print(ls)
# .remove(data to be deleted) deletes data block by identifying data
ls.remove(90)
print(ls)
# .pop(index no.) deletes data block by identifying index no.
ls.pop(1)
print(ls)
# ls.pop() putting nothing inside pop deletes last block of the list as it follows LIFO principle
# .extend([]) adds multiple data to the list
ls.extend(["mathura","vrindavan",786])
print(ls)


data=[45,67,89,90,2333]
# min() gives minimum of the list
# max() gives maximum of the list
print(min(data))
print(max(data))
# sum() gives sum of all data of list
print(sum(data))

