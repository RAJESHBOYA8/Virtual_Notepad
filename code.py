import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk

# Create main application window
root = tk.Tk()
root.title("Virtual Notepad")
root.geometry("900x600")

# Create Text Area
text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand=True, fill='both')

# Scrollbar
scroll = tk.Scrollbar(text_area)
scroll.pack(side='right', fill='y')
text_area.config(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)

# File operations
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Virtual Notepad")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Virtual Notepad")

def save_file():
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Virtual Notepad")

# Text color
def change_color():
    color = colorchooser.askcolor(title="Choose Text Color")[1]
    if color:
        try:
            text_area.tag_add("colored", "sel.first", "sel.last")
            text_area.tag_config("colored", foreground=color)
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select text to color.")

# Insert image
def insert_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 150))  # Resize image
        photo = ImageTk.PhotoImage(img)
        text_area.image_create(tk.INSERT, image=photo)
        # Store reference to prevent garbage collection
        if not hasattr(text_area, 'images'):
            text_area.images = []
        text_area.images.append(photo)

# Edit operations
def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    messagebox.showinfo("About", "Virtual Notepad\nWith Color & Image Insertion\nBuilt using Python Tkinter")

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Change Text Color", command=change_color)
edit_menu.add_command(label="Insert Image", command=insert_image)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Start the app
root.mainloop()
