
## Functions
#$ Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

import random
import time

"""
## loop that generates 10 random numbers
for i in range(10):
    x = random.random()
    print(x)

time.sleep(1)
print("Ok")
time.sleep(1)

## randint take a random number between "low" and "high" parameters
print(random.randint(1, 20))

## choice pick a random number of the list
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(t))
"""


#$ Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.

#% A Error occours because the function "repeat_lyrics" isn´t definied yet, the line to use is in the top instead of being in the bottom

"""
repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()
"""


#$ Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?

#% The code works because even if the definition of the function "print_lycrs"(1) is defined after the the use of it in the "repeat_lyrics"(2), the use of the (2) is after the (1) definition, so the code have the definition in the end.

"""
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
"""


#$ Exercise 4: What is the purpose of the “def” keyword in Python?

#% It indicates that the following indented section of code is to be stored for later


#$ Exercise 5: What will the following Python program print out?

#% It will print: ABC, ZAP and ABC 

"""
def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()
"""


#$ Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

"""
def computepay(hourwrk, rate) :
    try:
        hourwrk = float(hourwrk)
        rate = float(rate)
        if hourwrk > 40 :
            payment = ((hourwrk - 40) * (rate * 1.5)) + (40 * rate)
        else:
            payment = hourwrk * rate
        return payment
    except:
        print("Enter a valid number.")

print(computepay(hourwrk = input("Enter your hours: "), rate = input("Enter your hours: ")))
"""


#$ Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

"""
def computepay(score):
    try:
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
        return my_score
    except:
        print("Enter a valid number")

print(computepay(my_score = input("Enter your score: ")))
"""
