import customtkinter 
import time 

base = customtkinter.CTk()

base.geometry("380x240")
base.title("Nexus Login")
base.resizable(False, False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def login():
    print("sucessfully logged in")

def Remeber():
    print("Checked")

frame = customtkinter.CTkFrame(master=base)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("Impact", 24))
label.pack(pady=12, padx=10)

entry =customtkinter.CTkEntry(master=frame, placeholder_text="Key")
entry.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

base.mainloop()



