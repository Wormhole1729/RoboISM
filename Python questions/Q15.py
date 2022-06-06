string = input("Enter a string ")
alphabet = 0
nums = 0
chars = 0
for i in range(len(string)):
    if ord(string[i:i+1]) in range(65,91):
        alphabet += 1

    if ord(string[i:i+1]) in range(97,123):
        alphabet += 1

    if ord(string[i:i+1]) in range(48,58):
        nums += 1




print(alphabet)
print(nums)
print(len(string) - nums - alphabet)
