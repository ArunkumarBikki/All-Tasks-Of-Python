#choose 1. Find the square of a number 2. Find the cube of a number 3. Exit.
while True:
    print("1.Find the square of a number")
    print("2.Find the cube of a number")
    print("3.Exit")
    choice = input("Enter your choice 1 or 2 or 3:")
    
    if choice == "1":
        num = int(input("Enter a number: "))
        print(f"square of {num} is {num ** 2}")
    
    elif choice == "2":
        num = int(input("Enter a number: "))
        print(f"cube of {num} is {num ** 3}")
    
    elif choice == "3":
        print("Exit")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3 only.")

# palindrome number
num = int(input("Enter a number to check palindrome or not"))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if temp == rev:
    print("It is a Palindrome Number")
else:
    print("It is not a Palindrome Number")

#check a number is perfect or not
try:
    perfect = int(input("Enter a number to check perfect or not:"))
except ValueError:
    print("Enter +ve number only")
else:
    if(perfect < 2):
        print("Not a perfect number")
    else:
        sum = 0
        for i in range(1,perfect):
            if(perfect % i == 0):
                sum+=i
        if(perfect == sum):
            print(f'{perfect} is a perfect number')
        else:
            print(f'{perfect} is not a perfect number')

# GCD
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
while b > 0:
    rem = a % b
    a = b
    b = rem
GCD = a
print("GCD of two numbers is:", GCD)

# LCM
x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
if x > y:
    big = x
else:
    big = y
while True:
    if (big % x == 0) and (big % y == 0):
        LCM = big
        break
    big = big + 1
print("LCM of two numbers is:", LCM)