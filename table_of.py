# write a program to multiply any number with 1 to 10 will get table of that number
num = int(input("Enter number:"))
for i in range(1,11):
    print( num, "X", i, "=", num*i )