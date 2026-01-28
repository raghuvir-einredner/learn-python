# dictionary stores data in key value pair
dict1={"name":"Raghuvir","age":18,"city":"ara"}
print(dict1)
#name , age , city are keys and raghvuir , 18 , ara are values
#Each key is unique
#dictionary do not allows duplicate keys
#dictionary are unordered and mutable

# to access values through key
print(dict1["name"])
print(dict1["age"])
print(dict1["city"])

# to update some value in dictionary
dict1["name"]="Shiv"
print(dict1)

# .items() returns all key value pairs as tuple of the dictionary
print(dict1.items())
print(dict1.keys())
print(dict1.values())

# .update() adds another dictionary end to end
dict2={"income":0,"net worth":"null"}
dict1.update(dict2)
print(dict1)

# .get(key) gives value of key
print(dict1.get("income"))

#dictionary can also be nested
student={"name":"Raghuvir","subject marks":{"phy":34,"chem":45,"math":86}}
print(student)
print(student["subject marks"])
#to access inner data in a nested dictionary
print(student["subject marks"]["phy"])

#slicing and indexing not possible in dictionary because doesnt store data w.r.t to position or index
# .len will give no. of key and value pair in dictionary
print(len(student))

#del deletes given key from dictionary
del dict1["income"]
print(dict1)

#taking user input in dictionary
ste={}
y=input("Enter your name:")
ste["name"]=y
z=input("Enter your income:")
ste["income"]=z
x=input("Enter your net worth:")
ste["net worth"]=x
print(ste)

