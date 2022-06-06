array =[1,2,3,4,3]
print(array)
flag = 0
for i in range(0,5):                        # used a test case of 5 elements
    for j in range(i+1,5):
        if array[i] == array[j]:
            print(array[i])
            flag += 1
            break;
        else:
            continue
    if flag == 1:
        break;
