string = input("Enter a string ")
a = "i"

for i in range(len(string)):
    a += string[i:i+1]*2

print(a[1:len(a)])
