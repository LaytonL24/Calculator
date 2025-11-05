import tkinter 

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_length = len(button_values) #5
column_length = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

root = tkinter.Tk()
root.title("Calculator")
root.resizable(False,False)

frame = tkinter.Frame(root)
label = tkinter.Label(frame, text="0",font=("Arial",45),background=color_black,
                      foreground=color_white, anchor="e", width=column_length)

label.grid(row=0,column=0,columnspan=column_length, sticky="we")

# Iterate
for row in range(row_length):
    for column in range(column_length):
        value = button_values[row][column]
        button = tkinter.Button(frame,text=value,font=("Arial",30), width=column_length-1, 
                                height=1,command=lambda value=value: button_clicked(value))
        # Determine button colors
        if value in top_symbols:
            button.config(foreground=color_black,background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        
        button.grid(row=row+1, column=column)

frame.pack()

# Global Variables
A = "0"
operator = None
B = None

# Function to clear everything
def clear():
    global A, operator, B
    A = "0"
    operator = None
    B = None

# Removes decimals from whole numbers with trailing 0 
def whole_number(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

# Function to handle button clicked for right side of calculator
def handle_r_s(value):
    global label, A, B, operator

    if value == "=":
        if A is not None and operator is not None:
            B = label["text"]
            num1 = float(A)
            num2 = float(B)

            if operator == "+":
                label["text"] = whole_number(num1 + num2)
            elif operator == "-":
                label["text"] = whole_number(num1 - num2)
            elif operator == "×":
                label["text"] = whole_number(num1 * num2)
            elif operator == "÷":
                label["text"] = whole_number(num1 / num2)

            clear()

    elif value in "+-×÷": 
        if operator is None:
            A = label["text"]
            label["text"] = "0"
            B = "0"
        
        operator = value

# Function to handle button clicked for right side of calculator
def handle_t_s(value):
    global label, A, B, operator
    if value == "AC":
        clear()
        label["text"] = "0"

    elif value == "+/-":
        result = float(label["text"]) * -1
        label["text"] = whole_number(result)

    elif value == "%":
        percented = float(label["text"]) / 100
        label["text"] = whole_number(percented)

# Main to do all operations for calculator
def button_clicked(value):
    global right_symbols, top_symbols, label

    if value in right_symbols:
        handle_r_s(value)

    elif value in top_symbols:
        handle_t_s(value)

    else: # digits . or sqaure root
        if value == ".":
            if value not in label["text"]:
                label["text"] += value

        elif value == "√":
            s_root = float(label["text"]) ** 0.5
            label["text"] = whole_number(s_root)

        elif value in "0123456789":
            if label["text"] == "0": 
                label["text"] = value # Replace 05 with 5
            else:
                label["text"] += value # Add digit

root.mainloop()