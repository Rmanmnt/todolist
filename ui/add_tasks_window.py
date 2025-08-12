import tkinter as tk
from tkinter import ttk, messagebox

def add_task_window(root, controller, call_back=None):
    atwindow = tk.Toplevel(root)
    atwindow.transient(root)
    atwindow.grab_set()
    atwindow.focus_set()
    atwindow.title("Create Task")
    atwindow.geometry("400x330")
    atwindow.resizable(False, False)
    atwindow.configure(bg="#f5f5f5")

    label_font = ("Segoe UI", 11)
    label_font_bold = ("Segoe UI", 11, "bold")
    button_font = ("Segoe UI", 11, "bold")

    frame = ttk.Frame(atwindow, padding=15)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text='Name:', font=label_font_bold).grid(row=0, column=0, sticky="w", pady=8)
    name_entry = ttk.Entry(frame, font=label_font)
    name_entry.grid(row=0, column=1, sticky="ew", pady=8)

    ttk.Label(frame, text='Description:', font=label_font_bold).grid(row=1, column=0, sticky="nw", pady=8)
    description_text = tk.Text(frame, height=5, font=label_font, wrap="word")
    description_text.grid(row=1, column=1, sticky="ew", pady=8)

    ttk.Label(frame, text='Priority:', font=label_font_bold).grid(row=2, column=0, sticky="w", pady=8)
    priority_var = tk.StringVar()
    priority_combo = ttk.Combobox(frame, textvariable=priority_var, values=["کم", "متوسط", "زیاد"], state="readonly", font=label_font)
    priority_combo.current(1)
    priority_combo.grid(row=2, column=1, sticky="ew", pady=8)

    ttk.Label(frame, text='Status:', font=label_font_bold).grid(row=3, column=0, sticky="w", pady=8)
    status_var = tk.StringVar()
    status_combo = ttk.Combobox(frame, textvariable=status_var, values=["فعال", "غیرفعال", "تمام شده"], state="readonly", font=label_font)
    status_combo.current(0)
    status_combo.grid(row=3, column=1, sticky="ew", pady=8)

    # Make columns stretch
    frame.columnconfigure(1, weight=1)

    def submit_task():
        name = name_entry.get().strip()
        description = description_text.get("1.0", "end").strip()
        priority = priority_combo.get()
        status = status_combo.get()

        flag, messages = controller.check_add_task_entry_values(name, description, priority)
        if flag:
            result = controller.add_task(name, description, priority, status)
            messagebox.showinfo('Add Task', result)
            if call_back:
                call_back(controller.get_all_tasks())
            atwindow.destroy()
        else:
            messagebox.showerror('Add Task', messages)

    submit_btn = ttk.Button(frame, text="ثبت", command=submit_task)
    submit_btn.grid(row=4, column=1, sticky="e", pady=15)
