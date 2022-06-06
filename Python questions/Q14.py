def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)
 
a = int(input("Enter an integer "))
b = int(input("Enter an Integer "))
print("gcd(", a , "," , b, ") = ", gcd(a, b))
 
