from tkinter import *
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk
import os

# Create the main application window
root = Tk()
root.title("VIRTUAL NOTEPAD - BY RAJESH")
root.geometry("800x600")

# Text widget for writing
text_area = Text(root, font=("Arial", 14), undo=True)
text_area.pack(fill=BOTH, expand=1)

# Scrollbar
scroll = Scrollbar(text_area)
scroll.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, END)
        with open(file_path, "r") as file:
            text_area.insert(INSERT, file.read())
        root.title(f"VIRTUAL NOTEPAD - BY RAJESH - {os.path.basename(file_path)}")

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))
        root.title(f"VIRTUAL NOTEPAD - BY RAJESH - {os.path.basename(file_path)}")

# Function to pick color
def pick_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)

# Function to insert image
def insert_image():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if img_path:
        img = Image.open(img_path)
        img = img.resize((150, 150))  # Resize image
        img = ImageTk.PhotoImage(img)
        text_area.image_create(INSERT, image=img)
        text_area.image = img  # Keep reference to avoid garbage collection

# Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))

# Format Menu
format_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Text Color", command=pick_color)

# Insert Menu
insert_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Insert", menu=insert_menu)
insert_menu.add_command(label="Insert Image", command=insert_image)

# Run the application
root.mainloop()
