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
# DONE: 2. (3 pts)
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
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
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
# DONE: 5. (10 pts)
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
# DONE: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

initial_balance = 1000  

def digit_handler(digit):
    current_amount = amount_label.cget("text")
    amount_label.config(text=current_amount + str(digit))

def withdrawal_handler():
    current_balance = int(current_balance_label.cget("text"))  
    amount = int(amount_label.cget("text")) if amount_label.cget("text") else 0
    new_balance = current_balance - amount
    current_balance_label.config(text=str(new_balance)) 
    amount_label.config(text="")

def deposit_handler():
    current_balance = int(current_balance_label.cget("text"))  
    amount = int(amount_label.cget("text")) if amount_label.cget("text") else 0
    new_balance = current_balance + amount
    current_balance_label.config(text=str(new_balance)) 
    amount_label.config(text="")

window = tk.Tk()
window.title("ATM")

balance_frame = tk.Frame(window)
balance_frame.grid(row=0, column=0, columnspan=3)
balance_label = tk.Label(balance_frame, text="Current Balance ($):")
balance_label.grid(row=0, column=0)
current_balance_label = tk.Label(balance_frame, text=initial_balance)  
current_balance_label.grid(row=1, column=0, columnspan=3)

amount_frame = tk.Frame(window)
amount_frame.grid(row=1, column=0, columnspan=3)
amount_label_text = tk.Label(amount_frame, text="Amount ($):")
amount_label_text.grid(row=0, column=0)
amount_label = tk.Label(amount_frame, text="")
amount_label.grid(row=1, column=0, columnspan=3)

button_frame = tk.Frame(window)
button_frame.grid(row=2, column=0, columnspan=3, rowspan=4)
button_frame.grid_columnconfigure([0,1,2], minsize=75)
button_frame.grid_rowconfigure([0,1,2,3], minsize=75)

digits = "1234567890"
row = 0
col = 0
for digit in digits:
    button = tk.Button(
        button_frame, 
        text=digit, 
        command=lambda d=digit: digit_handler(d),
        width=7,  
        height=3, 
    )
    button.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 2:
        col = 0
        row += 1

withdraw_button = tk.Button(
    button_frame, 
    text="Withdrawl", 
    command=withdrawal_handler,
    width=7,  
    height=3, 
)
withdraw_button.grid(row=row, column=0, sticky="nsew")

deposit_button = tk.Button(
    button_frame, 
    text="Deposit", 
    command=deposit_handler,
    width=7,  
    height=3, 
)
deposit_button.grid(row=row, column=2, sticky="nsew")

def keypress(event):
    key = event.char
    if key.isdigit():
        digit_handler(key)

window.bind("<Key>", keypress)

window.mainloop()

