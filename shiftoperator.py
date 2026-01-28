a=int(input("enter number :"))
b=a<<2
print("after 2 left bit shifting result is ,",b)
print(b/a )

#rightshift
c=a>>2
print("after 2 right bit shifting result is ,",c)


#mixed
x=11
y=x>>1
z=y<<2
print((x+y)/z)

r,q=15,12
s,p=r<<2,q>>1
print((r+s)/(p-q))