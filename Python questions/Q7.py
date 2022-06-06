def most_frequent(List):
    return max(set(List), key = List.count)



print("Enter the list of numbers and 'end' after the last element")
List = []
x = 0
while (x != 'end'):
    x = input()
    List.append(x)


List.remove('end')



print(most_frequent(List))
