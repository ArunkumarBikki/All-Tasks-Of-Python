# Write a program to find the greatest of three numbers
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if num1>num2 and num1>num3:
    print(f"{num1} is greater than {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater than {num1} and {num2}")
elif num1==num2 and num1==num3:
    print("All the numbers are equal")

# Check if a year is a leap year
year = int(input("Enter a year to check leap or not"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
    print(f"{year} is a Leap Year")
else: 
    print(f"{year} is not a Leap Year")

# Write a program to classify a character entered by the user as a vowel, consonant, or neither.

# Calculate the grade of a student based on the marks they score: 
marks = float(input("Enter your marks:"))
if marks>=90 and marks<=100:
    print("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A")
elif marks>=70 and marks<80:
    print("Grade B+")
elif marks>=60 and marks<70:
    print("Grade B")
elif marks>=50 and marks<60:
    print("Grade C")
elif marks<0 or marks>100:
    print("Enter valid marks")
else:
    print("Fail")

# Write a program to check if three sides length form a valid triangle. 
a = float(input("Enter the length of first side"))
b = float(input("Enter the length of second side"))
c = float(input("Enter the length of third side"))
if a <= 0 or b <= 0 or c <= 0:
    print("The lengths of the sides must be greater than zero.")
elif a + b > c and b + c > a and c + a > b:
    print("It forms a valid triangle.")
else:
    print("It doesn't form a valid triangle.")
