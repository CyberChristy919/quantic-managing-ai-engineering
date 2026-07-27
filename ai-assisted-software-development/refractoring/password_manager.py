import tkinter as tk
from tkinter import messagebox
import json
from cryptography.fernet import Fernet
import random
import string
import re

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x400")

        self.load_encryption_key()
        self.load_passwords()
        self.create_widgets()

    def load_encryption_key(self):
        try:
            with open('key.key', 'rb') as key_file:
                self.encryption_key = key_file.read()
        except FileNotFoundError:
            self.encryption_key = Fernet.generate_key()
            with open('key.key', 'wb') as key_file:
                key_file.write(self.encryption_key)

        self.cipher_suite = Fernet(self.encryption_key)

    def load_passwords(self):
        try:
            with open('passwords.json', 'r') as f:
                self.passwords = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.passwords = {}

    def save_passwords(self):
        with open('passwords.json', 'w') as f:
            json.dump(self.passwords, f, indent=4)

    def is_valid_email(self, email):
        pattern = r"^[\w\.+-]+@\w+\.\w+$"
        return re.fullmatch(pattern, email, flags=re.IGNORECASE) is not None

    def generate_password(self):
        url = self.url_entry.get().strip()
        username = self.username_entry.get().strip()

        if not url:
            messagebox.showerror("Input Error", "URL is required.")
            return

        if not username:
            messagebox.showerror("Input Error", "Email/username is required.")
            return

        if not self.is_valid_email(username):
            messagebox.showerror("Validation Error", f"Invalid email: {username}")
            return

        password_length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))

        encrypted_password = self.cipher_suite.encrypt(password.encode())

        self.passwords[url] = {
            "username": username,
            "password": encrypted_password.decode()
        }

        self.save_passwords()
        messagebox.showinfo("Success", f"Email validation result: True\nGenerated password saved for {url}")
        self.screen2.destroy()
        self.update_url_list()

    def open_screen2(self):
        self.screen2 = tk.Toplevel(self.master)
        self.screen2.title("Create New Password")

        tk.Label(self.screen2, text="URL:").pack()
        self.url_entry = tk.Entry(self.screen2)
        self.url_entry.pack()

        tk.Label(self.screen2, text="Email / Username:").pack()
        self.username_entry = tk.Entry(self.screen2)
        self.username_entry.pack()

        tk.Button(self.screen2, text="Generate Password", command=self.generate_password).pack()

    def open_screen3(self, url):
        screen3 = tk.Toplevel(self.master)
        screen3.title(f"Password for {url}")

        decrypted_password = self.cipher_suite.decrypt(self.passwords[url]["password"].encode())

        tk.Label(screen3, text=f"Username: {self.passwords[url]['username']}").pack()
        tk.Label(screen3, text=f"Password: {decrypted_password.decode()}").pack()

    def update_url_list(self):
        self.url_listbox.delete(0, tk.END)
        for url in self.passwords:
            self.url_listbox.insert(tk.END, url)

    def create_widgets(self):
        self.url_listbox = tk.Listbox(self.master)
        self.url_listbox.pack()
        self.update_url_list()

        tk.Button(self.master, text="Create New", command=self.open_screen2).pack()
        tk.Button(self.master, text="Close", command=self.master.quit).pack()

        self.url_listbox.bind(
            "<Double-Button-1>",
            lambda event: self.open_screen3(self.url_listbox.get(self.url_listbox.curselection()))
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
