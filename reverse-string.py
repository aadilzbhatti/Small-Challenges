#reverse a string

s = ""
str = input("Enter the string to be reversed: ");

for i in range (0, len(str)):
    s += str[len(str) - i-1]

print(s)
    