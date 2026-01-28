# .sort() sorts elements of list in ascending order
lst=[78,157,5,4,230,316,97]
lst.sort()
print(lst)
# .sort(reverse=true) sorts elements in descending order
lst.sort(reverse=True)
print(lst)

# .reverse() reverses order of elements of list
lst2=["rohan","sohan","mohan"]
lst2.reverse()
print(lst2)

# code to check a no. is palindrome or not
num=list(input("enter your number to check for palindrome property : "))
one=num.copy()
num.reverse()
if (one == num):
    print("number is palindrome")
else:
    print("number is not palindrome")

#find max min and find their avg
lst3=[70,157,5,4,215,316,4,25]
a=min(lst3)
b=max(lst3)
print((a+b)/2)
# .index( ) gives index number of data , if data repeats it only gives the index no. when data
#is encountered for first time
print(lst3.index(4))