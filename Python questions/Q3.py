int1 = int(input("Enter 1st integer "))
operator = input("Eneter '+' '-' '/' 'or' ")
int2 = int(input("Enter 2nd integer "))

if operator == '+':
    print(int1 + int2)

elif operator == '-':
    print(int1 - int2)

elif operator == '/':
    print(int1/int2)

else:
    print(int1 or int2)


    
