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


#find max. of list through for loop
'''lst=[5,35,66,7,22,6,10]
max=lst[0] #dont take max = 0 because if loop contains neg values then this will not work
for a in lst:
    if a>max:
        max=a
print(max,"is maximum")'''

#given list count the no. of elements exactly divisble by 8
'''lst=[100,160,168,720,400,161]
count=0
for a in lst:
    if a%8==0:
        count+=1
print("total no. divisible by 8 in list is ",count)'''

#write output of given code
'''for x in range(1,10):
    if x%2!=0:
        print(x**3)'''
#output:
#1
#27
#125
#343
#729

# pass logic is used to suspend the current task for sometime in loop(in both for and while)

#loop with else
#else block will be executed only if loop runs without hitting break
#Code for searching for an element in a list by for loop
'''num=[1,3,5,7,9,11,13]
tar=int(input("Enter the num you want to find in the list :"))
for a in num:
    if a==tar:
        print("found",tar,"at index",num.index(a))
        break
else:
    print("not found in list")'''

#code for searching for an element in a list by while loop
'''num=[1,3,5,7,9,11,13]
tar=int(input("Enter the num you want to find in the list :"))
i=0
while i<len(num):
    if num[i]==tar:
        print("found",tar,"at index",i)
        break
    i+=1
else:
    print("not found in list")'''

#continue keyword is used with loop to skip a specific iteration sending signal back to starting point
#used with both for and while
#code to list all even numbers between a given user input range where starting and ending is included
# by for loop and continue statement
'''m=int(input("Enter starting point of your range : "))
n=int(input("Enter end point of your range : "))
for i in range(m,n+1):
    if i%2!=0:
        continue
    print(i)'''
##code to list all even numbers between a given user input range where starting and ending is included
# by while loop and continue statement
'''m=int(input("Enter starting point of your range : "))
n=int(input("Enter end point of your range : "))
i=m
while i<n+1:
    if i%2!=0:
        i=i+1
        continue
    print(i)
    i=i+1'''

