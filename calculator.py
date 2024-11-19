import tkinter as tk

def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create labels
tk.Label(root, text="First Number").grid(row=0, column=0)
tk.Label(root, text="Second Number").grid(row=1, column=0)
tk.Label(root, text="Result").grid(row=2, column=0)

# Create a variable to hold the result
result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=2, column=1)

# Create buttons
tk.Button(root, text="Add", command=add).grid(row=3, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=3, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=4, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=4, column=1)

# Start the GUI event loop
root.mainloop()