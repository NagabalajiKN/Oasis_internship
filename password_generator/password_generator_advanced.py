from tkinter import *
from tkinter import messagebox
import string
import secrets
import pyperclip
import os
import re

window = Tk()
window.title('SECURE SENTINEL')
current_directory = os.path.dirname(__file__)
image_path = os.path.join(current_directory, 'password_logo.png')
window.iconphoto(False, PhotoImage(file=image_path))

# Set the background color to a light blue
window.configure(bg='#f4f7fd')

for i in range(5):
    window.columnconfigure(i, weight=1, minsize=40)
    window.rowconfigure(i, weight=1, minsize=50)


global is_on1                                            # Global variables to keep track of the state of the switches
global is_on2
global is_on3
is_on1 = False
is_on2 = False
is_on3 = False

# Custom color scheme
bg_color = '#f4f7fd'
text_color = '#333333'
button_color = '#3172da'  # Greenish color for buttons

# Custom fonts
heading_font = ('Segoe UI', 18, 'bold')
label_font = ('Segoe UI', 12, 'bold')
button_font = ('Segoe UI', 12, 'bold')

# Load images
on_path = os.path.join(current_directory, 'on.png')
off_path = os.path.join(current_directory, 'off.png')
on_image1 = PhotoImage(file=on_path).subsample(13, 12)
off_image1 = PhotoImage(file=off_path).subsample(13, 12)

warning_label = Label(window, text='', font=('Segoe UI', 12), fg='red', bg=bg_color)
warning_label.grid(column=1, row=6, columnspan=2)

def switch1():
    global is_on1
    if is_on1:
        on_button1.config(image=off_image1)
        is_on1 = False
    else:
        on_button1.config(image=on_image1)
        is_on1 = True

def switch2():
    global is_on2
    if is_on2:
        on_button2.config(image=off_image1)
        is_on2 = False
    else:
        on_button2.config(image=on_image1)
        is_on2 = True

def switch3():
    global is_on3
    if is_on3:
        on_button3.config(image=off_image1)
        is_on3 = False
    else:
        on_button3.config(image=on_image1)
        is_on3 = True

def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:              # Check for length of password  
        score += 1

    # Check for uppercase, lowercase, and digits
    if re.search(r'[A-Z]', password) and \
       re.search(r'[a-z]', password) and \
       re.search(r'\d', password):
        score += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):   # Check for special characters
        score += 1

    if score == 3:
        return "Strong - Password is very secure!"
    elif score == 2:
        return "Moderate - Password is moderately secure."
    else:
        return "Weak - Password needs improvement."
    
def show_custom_message(message, display_immediately=True):
    top = Toplevel()
    top.title('Random 🗝️')
    top.configure(bg=bg_color)
    label = Label(top, text=message, font=('Segoe UI', 14), bg=bg_color, fg=text_color)
    label.pack(padx=10, pady=10)
    
    if display_immediately:
        ok_button = Button(top, text='OK', command=top.destroy, font=button_font, bg=button_color, fg='white', activebackground=button_color)
        ok_button.pack(pady=10)
    else:
        return top

def generate_password_and_copy(length, is_on1, is_on2, is_on3):
    generated_password = generate_password(length, is_on1, is_on2, is_on3)
    if generated_password:
        pyperclip.copy(generated_password)
        password_strength = check_password_strength(generated_password)
        copy_button_top = show_custom_message('Password: {}\n\nStrength: {}\n\nClick "Copy" to copy to clipboard.'.format(generated_password, password_strength), display_immediately=False)
        copy_button = Button(copy_button_top, text='Copy', command=lambda: copy_to_clipboard_and_destroy(copy_button_top, generated_password), font=button_font, bg=button_color, fg='white', activebackground=button_color)
        copy_button.pack(pady=10)
    else:
        warning_label.config(text='Less than 8 characters selected.')


def copy_to_clipboard_and_destroy(top, password):
    pyperclip.copy(password)
    top.destroy()

def generate_password(length, is_on1, is_on2, is_on3):
    characters = ""
    if length < 8:
        warning_label.config(text='Password length must be at least 8 characters.')
        return None
    else:
        warning_label.config(text='')

    if is_on1:
        characters += string.ascii_letters
    if is_on2:
        characters += string.digits
    if is_on3:
        characters += string.punctuation

    if not characters:
        return None

    password = ''
    for _ in range(length):
        password += secrets.choice(characters)

    return password

heading_label = Label(window, text='PASSWORD GENERATOR 🔐', font=heading_font, bg=bg_color, fg=text_color)
heading_label.grid(column=0, row=0, columnspan=4)

length_label = Label(window, text='Length:', font=label_font, bg=bg_color, fg=text_color)
length_label.grid(column=0, row=1, sticky='W', padx=20)

length_entry = Entry(window, width=20, font=('default', 14))
length_entry.grid(column=1, row=1, columnspan=2)

letter_label = Label(window, text=' Include Letters?', font=label_font, bg=bg_color, fg=text_color)
letter_label.grid(column=0, row=2, sticky='W', padx=20)

on_button1 = Button(window, image=off_image1, bd=0, command=switch1, bg=bg_color, activebackground=bg_color)
on_button1.grid(column=1, row=2)

number_label = Label(window, text='Include Numbers?', font=label_font, bg=bg_color, fg=text_color)
number_label.grid(column=0, row=3, sticky='W', padx=20)

on_button2 = Button(window, image=off_image1, bd=0, command=switch2, bg=bg_color, activebackground=bg_color)
on_button2.grid(column=1, row=3)

symbol_label = Label(window, text='Include Symbols?', font=label_font, bg=bg_color, fg=text_color)
symbol_label.grid(column=0, row=4, sticky='W', padx=20)

on_button3 = Button(window, image=off_image1, bd=0, command=switch3, bg=bg_color, activebackground=bg_color)
on_button3.grid(column=1, row=4)

generate_button = Button(window, text='Generate Password', font=button_font, command=lambda: generate_password_and_copy(int(length_entry.get()), is_on1, is_on2, is_on3), bg=button_color, fg='white', activebackground=button_color)
generate_button.grid(column=1, row=5, columnspan=2, pady=20)

window.mainloop()
