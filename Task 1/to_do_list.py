import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

def mark_as_done():
    selected_index = listbox.curselection()
    if selected_index:
        task = listbox.get(selected_index)
        updated_task = task + " (Done)"
        listbox.delete(selected_index)
        listbox.insert(selected_index, updated_task)

window = tk.Tk()
window.title("To-Do List")

listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=20)

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)
mark_done_button = tk.Button(window, text="Mark as Done", command=mark_as_done)
mark_done_button.pack(pady=5)
window.mainloop()
