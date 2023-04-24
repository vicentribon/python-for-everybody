import time
#% Variable
x = None
result = None
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


#% Functions
def usrselect():
    while True:
        userinput = input("> ")
        try:
            value = int(userinput)
            if 0 < int(userinput) < 5:
                break
            else :
                print("Program: ERROR, this option is invalid!")
                continue
        except ValueError:
            print("Program: ERROR, input is not a number!")
            continue
    return userinput

def optionchosed():
    global x
    if userinput == "1":
        x = "Program: You choose '+'."
    elif userinput == "2":
        x = "Program: You choose '-'."
    elif userinput == "3":
        x = "Program: You choose '*'."
    elif userinput == "2":
        x = "Program: You choose '/'."
    return x
        
def selectnum1():
    while True:
        num1 = input("> ")
        try:
            value = float(num1)
            break
        except ValueError:
            print("Program: ERROR, enter a valid number!")
            continue
    return num1

def selectnum2():
    while True:
        num2 = input("> ")
        try:
            value = float(num2)
            break
        except ValueError:
            print("Program: ERROR, enter a valid number!")
            continue
    return num2
        
def cacloptions():
    global result
    #$ Addup
    if userinput == "1":
        result = float(num1) + float(num2)
        #print(num1, "+", num2, "=", float(result))
    #$ Subtract
    elif userinput == "2":
        result = float(num1) - float(num2)
        #print(num1, "-", num2, "=", float(result))
    #$ Multiply
    elif userinput == "3":
        result = float(num1) * float(num2)
        #print(num1, "-", num2, "=", float(result))
    #$ Division
    elif userinput == "4":
        result = float(num1) / float(num2)
        #print(num1, "-", num2, "=", float(result))
    return result



#$ Introduction
print("--- Welcome to My Calculator ---")
time.sleep(2)
#% Main Code
while True:
    print("Program: Options")
    print("""
1 - Addup    --> "+"
2 - Subtract --> "-"
3 - Multiply --> "*"
4 - Division --> "/"
    """)
    time.sleep(1)
    
    #$ First input (option)
    print("Program: Please select an option:")
    userinput = usrselect()
    print(optionchosed())

    #$ Select the numbers
    #* Num1
    print("Program: Enter number one: ")
    num1 = selectnum1()

    time.sleep(0.5)

    #* Num2
    print("Program: Enter number two: ")
    num2 = selectnum2()

    #$ Calc
    time.sleep(1)
    print("Program: Calculating...")
    time.sleep(1)
    print("Program: The result is:", cacloptions())
    time.sleep(1.5)
    
    #$ Repeat?
    print("Program: Do you want do repeat?")
    print("Program:  Yes / No")
    #* Repeat Action
    usr_repeat = input("> ")
    if usr_repeat in ("YES", "Yes", "yes", "Y", "y"):
        print("Program: Ok! Let's go back then!")
        time.sleep(1)
        continue
    elif usr_repeat in ("NO", "No", "no", "N", "n"):
        time.sleep(1)
        print("Thanks for using My Calculator, made by Ribon.")
        exit()


    
