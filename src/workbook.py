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
