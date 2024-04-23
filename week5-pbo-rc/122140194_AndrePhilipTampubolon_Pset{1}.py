import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.configure(bg="white")
        self.resizable(False, False)
        self.title("Login")

        self.USERNAME = tk.StringVar()
        self.PASSWORD = tk.StringVar()

        # kamus untuk nyimpan username dan password
        self.registered_accounts = {"dreeept": "andre05112004"}

        self.create_widgets()

    #widget di tampilan awal login
    def create_widgets(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(padx=10, pady=10, fill="x", expand=True)

        username_label = ttk.Label(input_frame, text="Username")
        username_label.pack(padx=10, fill="x", expand=True)

        self.username_entry = ttk.Entry(input_frame, textvariable=self.USERNAME)
        self.username_entry.pack(padx=10, fill="x", expand=True)

        password_label = ttk.Label(input_frame, text="Password")
        password_label.pack(padx=10, fill="x", expand=True)

        self.password_entry = ttk.Entry(input_frame, textvariable=self.PASSWORD)
        self.password_entry.pack(padx=10, fill="x", expand=True)

        login_button = ttk.Button(input_frame, text="Login", command=self.combine_command)
        login_button.pack(padx=10, pady=10, fill="x", expand=True)

        register_button = ttk.Button(input_frame, text="Register", command=self.open_register_window)
        register_button.pack(padx=10, pady=10, fill="x", expand=True)

    #masukkan nilai username dan password yang didapat kedalam variabel
    def get_info(self):
        username_info = self.USERNAME.get()
        password_info = self.PASSWORD.get()
        return username_info, password_info

    def check(self, username_info, password_info): 
        if username_info in self.registered_accounts: #mengecek apakah username dan password ada di dalam kamus
            if self.registered_accounts[username_info] == password_info: #cek apakah password yg diinput benar atau salah
                showinfo(message=f"Welcome, {username_info}!", title="Login Successful")
            else:
                showinfo(message="Password salah!", title="Login Failed")
        else:
            showinfo(message="Username tidak terdaftar, silahkan registrasi", title="Login Failed")  #jika username belum diregistrasi

    def combine_command(self):
        username_info, password_info = self.get_info()
        self.check(username_info, password_info)

    def open_register_window(self):
        register_window = RegisterApp(self)
        register_window.title("Register")
        register_window.geometry("300x300")

class RegisterApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("300x300")
        self.configure(bg="white")
        self.resizable(False, False)

        self.USERNAME = tk.StringVar()
        self.PASSWORD = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(padx=10, pady=10, fill="x", expand=True)

        username_label = ttk.Label(input_frame, text="Username")
        username_label.pack(padx=10, fill="x", expand=True)

        self.username_entry = ttk.Entry(input_frame, textvariable=self.USERNAME)
        self.username_entry.pack(padx=10, fill="x", expand=True)

        password_label = ttk.Label(input_frame, text="Password")
        password_label.pack(padx=10, fill="x", expand=True)

        self.password_entry = ttk.Entry(input_frame, textvariable=self.PASSWORD)
        self.password_entry.pack(padx=10, fill="x", expand=True)

        register_button = ttk.Button(input_frame, text="Register", command=self.complete_registration)
        register_button.pack(padx=10, pady=10, fill="x", expand=True)

    def complete_registration(self):
        username_info = self.username_entry.get()
        password_info = self.password_entry.get()
        if username_info and password_info:
            # Cek apakah username sudah terdaftar
            if username_info in self.master.registered_accounts:
                showinfo(message="Username sudah terdaftar", title="Registration Failed")
            else:
                # Menambahkan pasangan username dan password baru ke dalam dictionary
                self.master.registered_accounts[username_info] = password_info
                showinfo(message="You have successfully registered", title="Registration Successful")
                self.destroy()  # Tutup jendela pendaftaran setelah berhasil registrasi
        else:
            showinfo(message="Masukkan username dan password")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
