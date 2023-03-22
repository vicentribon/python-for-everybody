
## Why Program
#$ Exercise 1: What is the function of the secondary memory in a computer?
#% It´s function is to stored that will be saved and can be used even after the reboot of the machine.


#$ Exercise 2: What is a program?
#% A program is a basic a sequence of rules and instructions to solve a specificy problem. If follow correctly, the result will be the a desired one.


#$ Exercise 3: What is the difference between a compiler and an interpreter?
#% An interpreter reads the source code of the program as written by the programmer, parses (analisa) the source code, and interprets the instructions on the fly (em tempo real). Python is an interpreter and when we are running Python interactively, we can type a line of Python (a sentence) and Python processes it immediately and is ready for us to type another line of Python.
#* It translates python source code from a human readable form to machine code, it can analyze and execute a program line by line.

#% A compiler needs to be handed the entire program in a file, and then it runs a process to translate the high-level source code into machine language and then the compiler puts the resulting machine language into a file for later execution. 
#* It reads human readable programs, it takes the entire source code and produce object code or the executable.


#$ Exercise 4: Which of the following contains “machine code”?

#@ a) The Python interpreter
#@ b) The keyboard
#@ c) Python source file
#@ d) A word processing document

#% R: The Python interpreter, "A".


#$ Exercise 5: What is wrong with the following code:
"""
>>> primt 'Hello world!'
File "<stdin>", line 1
  primt 'Hello world!'
                     ^
SyntaxError: invalid syntax
>>>
"""

#% The mistake is in the syntaxe of the command "print" but in this code it is written as "primt".


#$ Exercise 6: Where in the computer is a variable such as “x” stored after the following Python line finishes?
#% This variable is stored in the main memory, in other words, in the CPU.