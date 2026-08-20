'''write a program to print
*
**
***
****
*****

*****
****
***
**
*
'''
pattern = "*"
for i in range(0,6):
    print(pattern * i)
 
for i in range(0, 5):
    for j in range(5 - i):
        print("*", end="")
    print()