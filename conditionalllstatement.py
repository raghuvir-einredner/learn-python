#input function always takes input in str format you have to change acc to use
#indentation error keep in mind
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
if x>y:
    print(x," is greater than ",y)
else:
    print(y," is greater than ",x)
# if else statement only applicable to compare between two variables

# ladder if else
light=input("enter traffic signal colour :")
if light=="green":
    print("Go")
elif light=="red":
    print("Stop")
elif light=="yellow":
    print("Be ready to go")
else:
    print("invalid traffic signal")

#nested if else
email=input("enter your email address:")
if (email=="raghuvir@gmail.com"):
    pswd=input("enter your password :")
    if (pswd=="12345"):
        print("login successful")
    else :
        print("password is incorrect")
else :
    print("email is incorrect")