import tkinter as tk
from tkinter import ttk, messagebox

def update_task_window(root, controller, task_id, call_back=None):
    utwindow = tk.Toplevel(root)
    utwindow.transient(root)
    utwindow.grab_set()
    utwindow.focus_set()
    utwindow.title("Update Task")
    utwindow.geometry("400x330")
    utwindow.resizable(False, False)
    utwindow.configure(bg="#f5f5f5")

    task = controller.get_task(task_id)
    if task:
        label_font = ("Segoe UI", 11)
        label_font_bold = ("Segoe UI", 11, "bold")
        button_font = ("Segoe UI", 11, "bold")

        frame = ttk.Frame(utwindow, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text='Name:', font=label_font_bold).grid(row=0, column=0, sticky="w", pady=8)
        name_entry = ttk.Entry(frame, font=label_font)
        name_entry.grid(row=0, column=1, sticky="ew", pady=8)
        name_entry.insert(0, task.name)

        ttk.Label(frame, text='Description:', font=label_font_bold).grid(row=1, column=0, sticky="nw", pady=8)
        description_text = tk.Text(frame, height=5, font=label_font, wrap="word")
        description_text.grid(row=1, column=1, sticky="ew", pady=8)
        description_text.insert("1.0", task.description)  

        priority_values = ["کم", "متوسط", "زیاد"]
        status_values = ["فعال", "غیرفعال", "تمام شده"]

        ttk.Label(frame, text='Priority:', font=label_font_bold).grid(row=2, column=0, sticky="w", pady=8)
        priority_var = tk.StringVar(value=task.priority)  
        priority_combo = ttk.Combobox(frame, textvariable=priority_var, values=priority_values, state="readonly", font=label_font)
        priority_combo.grid(row=2, column=1, sticky="ew", pady=8)

        ttk.Label(frame, text='Status:', font=label_font_bold).grid(row=3, column=0, sticky="w", pady=8)
        status_var = tk.StringVar(value=task.status)
        status_combo = ttk.Combobox(frame, textvariable=status_var, values=status_values, state="readonly", font=label_font)
        status_combo.grid(row=3, column=1, sticky="ew", pady=8)

        frame.columnconfigure(1, weight=1)

        def submit_task():
            name = name_entry.get().strip()
            description = description_text.get("1.0", "end").strip()
            priority = priority_combo.get()
            status = status_combo.get()

            flag, messages = controller.check_add_task_entry_values(name, description, priority, status)
            if flag:
                result = controller.update_task(task.id, name, description, priority, status)
                messagebox.showinfo('Update Task', result)
                if call_back:
                    call_back(controller.get_all_tasks())
                utwindow.destroy()
            else:
                messagebox.showerror('Update Task', messages)

        submit_btn = ttk.Button(frame, text="ثبت", command=submit_task)
        submit_btn.grid(row=4, column=1, sticky="e", pady=15)

    else:
        label_font_bold = ("Segoe UI", 11, "bold")
        ttk.Label(utwindow, text="Task not found!", foreground="red", font=label_font_bold, background="#f5f5f5").pack(pady=40)
