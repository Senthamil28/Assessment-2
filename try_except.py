a,b=input("Enter The Numerator Number:"),input("Enter The Denominator Number:")
try:
    c=int(a)/int(b)
    print("The Division of {0} and {1} is {2}".format(a,b,c))
except ZeroDivisionError:
    print("Check the given values")
