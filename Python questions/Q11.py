def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


a = input("enter a string: ")
b  = reverse(a)
if a == b:
    print("string is palindrome")

else:
    print("Not a palindrome")





