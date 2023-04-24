## Loops and Iterations

#$ Write a "while" loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

import time
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', '¨', '§', 'ª', 'º', '°', '¢', '£', '¬']
numbers = ['0','1','2','3','4','5','6','7','8','9']

#% Functions
def word_check():
    while True:
        usr_enter = input("User: ")
        try:
            if any(c in (symbols) for c in usr_enter):
                print("ERROR: The word can't contain special caracters!")
                continue
            elif any(c in (numbers) for c in usr_enter):
                print("ERROR: The word can't contain numbers!")
                continue
            else:
                print("Word choosed by the user: ",usr_enter)
                break
        except:
            print("ERROR: Unknow error.")        
    return usr_enter

#% Code
print("Program: Welcome to the backwards word counting!")
while True:
    #% Start
    print("Program: Enter your word")
    usr_enter = word_check()

    #% Define Index
    index = -1
    for i in usr_enter:
        if(i.isalnum()):
            index += 1
    time.sleep(1)
    
    #% Print letters
    while index > -1:
        letter = usr_enter[index]
        print(*letter)
        time.sleep(1)
        index = index - 1
    time.sleep(1)
    
    #% Ending
    print("""
Program: Do you want to do it again?
Program: Yes / No """)
    answer_repeat = input("User: ")
    time.sleep(1)
    
    #% Conditional Chain
    if answer_repeat in ("Yes", "YES", "yes", "Y", "y"):
        print("Program: Ok, so lets begin again!")
        time.sleep(1)
        continue
    elif answer_repeat in ("No", "NO", "no", "N", "n"):
        print("Program: Thanks for using our backwards letter counting!")
        time.sleep(1)
        exit()
    else:
        print("Program: Please enter a valid option.")
        continue

    