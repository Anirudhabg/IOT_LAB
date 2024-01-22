# 5 -> Print a name "n" times, where name and n are read from standard input, using for and while loops
name = input("Enter your name: ")
n = int(input("Enter number of times to print the name: "))

print("Using for loop: ")
for i in range(n):
    print(name)

print("Using while loop: ")
count = 0
while count < n:
    print(name)
    count += 1