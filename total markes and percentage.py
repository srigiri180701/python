rollnum =int(input("enter a roll num"))
n=int(input("enter phy markes"))
m=int(input("enter che markes"))
b=int(input("enter computer sci markes"))
a=(n+m+b)/(3)
print("roll num ",rollnum)
print("percentage",a)
print("total markes",n+m+b)

if a>=80:
    print("first")
elif a>69 and a<80 :
    print("second")
elif a>59 and a<=68:
    print("third")
elif a>40 and a<=58:
    print("fourth")
else :
    print("fail")
