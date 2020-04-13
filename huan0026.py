""" 
Name: Ching Han Huang, 113510994

I use float function to represent the user-entered numbers, because 
float function can accept more possibile responses, and it is more precise. 
For example, the user can enter 5 with float function, but can not enter 5.1 with int function.
""" 

name = input("what is your name ? ")
print("Hi " + name)

number1 = float(input("Enter the first number : "))
number2 = float(input("Enter the second number : "))
number3 = float(input("Enter the third number : "))
average = (number1 + number2 + number3)/3
print("Thank you,", name,", the average of your numbers is", average)
