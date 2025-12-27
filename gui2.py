import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do Application")

        self.root.geometry("500x500")

        self.tasksframe = tk.Frame(self.root)
        self.tasksframe.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.scroller = tk.Scrollbar(
            self.tasksframe, orient=tk.VERTICAL)

        self.scroller.grid(row=0, column=1, sticky="ns", pady=20)

        self.tasklist = tk.Listbox(
            self.tasksframe, height=15, width=50, activestyle="underline", yscrollcommand=self.scroller.set)

        self.tasklist.grid(row=0, column=0, sticky="nsew")
        self.scroller['command'] = self.tasklist.yview

        self.tasksframe.grid_rowconfigure(0, weight=1)
        self.tasksframe.grid_columnconfigure(0, weight=1)

        # -----Functionality for add, remove, and mark-done

        self.controls = tk.Frame(self.root)
        self.controls.grid(row=1, column=0, columnspan=3, pady=20)

        self.addtask = tk.Button(
            self.controls, text="Add New Task", command=self.add_task_prompt)
        self.addtask.grid(row=1, column=0, padx=10)

        self.removetask = tk.Button(
            self.controls, text="Mark Task As Done and Remove", command=self.remove_after_marked_done)
        self.removetask.grid(row=1, column=1, padx=10)

        # -----Textbox entry for new task

        self.taskentry = tk.Frame(self.root)
        self.taskentry.grid(row=2, column=0, columnspan=2, pady=10)

        # -----Dropdown menu function

        self.menubutton = tk.Menubutton(
            self.root, text="Commands", relief=tk.RAISED)
        self.menubutton.grid()
        self.menu = tk.Menu(self.menubutton)
        # ---debugging list to test deletion and list filling
        # for i in range(100):
        # self.tasklist.insert(i, f"Task"+f"{i}")

        self.root.mainloop()

    def add_task_to_end(self, event):
        to_add = self.taskdesc.get().strip()
        if not to_add:
            messagebox.showerror(
                title="Error", message="Enter a Task Description")
            return
        self.tasklist.insert(tk.END, to_add)

        self.taskdesc.destroy()
        self.prompt.destroy()
        del self.taskdesc
        del self.prompt

    def add_task_prompt(self):
        self.taskdesc = tk.Entry(self.taskentry)
        self.prompt = tk.Label(
            self.taskentry, text="Enter Task Description", padx=10)

        self.taskdesc.grid(row=2, column=1)
        self.prompt.grid(row=2, column=0)
        self.taskdesc.focus()
        self.taskdesc.bind(
            "<Return>", self.add_task_to_end)

    def remove_after_marked_done(self):
        to_remove = self.tasklist.curselection()
        if not to_remove:
            messagebox.showerror(
                title="Error", message="Please select a task.")
            return
        self.tasklist.delete(to_remove[0])


GUI()
