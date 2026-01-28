'''for repetition of tasks loops are used
1. while loop '''

#print 20 to 1 on screen
'''i=20
while i>0:
    print(i)
    i-=1 '''

#print multiplication table of any number n
'''n=int(input("Enter a number to get its multiplication table : "))
i=1
while i<11:
    print(n,"x",i,"=",n*i)
    i+=1'''

#for a given list print all data through while loop
'''lst=[30,50,70,80,90,100]
i=0
while i<len(lst):
    print(lst[i])
    i+=1'''

#break statement is used to break loop at a certain point
'''a=2
while a<=10:
    if(a==8):
        break #will break the loop when a becomes 8
    print(a)  #output will be 2 4 6
    a+=2'''

#write a code to search something in list using break
'''lst=[3,5,7,9,11,13,15,17,19]
sea=int(input("Enter number you want to find in list : "))
i=0
while i<len(lst):
    if sea==lst[i]:
        print(sea,"found at index",i)
        break
    i+=1 '''

#2.for loop gets starting point , ending and updation all in one

#default starting point is 0 , ending point is not included , updation is +1 default
'''for a in range(10):
     print("a")'''

#print odd nos. between 50 to 75 with for loop
'''for i in range(51,75,2):
    print(i)'''

#print table of any no. n through for loop
'''n=int(input("Enter a number to get its multiplication table : "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)'''

#to use for loop without range we provide a dataset to the for loop
#works for all string , array , list , tuple ,dictionary , set

#printing elements of list through for loop
'''lst=["earth","mars","jupiter","venus","saturn"]
for a in lst:
    print(a)'''

#search particular character in string
# find if c exists in given string or not
'''str="Welcome"
for a in str:
    if a=="c":
        print("c found")
        break'''




