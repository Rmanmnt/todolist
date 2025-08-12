import tkinter as tk
from tkinter import ttk
from ui.add_tasks_window import add_task_window
from ui.tasks_window import tasks_window


class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.geometry('600x500')
        self.root.title('To-Do List')
        self.root.configure(bg="#f5f5f5")

        self.setup_style()
        self.create_widgets()
        self.refresh_task_list(self.controller.get_all_tasks())

    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview",
                        background="#f0f0f0",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#f5f5f5",
                        font=("Helvetica", 12))
        style.map('Treeview', background=[('selected', '#2196f3')], foreground=[('selected', 'white')])

        style.configure("TButton", font=("Helvetica", 12, "bold"))

    def create_widgets(self):
        # Frame برای لیست تسک‌ها
        self.tasks_labelframe = ttk.LabelFrame(self.root, text="Tasks", padding=10)
        self.tasks_labelframe.pack(fill="both", expand=True, padx=20, pady=20)

        columns = ("name", "status")
        self.tree = ttk.Treeview(self.tasks_labelframe, columns=columns, show='headings', selectmode='browse')
        self.tree.heading("name", text="Task Name")
        self.tree.heading("status", text="Status")
        self.tree.column("name", width=400)
        self.tree.column("status", width=120, anchor='center')

        self.tree.pack(fill="both", expand=True)

        # Bind کلیک روی ردیف
        self.tree.bind("<<TreeviewSelect>>", self.on_task_select)

        # Frame برای دکمه‌ها
        button_frame = tk.Frame(self.root, bg=self.root["bg"])
        button_frame.pack(pady=10)

        btn_add = ttk.Button(button_frame, text="Add Task", command=self.open_add_task_window)
        btn_add.pack(side="left", padx=5)

        btn_refresh = ttk.Button(button_frame, text="Refresh", command=lambda: self.refresh_task_list(self.controller.get_all_tasks()))
        btn_refresh.pack(side="left", padx=5)

    def refresh_task_list(self, tasks):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for task in tasks:
            self.tree.insert('', 'end', iid=task.id, values=(task.name, task.status.capitalize()))

    def open_add_task_window(self):
        add_task_window(self.root, self.controller, self.refresh_task_list)

    def on_task_select(self, event):
        selected = self.tree.selection()
        if selected:
            task_id = selected[0]
            tasks_window(self.root, self.controller, task_id, self.refresh_task_list)
