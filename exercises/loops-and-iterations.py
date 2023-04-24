
## Loops and Iterations

#% An example of a "while" loop:
"""
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
"""


#% Example of a infinite loop with the statement "True" that only stop when the user input the string done
"""
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')
"""

#% loop that copies its input until the user types “done”, but treats lines that start with the hash character as lines not to be printed
"""
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
"""


#% loop that print all the elements of a list
"""
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
"""

#% loop that count a the number of elements in a list using the variable itervar
#$ while the var "itervar" is not used in the loop body, it control the loop for each item inside the list

"""
count = 0
for itervar in ["bruh", "bruh1", "bruh2","bruh3", "bruh4"]:
    count = count + 1
print('Count: ', count)
"""

#% loop that see the values on a list and each time the cicle is done, the loop adds the values to the "total" var
"""
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)
"""

"""
largest = None
# Defini essa var com None, então ela é considerada vazia mas pode ser preenchida
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        # A primeira lógica verifica se largest está vazio, isso serve para a primeira execução do loop
        # Já a segunda veririca se o itervar é maior que o largest, se sim ele considera o itervar como maior. Lembrando que ele só sera executado quando o valor de itervar for maior que o largest, caso contrário ele pulará e irá para o print.
        # Para procurar qual o
        largest = itervar
        # a var largest será igual a itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
"""

#$ Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


"""
total = 0
count = 0

while True:
    line = input("> ")
    try:   
        # If input is equal "done" stop code
        if line == "done":
            break
        else:
        # If input is a number, verifiy it, if is save input and add to total
            line = float(line)
            print(">", line)
            # Count of all the numbers that the user input
            count = line
            # Total of numbers input
            total = total + line
            # The avarege of the numbers input
            avarege = total / count
    except:
        # If input not a number, report error
        print("Please enter a valid number")
        continue
# Print the results
print('Soma: ', total)       
print('Total: ', count)
print('Média: ', avarege)
"""


#$ Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

"""
list = []

while True:
    line = input("> ")
    try:   
        # If input is equal "done" stop code
        if line == "done":
            break
        else:
        # If input is a number, verifiy it, if is save input and add to total
            line = float(line)
            print(">", line)
            list.append(line)
    except:
        # If input not a number, report error
        print("Please enter a valid number")
        continue
print(list)
print('Maior valor: ', max(list))
print('Menor valor: ', min(list))
"""


