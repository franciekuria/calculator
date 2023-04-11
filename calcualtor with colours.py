import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Number Calculator")

# Create a label to display the numbers entered
number_label = tk.Label(root, text="0", width=20, height=2)
number_label.grid(row=0, column=0, columnspan=4)

# Define a function to update the number_label with the button pressed
def update_label(number):
    current_number = number_label.cget("text")
    if current_number == "0":
        current_number = ""
    number_label.config(text=current_number + str(number))

# Define a function to clear the number_label
def clear_label():
    number_label.config(text="0")

# Define a function to calculate the result
def calculate_result():
    result = eval(number_label.cget("text"))
    number_label.config(text=result)

# Create the number buttons
for i in range(1, 10):
    button = tk.Button(root, text=str(i), width=5, height=2, bg="black", fg="white", command=lambda x=i: update_label(x))
    button.grid(row=((i-1)//3)+1, column=((i-1)%3))

# Create the zero button
button_zero = tk.Button(root, text="0", width=5, height=2, bg="black", fg="white", command=lambda: update_label(0))
button_zero.grid(row=4, column=1)

# Create the clear button
button_clear = tk.Button(root, text="C", width=5, height=2, bg="red", fg="white", command=clear_label)
button_clear.grid(row=4, column=0)

# Create the equal button
button_equal = tk.Button(root, text="=", width=5, height=2, bg="green", fg="white", command=calculate_result)
button_equal.grid(row=4, column=2)

# Create the addition button
button_add = tk.Button(root, text="+", width=5, height=2, bg="blue", fg="white", command=lambda: update_label("+"))
button_add.grid(row=1, column=3)

# Create the subtraction button
button_subtract = tk.Button(root, text="-", width=5, height=2, bg="blue", fg="white", command=lambda: update_label("-"))
button_subtract.grid(row=2, column=3)

# Create the multiplication button
button_multiply = tk.Button(root, text="*", width=5, height=2, bg="blue", fg="white", command=lambda: update_label("*"))
button_multiply.grid(row=3, column=3)

# Create the division button
button_divide = tk.Button(root, text="/", width=5, height=2, bg="blue", fg="white", command=lambda: update_label("/"))
button_divide.grid(row=4, column=3)

# Run the main loop
root.mainloop()
