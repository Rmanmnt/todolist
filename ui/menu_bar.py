import tkinter as tk


def create_menu(root):
    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="جدید")
    file_menu.add_separator()
    file_menu.add_command(label="خروج", command=root.quit)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="درباره ما")

    menubar.add_cascade(label="فایل", menu=file_menu)
    menubar.add_cascade(label="راهنما", menu=help_menu)

    root.config(menu=menubar)