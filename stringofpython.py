#string in py is immutable that it is not changable
#string = "Hello World"
#string[2]='h'
#print(string)
#above code will give error

#how to find length of string
#use len() fun
#space is also counted
string = "Hello World"
#p=len(string)
#print("length is : ",p)

#to combine two or more strings
#FN=input("Enter your first name: ")
#LN=input("Enter your last name: ")
#Fullname=FN+" "+LN
#print("Your good name is : ",Fullname)

#slicing of string
a="razor blade"
print(a[1:5])#starts from one till five doesnt includes five
print(a[:5])#starts from zero till five doesnt include five
print(a[5:])#starts from five till end of string

#negative indexing of string
#negative indexing is done in reverse order starting from last position with " -1 "
#slicing is done from right way
print(a[-4:-1])

m="welcome"
n="my india"
print(n[3:]+"."+m[3:6])

x="2567@gmail.com"
y="zuber ansari"
z="Email Id is"
print(z[:8]+" : "+y[:5]+x[2:])


