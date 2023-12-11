from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import csv
import os
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import simpledialog, messagebox

# Set a modern font and color scheme
FONT = ('Segoe UI', 12, 'bold')
BG_COLOR = "#140720"  # Light gray background color
FG_COLOR = "#e8d8f6"  # Dark gray text color
BUTTON_COLOR = "#80cbfa"  # Green color for buttons

window = tk.Tk()
window.title('Shape Shifter')
window.configure(bg=BG_COLOR)

current_directory = os.path.dirname(__file__)
image_path = os.path.join(current_directory, 'bmiicon.png')

# ...

window.iconphoto(False, PhotoImage(file=image_path))

today = date.today()

for i in range(4):
    window.columnconfigure(i, weight=1, minsize=40)
    window.rowconfigure(i, weight=1, minsize=50)

# Get the current directory where bmi_advanced.py is located
csv_path = os.path.join(current_directory, 'data.csv')

bmi_results = ""
if not os.path.exists(csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'weight', 'height', 'bmi', 'date'])

def visualize_data():
    user_name = tk.simpledialog.askstring("Input", "Enter the user's name:",)

    if not user_name:
        return  # User canceled the input

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row
        user_data = [row for row in reader if row and row[0].lower() == user_name.lower()]

    if not user_data:
        tk.messagebox.showinfo('Error', f'No data found for user: {user_name}')
        return

    # Check if each row has the expected number of elements (4 or 5)
    if any(len(row) not in (4, 5) for row in user_data):
        tk.messagebox.showinfo('Error', 'Invalid data format in CSV file')
        return

    # Extract relevant data for visualization
    dates = [row[4] if len(row) == 5 else '' for row in user_data]
    bmi_values = [float(row[3]) for row in user_data]

    # Create a new window for visualization
    visualize_window = tk.Toplevel(window)
    visualize_window.title(f'Visualization for {user_name}')

    # Create a matplotlib figure
    fig, ax = plt.subplots()
    ax.plot(dates, bmi_values, marker='o', linestyle='-')
    ax.set_xlabel('Date')
    ax.set_ylabel('BMI')
    ax.set_title(f'BMI History for {user_name}')

    # Embed the matplotlib figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=visualize_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()



heading_label = tk.Label(window, text='BMI CALCULATOR 💪🏼', font=('Helvetica', 18), bg=BG_COLOR, fg=FG_COLOR)
heading_label.grid(column=1, row=0, pady=(20, 10))

# Update labels with modern font and color
name_label = tk.Label(window, text='Name:', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
name_label.grid(column=0, row=1, sticky='W', padx=20)

name_entry = tk.Entry(window, width=20, font=FONT)
name_entry.grid(column=1, row=1)

weight_label = tk.Label(window, text='Weight (kg):', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
weight_label.grid(column=0, row=2, sticky='W', padx=20)

weight_entry = tk.Entry(window, width=20, font=FONT)
weight_entry.grid(column=1, row=2)

height_label = tk.Label(window, text='Height (m):', font=FONT, bg=BG_COLOR, fg=FG_COLOR)
height_label.grid(column=0, row=3, sticky='W', padx=20)

height_entry = tk.Entry(window, width=20, font=FONT)
height_entry.grid(column=1, row=3)

def calculate_bmi():
    name = name_entry.get()
    name = name.lower()
    weight = weight_entry.get()
    height = height_entry.get()

    # Check if weight and height are provided
    if not weight or not height:
        tk.messagebox.showinfo('Error', 'Please enter both weight and height.')
        return

    weight = float(weight)
    height = float(height)
    bmi = weight / (height ** 2)
    d1 = today.strftime("%d/%m/%Y")

    # Update the placeholder label text
    result_label.config(text=f'\nBMI: {bmi:.2f}')

    if bmi < 18.5:  # print category
        category_label.config(text="Category : Underweight.\nYou should gain weight 💪")
    elif bmi < 25:
        category_label.config(text='Category : Healthy weight.\nWell done!! Keep it up😁')
    elif bmi < 30:
        category_label.config(text='Category : Overweight.\nYou should lose some weight and exercise more.⛹️')
    else:
        category_label.config(text='Category : Obese.\nYou should take immediate action to lose weight.You can do it🙂')

    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, weight, height, bmi, d1])

def clear_text():
   name_entry.delete(0, tk.END)
   weight_entry.delete(0, tk.END)
   height_entry.delete(0, tk.END)
   output_label.configure(text='')
   result_label.configure(text='')
   category_label.configure(text='')
   

def history():
    new_window = tk.Toplevel(window)
    new_window.title('History')
    new_window.configure(bg=BG_COLOR)  # Set background color

    history_heading_label = tk.Label(new_window, text='BMI History', font=('Calibri', 18), bg=BG_COLOR, fg=FG_COLOR)
    history_heading_label.grid(column=0, row=0, sticky='w')  # Align to the left (west)

    history_tree = ttk.Treeview(new_window, columns=('Name', 'Weight', 'Height', 'BMI', 'Date'), show='headings', height=10)
    history_tree.grid(column=0, row=1, sticky='nsew')  # Make it expand in all directions

    new_window.grid_columnconfigure(0, weight=1)  # Make the column expandable
    new_window.grid_rowconfigure(1, weight=1)  # Make the row expandable

    history_tree.heading('Name', text='Name')
    history_tree.heading('Weight', text='Weight')
    history_tree.heading('Height', text='Height')
    history_tree.heading('BMI', text='BMI')
    history_tree.heading('Date', text='Date')

    # Set background color for each row in the treeview
    for tag in ('evenrow', 'oddrow'):
        history_tree.tag_configure(tag, background=BG_COLOR,foreground=FG_COLOR)

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:  # Skip the header row
                continue
            tags = 'evenrow' if i % 2 == 0 else 'oddrow'
            history_tree.insert('', 'end', values=row, tags=tags)

    csvfile.close()

calculate_button = tk.Button(window, text='Calculate BMI', command=calculate_bmi, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#140720')
calculate_button.grid(column=1, row=4)

clear_button = tk.Button(window, text='Clear', command=clear_text, width=10, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#140720')
clear_button.grid(column=2, row=5)

history_button = tk.Button(window, text='History', command=history, width=10, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#140720')
history_button.grid(column=0, row=5)

# Add the Visualize button
visualize_button = tk.Button(window, text='Visualize Data', command=visualize_data, padx=10, pady=5, font=FONT, bg=BUTTON_COLOR, fg='#140720')
visualize_button.grid(column=1, row=5, pady=(10, 5))  # Adding some padding above the button

# Create a placeholder label for the result
result_label = tk.Label(window, font=('Helvetica', 16), bg=BG_COLOR, fg=FG_COLOR)
result_label.grid(column=1, row=6)

# Move the output and category labels below the result label
output_label = tk.Label(window, font=('Helvetica', 16), bg=BG_COLOR, fg=FG_COLOR)
output_label.grid(column=1, row=7)

category_label = tk.Label(window, font=('Helvetica', 15), bg=BG_COLOR, fg=FG_COLOR)
category_label.grid(column=1, row=8)

window.mainloop()