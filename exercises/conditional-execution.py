
## Conditional Execution
#$ Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

"""
## Vars
hours_worked = float(input("Enter hours worked: ")) 
rate = float(input("Enter your rate: ")) 

## Logic Conditional
if hours_worked <= 40 and hours_worked > 0 :
    payment = hours_worked * rate
    print("This is your payment: ", payment)
elif hours_worked > 40 :
    payment = ((hours_worked - 40) * (1.5 * rate)) + (40 * rate)
    print("This is your payment: ", payment)
else :
    print("Bro, u didn´t worked.")
"""

#$ Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

"""
## Var
hours_worked = input("Enter hours worked: ") 
rate = input("Enter your rate: ")

## Try, make sure the user input a number
try :
    hours_worked = float(hours_worked)
    rate = float(rate)

    if hours_worked <= 40 and hours_worked > 0 :
        payment = hours_worked * rate
        print("This is your payment: ", payment)
    elif hours_worked > 40 :
        payment = ((hours_worked - 40) * (1.5 * rate)) + (40 * rate)
        print("This is your payment: ", payment)
    else :
        print("Bro, u didn´t worked.")
## Except, if user input a letter, shows a error msg
except :
    print("ERROR: Please insert a number!")
"""


#$ Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

"""
## Vars
my_score = input("Please insert your score between '0.0' and '1.0': ")

## Conditionals to define your grade based on input
try :
    my_score = float(my_score)
    if my_score >= 0 and my_score < 0.6 :
        print("You got an F")
    elif my_score >= 0.6 and my_score < 0.7 :
        print("You got an D")
    elif my_score >= 0.7 and my_score < 0.8 :
        print("You got an C")
    elif my_score >= 0.8 and my_score < 0.9 :
        print("You got an B")
    elif my_score <= 1 and my_score > 0.9 :
        print("You got an A")
## If input is no a number, show error msg
except :
    print("Out of range")
"""



















