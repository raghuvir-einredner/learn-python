'''m="be continue"
n=2026
print(m,"in",n)

# take percentage of 3 sub take avg and then display message acc to grade he got
#phy=int(input("enter your percentage of physics : "))
#chem=int(input("enter your percentage of chem : "))
#maths=int(input("enter your percentage of maths : "))
#avg=(phy+chem+maths)/3
#if (avg>=90 and avg<=100):
#    print("you got A+")
#elif avg>=80:
#    print("you got A")
#elif avg>=70:
#    print("you got B")
#elif avg>=60:
 #   print("you got C")
#elif avg>=50:
#    print("you got D")
#else:
#    print("you failed !! try again next year.")

# write a code to compare height of three guys
a=float(input("enter A's height : "))
b=float(input("enter B's height : "))
c=float(input("enter C's height : "))
if a>b and a>c:
    print("A is tallest")
elif b>a and b>c:
    print("B is tallest")
else :
    print("C is tallest")
#although this code works but its complexity is high so nested if else will be a better choice here
a=float(input("enter A's height : "))
b=float(input("enter B's height : "))
c=float(input("enter C's height : "))
if a>b :
    if a>c:
        print("A is tallest")
    else:
        print("C is tallest")
else:
    if b>c:
        print("B is tallest")
    else:
        print("C is tallest")

#nested if else to check mob no. and otp
mob=int(input("enter mobno. : "))
if mob==7644040115:
    otp=int(input("enter otp : "))
    if otp==5678:
        print("otp is correct")
    else :
        print("otp is incorrect")
else:
    print("mob no. is incorrect")

#
a="this is good for you"
if a[-2:]=="ou":
    print("string ends with br")
else :
    print("string doesnot ends with br")
    '''

