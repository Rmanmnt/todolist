import tkinter as tk
from ui.window import MainView
from controller.controller import ToDoController


def main():
    root = tk.Tk()

    
    controller = ToDoController()
    view = MainView(root,controller)


    root.mainloop()

if __name__ == "__main__":
    main()
