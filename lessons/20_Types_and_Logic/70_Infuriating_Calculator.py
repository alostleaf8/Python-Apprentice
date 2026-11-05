"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things:

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)

Then use if-elif-else statements to perform the requested math operation on the
numbers and display the result.

If the user enters an unknown operation, display an error message
(use `messagebox.showerror()`).

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

from tkinter import messagebox, simpledialog, Tk # Import the required modules

window = Tk() # Create a window object

window.withdraw() # Hide the window, hint: use the withdraw method

number_1 =  simpledialog.askfloat("Your First Number", "Choose your first number") # Ask the user for the first number   

number_2 =  simpledialog.askfloat("Your Second Number", "Choose your second number") # Ask the user for the second number   

math_operation = simpledialog.askstring("Your Math Operation", "Choose your math operation from the following: addition, subtraction, multiplication, or division.")# Ask the user for the math operation

# variablessss
add = number_1 + number_2
subtract = number_1 - number_2
multiply = number_1 * number_2
try:
    divide = number_1 / number_2
except ZeroDivisionError:
     messagebox.showerror("", "Error          ")


# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if math_operation.lower()=="addition":
    messagebox.showinfo("Addition", add)
elif math_operation.lower()=="subtraction":
    messagebox.showinfo("Subtraction", subtract)
elif math_operation.lower()=="multiplication": 
    messagebox.showinfo("Multiplication", multiply)
elif math_operation.lower()=="division":
    messagebox.showinfo("Division", divide)
else:
    messagebox.showerror("", "Undefined Value          ")
# If the user enters an unknown operation, display an error message (use `messagebox.showerror()`).

window.mainloop()# Keep the window open
