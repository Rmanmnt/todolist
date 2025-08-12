import tkinter as tk
from tkinter import ttk, messagebox
from ui.update_tasks_window import update_task_window

def tasks_window(root, controller, task_id, call_back=None):
    twindow = tk.Toplevel(root)
    twindow.title("Task Details")
    twindow.geometry("400x380")
    twindow.resizable(False, False)
    twindow.configure(bg="#f5f5f5")

    label_font_bold = ("Segoe UI", 11, "bold")
    label_font = ("Segoe UI", 11)
    button_font = ("Segoe UI", 11, "bold")

    task = controller.get_task(task_id)

    if task:
        info_frame = ttk.Frame(twindow, padding=15)
        info_frame.pack(fill="both", expand=True)

        button_frame = tk.Frame(twindow, bg=twindow["bg"])
        button_frame.pack(pady=10, fill="x")

        style = ttk.Style()
        style.configure("TLabel", background="#f5f5f5", font=label_font)
        style.configure("Bold.TLabel", font=label_font_bold, background="#f5f5f5")
        style.configure("TButton", font=button_font)

        ttk.Label(info_frame, text=f"Name:", style="Bold.TLabel").pack(anchor="w", pady=3)
        ttk.Label(info_frame, text=task.name, style="TLabel").pack(anchor="w", pady=3)

        ttk.Label(info_frame, text=f"Description:", style="Bold.TLabel").pack(anchor="w", pady=3)
        desc_lbl = ttk.Label(info_frame, text=task.description, wraplength=360, style="TLabel")
        desc_lbl.pack(anchor="w", pady=3)

        ttk.Label(info_frame, text=f"Priority:", style="Bold.TLabel").pack(anchor="w", pady=3)
        priority_lbl = ttk.Label(info_frame, text=task.priority, foreground="#1E90FF", style="TLabel")
        priority_lbl.pack(anchor="w", pady=3)

        ttk.Label(info_frame, text=f"Status:", style="Bold.TLabel").pack(anchor="w", pady=3)
        status_lbl = ttk.Label(info_frame, text=task.status, foreground="#FF8C00", style="TLabel")
        status_lbl.pack(anchor="w", pady=3)

        def del_task():
            if messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?"):
                result = controller.remove_task(task.id)
                if result:
                    messagebox.showinfo("Delete Task", result)
                if call_back:
                    call_back(controller.get_all_tasks())
                twindow.destroy()

        def update_task():
            twindow.destroy()
            update_task_window(root, controller, task.id, call_back=call_back)

        ttk.Button(button_frame, text="Delete Task", command=del_task).pack(side="left", padx=10, ipadx=10, ipady=5)
        ttk.Button(button_frame, text="Update Task", command=update_task).pack(side="left", padx=10, ipadx=10, ipady=5)

    else:
        ttk.Label(twindow, text="Task not found!", foreground="red",
            font=label_font_bold, background="#f5f5f5").pack(pady=40)
