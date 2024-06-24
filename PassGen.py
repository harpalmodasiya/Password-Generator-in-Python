import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_scale.get()
    characters = ''
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Selection Error", "Select at least one option!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_history_listbox.insert(tk.END, password)

# Function to copy password
def copy_password():
    selected_password = password_history_listbox.get(tk.ACTIVE)
    if selected_password:
        root.clipboard_clear()
        root.clipboard_append(selected_password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Selection Error", "Select a password to copy")

# Function to clear password history
def clear_history():
    password_history_listbox.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='black')
root.geometry('780x270')

# Title Label
title_label = tk.Label(root, text="Password Generator", bg='black', fg='#7865f8', font=('Helvetica', 20, 'bold'))
title_label.place(x=245, y=8)

# Password Length Scale
length_label = tk.Label(root, text="Select the length of Password", bg='black', fg='white',font=('Helvetica', 12))
length_label.place(x=10, y=50)

length_scale = tk.Scale(root, from_=8, to_=32, orient=tk.HORIZONTAL, bg='black', fg='#7865f8', troughcolor='white', bd=0, length=360)
length_scale.place(x=10, y=90)

# Password Display Box
password_display_box = tk.Entry(root, bg='black', fg='#7865f8', bd=0, width=50)
password_display_box.place(x=10, y=150)

# Checkboxes for password options
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var, bg='black', fg='white', selectcolor='#7865f8',font=('Helvetica', 13))
lowercase_check = tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var, bg='black', fg='white', selectcolor='#7865f8',font=('Helvetica', 13))
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var, bg='black', fg='white', selectcolor='#7865f8',font=('Helvetica', 13))
symbols_check = tk.Checkbutton(root, text="Symbols", variable=symbols_var, bg='black', fg='white', selectcolor='#7865f8',font=('Helvetica', 13))

uppercase_check.place(x=10, y=150)
lowercase_check.place(x=210, y=150)
digits_check.place(x=10, y=180)
symbols_check.place(x=210, y=180)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='#7865f8', fg='black')
generate_button.place(x=10, y=220, width=360)

# Copy Password Button
copy_button = tk.Button(root, text="Copy Password", command=copy_password, bg='#7865f8', fg='black')
copy_button.place(x=410, y=220, width=170)

# Password History Listbox
history_label = tk.Label(root, text="Password History", bg='black', fg='white',font=('Helvetica', 12))
history_label.place(x=410, y=50)

password_history_listbox = tk.Listbox(root, bg='black', fg='white', selectbackground='#7865f8',font=('Helvetica', 11))
password_history_listbox.place(x=410, y=80, width=360, height=125)

# Clear History Button
clear_button = tk.Button(root, text="Clear History", command=clear_history, bg='#7865f8', fg='black')
clear_button.place(x=600, y=220, width=170)

# Run the application
root.mainloop()
