
# ! Vinícius Project - Linear Systems Solution
# & Made by Lucas Vicente Ribon (RA: N6089G7) and João Carlos Alves (RA:)

# ? How to..
# * How to make the calculation - numpy
# file
# B = np.array([-1, 5])

# x= solve(A,B)
# print(x)

# * Reads the .csv file - pandas
#df = pd.read_csv('/home/lribon/Documents/coding/Trabalho-Vinicius/file.csv', header = None)
#print(df.values)

# * System libraries
import sys
import time
import os
# * Pandas library
import pandas as pd
# * Numpy library
import numpy as np
from numpy.linalg import solve

# ? Introduction
time.sleep(2)
print("######## Linear Systems Solution with Python ########")
time.sleep(2)
print("Program: Welcome to our program!")
time.sleep(3)
print("Program: Here we are going to r&solve some systems of linear equations with Python!")
time.sleep(2)
print("Program: Are you ready?")
time.sleep(2)

# ? Loop for user rewrite in case answer is wrong
while True : 
    answer = input("Program: Type (Yes/y) or (No/n): ")    
    # * Verify the answer
    if answer == "Yes" or answer == "y":
        print("User: ",answer)
        time.sleep(2)
        print("Program: Let's go then!")
        break
    elif answer == "No" or answer == "n":
        print("User: ",answer)
        time.sleep(2)
        print("Program: Oh.. Ok then, bye.")
        time.sleep(2)
        exit()
    elif answer == "&":
        print("User: ",answer)
        time.sleep(3)
        def delay_print(s):
            for c in s:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.15)
        delay_print("Program: ( 　ﾟ,_ゝﾟ)")
        def delay_print2(z):
            for c in z:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.15)
        delay_print2("\nProgram: congratulations, you have found a secret!")
        print("")
        exit()
    else :
        print("User: ", answer)
        time.sleep(2)
        print("Program: Wrong value! Try again!")
        time.sleep(2)
        continue

#? Main Code
# * Input path
time.sleep(2)
print("Program: Before we start, make sure your csv file has the last column named as 'result'!")
time.sleep(2)
csv_path = input("Program: Enter a valid file path to the csv file: ")
time.sleep(1)
print("User: ", csv_path)
time.sleep(2)

# * Verify Path
while not os.path.isfile(csv_path):
    print("Program: ERROR, That is not a valid file, try again...")
    csv_path = input("Program: Enter a valid path: ")
    time.sleep(1)
    print("User: ", csv_path)
    
    time.sleep(2)

# * If error not trigger, then...
try:
    dataf = pd.read_csv(csv_path, header=0)
    # * Solution of Lienar Equation
    result = dataf['result'] # & set the result column
    total_columns = dataf.shape[1] # & see the number of columns


    # * Conditional on the number of columns
    if total_columns == 1 or total_columns == 2:
        # & Verify if file have enough columns to calculate the result
        print("Program: The file does not contain the data needed to perform the linear system.")
        print('')
        time.sleep(2)
        exit()
    # * Show select file and values
    else:
        print("Program: This is the file you have selected:")
        time.sleep(2)
        array_xyz = dataf.iloc[:,:total_columns - 1]
        time.sleep(1)
        print(dataf)
        print('')
        time.sleep(2)
        
        # & Defining the variables
        matrix_xyz = np.array(array_xyz)
        vector_result_tresvar = np.array(result)
            
        # & Show values of the linear system
        time.sleep(2)
        # ? Array
        print("Program: This is the Array of variables")
        time.sleep(1)
        print(matrix_xyz)
        print('')
        time.sleep(3)
        # ? Vectors
        print("Program: Vectors - Result Column")
        time.sleep(1)
        print(vector_result_tresvar)
        print('')
        time.sleep(3)
        # ? Calculating
        print("Program: Calculating...")
        time.sleep(2)
        print("Program: Done!")
        print('')
        time.sleep(2)
        
        # & Solving the linear equation
        print("Linear System Result")
        time.sleep(2)
        sistema_tresvar = solve(matrix_xyz, vector_result_tresvar)
        print(sistema_tresvar)
        print('')

except BaseException as exception:
    print(f"An exception occurred: {exception}")

# ? Credits
time.sleep(2)
print('Program: This code was made by Lucas Ribon and João Carlos!')
time.sleep(2)
print('Program: Thank you for seeing your project!')