print("Enter the list of numbers and 'e' after the last element")
numbers = []
x = 0
while (x != 'e'):
    x = input()
    numbers.append(x)


numbers.remove('')


for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i])


option = input("choose 'asc' for ascending order 'desc' for descending order 'none' for the unaltered list ")
if option == 'asc':
    
    numbers.sort()
    print(numbers)

elif option == 'desc':
    numbers.sort(reverse = True)
    print(numbers)
else:
    print(numbers)
    
