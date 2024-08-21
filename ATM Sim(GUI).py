import tkinter as tk
from tkinter import messagebox
import pyodbc

# Database connection
connection_string = 'DRIVER={SQL Server};SERVER=XPS-15;DATABASE=ATM;Trusted_Connection=yes;'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Global variable for current user
current_user = None

def signup():
    username = entry_username_signup.get()
    password = entry_password_signup.get()
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Username already exists.")
        return
    cursor.execute("INSERT INTO Users (Username, Password, Balance) VALUES (?, ?, 0.00)", (username, password))
    conn.commit()
    entry_username_signup.delete(0, tk.END)
    entry_password_signup.delete(0, tk.END)
    messagebox.showinfo("Success", "Sign-up successful.")
    switch_frame(frame_signin)

def signin():
    global current_user
    username = entry_username_signin.get()
    password = entry_password_signin.get()
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
    if cursor.fetchone():
        current_user = username
        label_current_user.config(text=f"Logged in as: {current_user}")
        switch_frame(f_main)
        update_balance()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def update_balance():
    cursor.execute("SELECT Balance FROM Users WHERE Username = ?", (current_user,))
    balance = cursor.fetchone()[0]
    label_balance.config(text=f"Balance: ${balance:.2f}")

def deposit():
    amount = entry_amount.get()
    if not amount or not amount.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Invalid amount.")
        return
    amount = float(amount)
    cursor.execute("UPDATE Users SET Balance = Balance + ? WHERE Username = ?", (amount, current_user))
    conn.commit()
    update_balance()
    entry_amount.delete(0, tk.END)
    messagebox.showinfo("Success", "Deposit successful.")

def withdraw():
    amount = entry_amount.get()
    if not amount or not amount.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Invalid amount.")
        return
    amount = float(amount)
    cursor.execute("SELECT Balance FROM Users WHERE Username = ?", (current_user,))
    balance = cursor.fetchone()[0]
    if amount > balance:
        messagebox.showerror("Error", "Insufficient balance.")
        return
    cursor.execute("UPDATE Users SET Balance = Balance - ? WHERE Username = ?", (amount, current_user))
    conn.commit()
    update_balance()
    entry_amount.delete(0, tk.END)
    messagebox.showinfo("Success", "Withdrawal successful.")

def reset_password():
    username = entry_username_signin.get()
    password = entry_password_signin.get()
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    cursor.execute("UPDATE Users SET Password = ? WHERE Username = ?", (password, username))
    conn.commit()
    messagebox.showinfo("Success", "Password reset successful.")

def delete_account(username):
    if not username:
        messagebox.showerror("Error", "No user is currently logged in.")
        return
    cursor.execute("DELETE FROM Users WHERE Username = ?", (username,))
    conn.commit()
    global current_user
    current_user = None
    label_current_user.config(text="")
    switch_frame(frame_signin)
    messagebox.showinfo("Success", "Account deleted successfully.")

def switch_frame(frame):
    frame_signup.pack_forget()
    frame_signin.pack_forget()
    f_main.pack_forget()
    frame.pack(fill='both', expand=True)

def toggle_to_signup():
    switch_frame(frame_signup)

def toggle_to_signin():
    switch_frame(frame_signin)

# Initialize main window
root = tk.Tk()
root.title("ATM Simulator")
root.geometry("900x510")
root.resizable(False, False)

# Color scheme
primaryColor = "#212121"
secondaryColor = "#1DA756"
primShade = "#303030"
secondaryShade = "#136C38"

# Frame for sign up
frame_signup = tk.Frame(root, bg=primaryColor)
frame_signup.pack(fill='both', expand=True)

tk.Label(frame_signup, text="Sign Up", font=('Arial', 24, 'bold'), fg=secondaryColor, bg=primaryColor).pack(pady=20)
tk.Label(frame_signup, text="Username", bg=primaryColor, fg=secondaryColor).pack()
entry_username_signup = tk.Entry(frame_signup, bg=primShade, fg="#ffffff", insertbackground="#ffffff")
entry_username_signup.pack()
tk.Label(frame_signup, text="Password", bg=primaryColor, fg=secondaryColor).pack()
entry_password_signup = tk.Entry(frame_signup, bg=primShade, fg="#ffffff", insertbackground="#ffffff", show='*')
entry_password_signup.pack()
tk.Button(frame_signup, text="Sign Up", bg=secondaryColor, fg=primaryColor, command=signup).pack(pady=20)
tk.Button(frame_signup, text="Already have an account? Sign In", bg=primaryColor, fg=secondaryColor, command=toggle_to_signin).pack(pady=10)

# Frame for sign in
frame_signin = tk.Frame(root, bg=primaryColor)
frame_signin.pack(fill='both', expand=True)

tk.Label(frame_signin, text="Sign In", font=('Arial', 24, 'bold'), fg=secondaryColor, bg=primaryColor).pack(pady=20)
tk.Label(frame_signin, text="Username", bg=primaryColor, fg=secondaryColor).pack()
entry_username_signin = tk.Entry(frame_signin, bg=primShade, fg="#ffffff", insertbackground="#ffffff")
entry_username_signin.pack()
tk.Label(frame_signin, text="Password", bg=primaryColor, fg=secondaryColor).pack()
entry_password_signin = tk.Entry(frame_signin, bg=primShade, fg="#ffffff", insertbackground="#ffffff", show='*')
entry_password_signin.pack()
tk.Button(frame_signin, text="Sign In", bg=secondaryColor, fg=primaryColor, command=signin).pack(pady=20)
tk.Button(frame_signin, text="Create an account", bg=primaryColor, fg=secondaryColor, command=toggle_to_signup).pack(pady=10)
tk.Button(frame_signin, text="Reset Password", bg=secondaryColor, fg=primaryColor, command=reset_password).pack(pady=20)

# Frame for main ATM features
f_main = tk.Frame(root, bg=primaryColor)

tk.Label(f_main, text="Welcome", font=('Arial', 24, 'bold'), fg=secondaryColor, bg=primaryColor).pack(pady=20)
tk.Label(f_main, text="Logged in as:", font=('Arial', 16), fg=secondaryColor, bg=primaryColor).pack()
label_current_user = tk.Label(f_main, text="", font=('Arial', 16), fg=secondaryColor, bg=primaryColor)
label_current_user.pack()

label_balance = tk.Label(f_main, text="Balance: $0.00", font=('Arial', 20), fg=secondaryColor, bg=primaryColor)
label_balance.pack()

tk.Label(f_main, text="Amount", bg=primaryColor, fg=secondaryColor).pack()
entry_amount = tk.Entry(f_main, bg=primShade, fg="#ffffff", insertbackground="#ffffff")
entry_amount.pack()

tk.Button(f_main, text="Deposit", bg=secondaryColor, fg=primaryColor, command=deposit).pack(pady=10)
tk.Button(f_main, text="Withdraw", bg=secondaryColor, fg=primaryColor, command=withdraw).pack(pady=10)
tk.Button(f_main, text="Delete Account", bg="#FF4D4D", fg="#ffffff", command=lambda: delete_account(current_user)).pack(pady=10)
tk.Button(f_main, text="Sign Out", bg="#FF4D4D", fg="#ffffff", command=lambda: switch_frame(frame_signin)).pack(pady=10)

switch_frame(frame_signin)

root.mainloop()
