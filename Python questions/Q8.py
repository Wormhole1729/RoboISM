string = input("enter a string ")
sum = 0

for i in range(len(string)):
     if ord(string[i:i+1])  in range(48,58):
         sum += int(chr(ord(string[i:i+1])))
  
print(sum)    
