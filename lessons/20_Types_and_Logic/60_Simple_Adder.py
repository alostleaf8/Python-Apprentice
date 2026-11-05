"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
50_My_Ages.py, to figure out how to complete the program.
"""

from tkinter import messagebox, simpledialog, Tk # Import the required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window, hint: use the withdraw method

number_1 =  simpledialog.askfloat("Your First Number", "Choose your first number") # Ask the user for the first number   

number_2 =  simpledialog.askfloat("Your Second Number", "Choose your second number") # Ask the user for the second number
sum = number_1 + number_2
messagebox.showinfo("","The sum of your two numbers is " + str(sum))  # Display the sum of the two numbers

window.mainloop() # Keep the window open