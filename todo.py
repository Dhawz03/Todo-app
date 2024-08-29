import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.title("To-Do List")

        self.configure(bg='#f0f0f0')
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self, text="My To-Do List", font=("Helvetica", 18), bg='#f0f0f0')
        title_label.pack(pady=10)

        # Task entry
        self.task_input = tk.Entry(self, width=30, font=("Helvetica", 12))
        self.task_input.pack(pady=10)

        # Priority dropdown
        self.priority_var = tk.StringVar()
        self.priority_combobox = ttk.Combobox(self, textvariable=self.priority_var)
        self.priority_combobox['values'] = ('High', 'Medium', 'Low')
        self.priority_combobox.set('Select Priority')
        self.priority_combobox.pack(pady=5)

        # Deadline selection
        self.deadline_label = tk.Label(self, text="Select Deadline:", font=("Helvetica", 12), bg='#f0f0f0')
        self.deadline_label.pack(pady=5)
        self.deadline_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.deadline_entry.pack(pady=5)

        # Add task button
        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task, bg='#5cb85c', fg='white', font=("Helvetica", 12))
        self.add_task_button.pack(pady=5)

        # Task listbox
        self.tasks_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=70, height=10, font=("Helvetica", 12))
        self.tasks_listbox.pack(pady=10)

        # Frame for edit and delete buttons
        self.button_frame = tk.Frame(self, bg='#f0f0f0')
        self.button_frame.pack(pady=5)

        self.edit_task_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task, bg='#5bc0de', fg='white', font=("Helvetica", 12))
        self.edit_task_button.grid(row=0, column=0, padx=5, pady=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg='#d9534f', fg='white', font=("Helvetica", 12))
        self.delete_task_button.grid(row=0, column=1, padx=5, pady=5)

        # Save and load buttons
        self.save_task_button = tk.Button(self, text="Save Tasks", command=self.save_tasks, bg='#0275d8', fg='white', font=("Helvetica", 12))
        self.save_task_button.pack(pady=5)

        self.load_button = tk.Button(self, text="Load Tasks", command=self.load_tasks, bg='#5bc0de', fg='white', font=("Helvetica", 12))
        self.load_button.pack(pady=5)

    def add_task(self):
        task = self.task_input.get()
        priority = self.priority_var.get()
        deadline = self.deadline_entry.get_date().strftime('%Y-%m-%d')

        if task and priority != 'Select Priority':
            formatted_task = f"{task} (Priority: {priority}, Deadline: {deadline})"
            self.tasks_listbox.insert(tk.END, formatted_task)
            self.task_input.delete(0, tk.END)
            self.priority_combobox.set('Select Priority')
        else:
            messagebox.showwarning("Input Error", "Please enter a task, select a priority, and choose a deadline.")

    def edit_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            current_task = self.tasks_listbox.get(task_index)
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=current_task)
            if new_task:
                self.tasks_listbox.delete(task_index)
                self.tasks_listbox.insert(task_index, new_task)

    def delete_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            self.tasks_listbox.delete(task_index)

    def save_tasks(self):
        tasks = self.tasks_listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task + "\n")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
            self.tasks_listbox.delete(0, tk.END)
            for task in tasks:
                self.tasks_listbox.insert(tk.END, task)