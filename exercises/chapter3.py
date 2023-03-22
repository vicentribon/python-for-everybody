import time

## Values and Types
#$ Exercise 1: Write a program that uses input to prompt a user for their name and then welcomes them.

"""
name = input("Enter your name: ")
print("Welcome", name,"!")
"""

#$ Exercise 2: Write a program to prompt the user for hours and rate per hour to compute gross pay.

"""
hours_worked = input("Enter value: ")
hour_value = input("Enter value: ")

pay = float(hours_worked) * float(hour_value)
print("You gain: ", pay)
"""

#$ Exercise 3: Assume that we execute the following assignment statements:

#% width = 17
#% height = 12.0

"""
width = 17
height = 12.0

time.sleep(1.5)
var1 = int(width) // 2
print("The floor division between 'width' and 2 is: ", var1)

time.sleep(1.5)
var2 = float(width) / 2.0
print("The division between 'width' and 2 is: ", var2)

time.sleep(1.5)
var3 = float(height) / 3
print("The division between 'height' and 2 is: ", var3)

time.sleep(1.5)
var4 = 1 + 2 * 5
print("Look this math man, insane (. _.)--C  ", var4)
"""

#$ Exercise 4: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

"""
tempC = input("Enter the temperature in C°: ")

print("Ok! Let´s transform this to F°")
time.sleep(2)
print("Calculating...")
time.sleep(2)
print("Done!")
time.sleep(1)


tempF =  float(tempC) * 1.8 + 32
print("The temperature in F° is: ", tempF)
"""