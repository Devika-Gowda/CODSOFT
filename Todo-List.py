import tkinter as tk
from tkinter import messagebox, ttk

tasks = []  # list to store (task, priority)

def add_task():
    task = task_entry.get().strip()
    priority = priority_var.get()

    if not task:
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    tasks.append((task, priority))
    update_listbox()
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        del tasks[selected]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()

def search_tasks():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)
    for task, priority in tasks:
        if query in task.lower():
            listbox.insert(tk.END, f"{task} [{priority}]")
            color_task(priority)

def show_all_tasks():
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task, priority in tasks:
        listbox.insert(tk.END, f"{task} [{priority}]")
        color_task(priority)

def color_task(priority):
    index = listbox.size() - 1
    if priority == "High":
        listbox.itemconfig(index, {'fg': 'red'})
    elif priority == "Medium":
        listbox.itemconfig(index, {'fg': 'orange'})
    else:
        listbox.itemconfig(index, {'fg': 'green'})

# Hover effects
def on_enter(event, hover_color):
    event.widget.config(bg=hover_color)

def on_leave(event, normal_color):
    event.widget.config(bg=normal_color)

# GUI setup
root = tk.Tk()
root.title("Todo List")
root.geometry("560x620")
root.configure(bg="#2c3e50")

# Title label
title_label = tk.Label(root, text="📝 Hello, Welcome to the Todo-List!", 
                       font=("Helvetica", 18, "bold"), fg="#f1c40f", bg="#2c3e50")
title_label.pack(pady=20)

# Search box
search_frame = tk.Frame(root, bg="#2c3e50")
search_frame.pack(pady=5)
search_entry = tk.Entry(search_frame, width=28, font=("Helvetica", 12))
search_entry.grid(row=0, column=0, padx=5)

search_button = tk.Button(search_frame, text="Search", command=search_tasks, 
                          bg="#e67e22", fg="white", font=("Helvetica", 11, "bold"), width=10)
search_button.grid(row=0, column=1, padx=5)
search_button.bind("<Enter>", lambda e: on_enter(e, "#d35400"))
search_button.bind("<Leave>", lambda e: on_leave(e, "#e67e22"))

# Task input + priority
task_frame = tk.Frame(root, bg="#2c3e50")
task_frame.pack(pady=10)

task_entry = tk.Entry(task_frame, width=32, font=("Helvetica", 13))
task_entry.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Medium")
priority_menu = ttk.Combobox(task_frame, textvariable=priority_var, 
                             values=["High", "Medium", "Low"], width=10, 
                             state="readonly", font=("Helvetica", 11))
priority_menu.grid(row=0, column=1, padx=5)

# Buttons frame
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=15)

# Add Task button
add_button = tk.Button(button_frame, text="Add", command=add_task, bg="#27ae60", 
                       fg="white", font=("Helvetica", 11, "bold"), width=10)
add_button.grid(row=0, column=0, padx=8)
add_button.bind("<Enter>", lambda e: on_enter(e, "#2ecc71"))
add_button.bind("<Leave>", lambda e: on_leave(e, "#27ae60"))

# Show All button
show_button = tk.Button(button_frame, text="Show All", command=show_all_tasks, 
                        bg="#2980b9", fg="white", font=("Helvetica", 11, "bold"), width=10)
show_button.grid(row=0, column=1, padx=8)
show_button.bind("<Enter>", lambda e: on_enter(e, "#3498db"))
show_button.bind("<Leave>", lambda e: on_leave(e, "#2980b9"))

# Delete Task button
delete_button = tk.Button(button_frame, text="Delete", command=delete_task, 
                          bg="#c0392b", fg="white", font=("Helvetica", 11, "bold"), width=10)
delete_button.grid(row=0, column=2, padx=8)
delete_button.bind("<Enter>", lambda e: on_enter(e, "#e74c3c"))
delete_button.bind("<Leave>", lambda e: on_leave(e, "#c0392b"))

# Clear All button
clear_button = tk.Button(button_frame, text="Clear All", command=clear_all, 
                         bg="#8e44ad", fg="white", font=("Helvetica", 11, "bold"), width=10)
clear_button.grid(row=0, column=3, padx=8)
clear_button.bind("<Enter>", lambda e: on_enter(e, "#9b59b6"))
clear_button.bind("<Leave>", lambda e: on_leave(e, "#8e44ad"))

# Task Listbox
listbox = tk.Listbox(root, width=50, height=15, font=("Helvetica", 12), 
                     bd=2, relief="ridge", bg="#f1f8f6", fg="#2c3e50")
listbox.pack(pady=15)


# Run the app
root.mainloop()
