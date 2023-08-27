import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.heading_label = tk.Label(root, text="Password Generator", font=("bold", 20))
        self.heading_label.pack(pady=10)

        self.user_label = tk.Label(root, text="User Name:")
        self.user_label.pack()
        self.user_entry = tk.Entry(root)
        self.user_entry.pack(pady=5)

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_scale = tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, length=200)
        self.length_scale.set(8)
        self.length_scale.pack(pady=5)

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack()
        self.complexity_scale = tk.Scale(root, from_=1, to=3, orient=tk.HORIZONTAL, length=200)
        self.complexity_scale.set(1)
        self.complexity_scale.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="Password:", font=("bold", 20))
        self.password_label.pack()
        self.password_entry = tk.Entry(root)
        self.password_entry.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Password", command=self.reset_password)
        self.reset_button.pack(pady=10)

    def generate_password(self):
        length = self.length_scale.get()
        complexity = self.complexity_scale.get()

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        if complexity <= 0:
            messagebox.showerror("Error", "Password complexity must be greater than zero.")
            return

        characters = string.ascii_letters * (complexity >= 1) + string.digits * (complexity >= 2) + string.punctuation * (complexity >= 3)
        password = ''.join(random.choices(characters, k=length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)

    def reset_password(self):
        self.length_scale.set(8)
        self.complexity_scale.set(1)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
