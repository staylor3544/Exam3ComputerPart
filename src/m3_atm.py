import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# grid is 6 rows and 3 columns
# 

window = tk.Tk()
window.title("ATM")

atm_frame = tk.Frame(
    window,
    width = 200, 
    height = 200, 
    bg = "#F48F85")
atm_frame.configure(borderwidth = 3, relief = 'sunken')
atm_frame.grid_propagate(0)
atm_frame.grid(column=1, row=1, pady=5, padx=5, sticky="e")

balance_label = tk.Label(
    atm_frame,
    text = "Amount ($):",
    fg = "#C00425",
    bg = "#FFCCBB",
)
balance_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

amount_label = tk.Label(
    atm_frame,
    text = "",
    fg = "#C00425",
    bg = "#FFCCBB"
)
amount_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

def digit_handler(digit):
    current_amount = amount_label.cget("text")
    amount_label.config(text=current_amount + str(digit))

button1 = tk.Button(
    atm_frame,
    text = "1",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button1.grid(column=1, row=3)

button2 = tk.Button(
    atm_frame,
    text = "2",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button2.grid(column=2, row=3)

button3 = tk.Button(
    atm_frame,
    text = "3",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button3.grid(column=3, row=3)

button4 = tk.Button(
    atm_frame,
    text = "4",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button4.grid(column=1, row=4)

button5 = tk.Button(
    atm_frame,
    text = "5",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button5.grid(column=2, row=4)

button6 = tk.Button(
    atm_frame,
    text = "6",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button6.grid(column=3, row=4)

button7 = tk.Button(
    atm_frame,
    text = "7",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button7.grid(column=1, row=5)

button8 = tk.Button(
    atm_frame,
    text = "8",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button8.grid(column=2, row=5)

button9 = tk.Button(
    atm_frame,
    text = "9",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
button9.grid(column=3, row=5)

def withdrawal_handler():
    current_balance = float(balance_label.cget("text"))
    amount = float(amount_label.cget("text"))
    new_balance = current_balance - amount
    balance_label.config(text=str(new_balance))
    amount_label.config(text="")


withdrawl_button = tk.Button(
    atm_frame,
    text = "Withdrawl",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75
)
withdrawl_button.grid(column=1, row=6)

def deposit_handler():
    current_balance = float(balance_label.cget("text"))
    amount = float(amount_label.cget("text"))
    new_balance = current_balance + amount
    balance_label.config(text=str(new_balance))
    amount_label.config(text="")

deposit_button = tk.Button(
    atm_frame,
    text = "Deposit",
    fg = "#C00425",
    bg = "#FFCCBB",
    height = 75,
    width = 75,
    command = deposit_handler
)
deposit_button.grid(column=3, row=6)



window.mainloop()

import tkinter as tk


window = tk.Tk()
window.title("ATM")  


atm_frame = tk.Frame(
    window,
    width=200,
    height=200,
    bg="#F48F85"
)
atm_frame.configure(borderwidth=3, relief='sunken')
atm_frame.grid(column=1, row=1, pady=5, padx=5, sticky="e")


amount_label = tk.Label(
    atm_frame,
    text="Amount ($):",
    fg="#C00425",
    bg="#FFCCBB"
)
amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")


amount_value_label = tk.Label(
    atm_frame,
    text="",
    fg="#C00425",
    bg="#FFCCBB"
)
amount_value_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

def digit_handler(digit):
    current_amount = amount_value_label.cget("text")
    amount_value_label.config(text=current_amount + str(digit))

for i in range(1, 10):
    digit = str(i)
    button = tk.Button(
        atm_frame,
        text=digit,
        fg="#C00425",
        bg="#FFCCBB",
        height=75,
        width=75,
        command=lambda digit=digit: digit_handler(digit)
    )
    button.grid(column=(i-1) % 3, row=(i-1) // 3 + 2)


def withdrawal_handler():
    current_balance = float(balance_label.cget("text"))
    amount = float(amount_value_label.cget("text"))
    new_balance = current_balance - amount
    balance_label.config(text=str(new_balance))
    amount_value_label.config(text="")

withdrawal_button = tk.Button(
    atm_frame,
    text="Withdrawal",
    fg="#C00425",
    bg="#FFCCBB",
    height=75,
    width=75,
    command=withdrawal_handler
)
withdrawal_button.grid(column=0, row=5)

def deposit_handler():
    current_balance = float(balance_label.cget("text"))
    amount = float(amount_value_label.cget("text"))
    new_balance = current_balance + amount
    balance_label.config(text=str(new_balance))
    amount_value_label.config(text="")

deposit_button = tk.Button(
    atm_frame,
    text="Deposit",
    fg="#C00425",
    bg="#FFCCBB",
    height=75,
    width=75,
    command=deposit_handler
)
deposit_button.grid(column=2, row=5)


balance_label = tk.Label(
    atm_frame,
    text="Current Balance ($):",
    fg="#C00425",
    bg="#FFCCBB"
)
balance_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")

balance_amount_label = tk.Label(
    atm_frame,
    text="1000", 
    fg="#C00425",
    bg="#FFCCBB"
)
balance_amount_label.grid(row=6, column=1, padx=10, pady=10, sticky="w")


window.update_idletasks()
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.geometry("+%d+%d" % (x, y))

window.mainloop()
