from tkinter import *
import re

bgc = "#E6E6FA"

# Create window, set title, bg colour, dimensions and icon
window = Tk()
window.title("Password Protection Program")
window.configure(background="#E6E6FA")
window.geometry("1080x840")
# window.wm_iconbitmap('logo.ico')

# Logo image?
# logo = PhotoImage(file="logo.png")
# logo_lbl = Label(window, image=logo)
# logo.lbl.pack()

# Welcome label
welcome = Label(window, text="Welcome to the Password Protection Program", bg=bgc, font=("Helvetica",16))

# Create master password label
create_lbl = Label(window, text="Create a master password", bg=bgc, font=("Helvetica",16))

# Enter pw
ent = Entry(window, show="*")

# Checks if password is good and then encrypts it to a file
def checkPassword():
    password = ent.get()
    strength = 0

    if len(password) == 0:
        msg = "Password cannot be empty"

    elif len(password) < 8:
        msg = "Password must be at least 8 characters"

    elif not(re.search("[0-9]", password)):
        msg = "Password must have at least 1 number"
        
    elif not(re.search("[a-z]", password) and re.search("[A-Z]", password)):
        msg = "Password must have uppercase and lowercase"
        
    else:
        msg = "Success!"

    mesg.configure(text=msg)
    

# Button
btn = Button(window, text="Enter", font=("Helvetica",16), command=checkPassword)

# Password strength
mesg = Label(window, text="", bg=bgc)    

# Add all widgets to window
welcome.pack()
create_lbl.pack()
ent.pack()
btn.pack()
mesg.pack()

# Draw window
window.mainloop()





