# Check if a given number is a prime number using a for loop
num = int(input("Enter a number:"))
if num < 2:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

# Write a program to calculate the factorial of a number using a while loop.
num = int(input("Enter a number to calculate the factorial: "))
factorial = 1
if num < 0:
    print("Factorial can't be done with -ve numbers")
else:
    i = 1
    while i <= num:
        factorial = factorial * i
        i = i + 1
    print(f"The factorial of {num} is {factorial}")

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
