# write a program to find factorial of number
numb = int(input("Enter a Number:"))
# numb = 5 [just trying to use f string here]
# print(f"enter a number:",numb,"!")

factorial = 1
for i in range(1, numb + 1):
    factorial = factorial * i
print("Factorial is",factorial)