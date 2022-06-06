print("Enter a range of values ")
a = int(input())
b = int(input())
for i in range(a,b):
    counter = 0
    for j in range(2,i):
        if i%j == 0:
            counter += 1
            
    if counter == 0 and i!= 1:
        print(i)
            


