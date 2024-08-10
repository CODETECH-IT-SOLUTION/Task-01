import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + number)

def clear_display():
    display.delete(0, tk.END)

def clear_previous():
    current = display.get()
    if current:
        display.delete(len(current) - 1, tk.END)

def perform_operation(operation):
    global num1
    global operator
    num1 = float(display.get())
    operator = operation
    display.delete(0, tk.END)

def calculate_result():
    global num1
    global operator
    num2_str = display.get()
    num2 = 0  # Initialize num2

    if operator == "%":
        num2 = float(num2_str) / 100
        result = num1 * num2
    else:
        num2 = float(num2_str)
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
    display.delete(0, tk.END)
    display.insert(0, result)

# Create main window
window = tk.Tk()
window.title("Calculator")

# Create display
display = tk.Entry(window, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
button_ac = tk.Button(window, text="AC", width=5, height=2, command=clear_display)
button_ac.grid(row=1, column=0, padx=5, pady=5)

button_percentage = tk.Button(window, text="C", width=5, height=2, command=clear_previous)
button_percentage.grid(row=1, column=1, padx=5, pady=5)

button_backspace = tk.Button(window, text="%", width=5, height=2, command=lambda: button_click("%"))
button_backspace.grid(row=1, column=2, padx=5, pady=5)

button_division = tk.Button(window, text="÷", width=5, height=2, command=lambda: perform_operation("/"))
button_division.grid(row=1, column=3, padx=5, pady=5)

button_7 = tk.Button(window, text="7", width=5, height=2, command=lambda: button_click("7"))
button_7.grid(row=2, column=0, padx=5, pady=5)

button_8 = tk.Button(window, text="8", width=5, height=2, command=lambda: button_click("8"))
button_8.grid(row=2, column=1, padx=5, pady=5)

button_9 = tk.Button(window, text="9", width=5, height=2, command=lambda: button_click("9"))
button_9.grid(row=2, column=2, padx=5, pady=5)

button_multiplication = tk.Button(window, text="×", width=5, height=2, command=lambda: perform_operation("*"))
button_multiplication.grid(row=2, column=3, padx=5, pady=5)

button_4 = tk.Button(window, text="4", width=5, height=2, command=lambda: button_click("4"))
button_4.grid(row=3, column=0, padx=5, pady=5)

button_5 = tk.Button(window, text="5", width=5, height=2, command=lambda: button_click("5"))
button_5.grid(row=3, column=1, padx=5, pady=5)

button_6 = tk.Button(window, text="6", width=5, height=2, command=lambda: button_click("6"))
button_6.grid(row=3, column=2, padx=5, pady=5)

button_subtraction = tk.Button(window, text="−", width=5, height=2, command=lambda: perform_operation("-"))
button_subtraction.grid(row=3, column=3, padx=5, pady=5)

button_1 = tk.Button(window, text="1", width=5, height=2, command=lambda: button_click("1"))
button_1.grid(row=4, column=0, padx=5, pady=5)

button_2 = tk.Button(window, text="2", width=5, height=2, command=lambda: button_click("2"))
button_2.grid(row=4, column=1, padx=5, pady=5)

button_3 = tk.Button(window, text="3", width=5, height=2, command=lambda: button_click("3"))
button_3.grid(row=4, column=2, padx=5, pady=5)

button_addition = tk.Button(window, text="+", width=5, height=2, command=lambda: perform_operation("+"))
button_addition.grid(row=4, column=3, padx=5, pady=5)

button_00 = tk.Button(window, text="00", width=5, height=2, command=lambda: button_click("00"))
button_00.grid(row=5, column=0, padx=5, pady=5)

button_0 = tk.Button(window, text="0", width=5, height=2, command=lambda: button_click("0"))
button_0.grid(row=5, column=1, padx=5, pady=5)

button_dot = tk.Button(window, text=".", width=5, height=2, command=lambda: button_click("."))
button_dot.grid(row=5, column=2, padx=5, pady=5)

button_equals = tk.Button(window, text="=", width=5, height=2, command=calculate_result, bg="orange")
button_equals.grid(row=5, column=3, padx=5, pady=5)

window.mainloop()