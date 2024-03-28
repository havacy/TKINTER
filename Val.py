import customtkinter 

base = customtkinter.CTk()
base.geometry("700x300")
base.resizable("0")
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

entry1 =customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 =customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

check = customtkinter.CTkCheckBox(master= frame, text="Remeber Me")
check.pack(pady=12, padx=10)
base.mainloop()

