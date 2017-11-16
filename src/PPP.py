## @file PPP.py
# @author Suhavi Sandhu
# @brief The graphical user interface for a password manager
# @date November 10, 2017

from tkinter import *
from tkinter import ttk
import re
import database
import PWChecking
from Constants import *
import inactivity
import Copy
import Encrypt

## @brief An ADT that represents the GUI
class PPP(Tk):

    ## @brief PPP constructor
    #  @details Initializes a PPP GUI object using a variable argument list
    #  @param *args A variable argument list that contains information that should be dsplayed in GUI
    def __init__(self, *args):

        # Initialize GUI
        Tk.__init__(self, *args)        
        # Customizing window title, size and icon
        self.title("Password Protection Program")
        self.geometry(screen_size)
        self.configure(background=BGC)
        # self.wm_iconbitmap('logo.ico')
        # List of accounts
        self.accounts = []
        # Image of eye on button
        self.view = PhotoImage(file=EYE)

        # Checks if master password has been initialized or not
        db = database.Account.select()
        if (len(db) == 0):
            self.showHomeScreen(REGISTER)
        else:
            self.showHomeScreen(LOGIN)
        

    ## @brief Home Screen
    #  @details Displays the first window which can either be a registration frame or log in frame
    #  @param state List of what goes in the frame, namely if it is a register frame or log in frame
    def showHomeScreen(self, state):
        # Creating and adding the frame
        HomeScreen = Frame(self, bg=BGC)      
        welcome = Label(HomeScreen, text=WELCOME, fg=BG, bg=BGC, font=LARGE)
        welcome.grid(row=0, columnspan=3, padx=10, pady=10) # Divides space into 3 columns and places label in the middle
        enterLabel = Label(HomeScreen, fg=BG, bg=BGC, text=state['prompt'])
        enterLabel.grid(row=1, column=1, padx=10, pady=2)
        ent = ttk.Entry(HomeScreen, width=10, font=LARGE, show="*")
        ent.grid(row=2, column=1, padx=10, pady=10)
        
        # Allows submit button to work when the user presses Enter key and calls matchPassword method
        ent.bind('<Return>', lambda x: self.checkPW(HomeScreen, match, ent, state['loggedIn']))
        ent.focus_set()
        # When clicked, checkPW method gets called with the frame name, label and the password entered by user as well as if it is for registering or logging in
        btn = Button(HomeScreen, text="Submit", fg=FG, bg=BG, font=LARGE, command=lambda: self.checkPW(HomeScreen, match, ent, state['loggedIn']))
        btn.grid(row=3, column=1)
        # Label that shows if the password matches the one in the database
        match = Label(HomeScreen, fg=BG, bg=BGC, text="")
        match.grid(row=4, column=1)
        HomeScreen.pack(expand=1)

    ## @brief Check Password
    #  @details Checks if password is good for registration or correct for logging in, depending on input
    #  @param frame The frame which called the method, so it can be updated to show something else upon entering a right password
    #  @param label The label that will be updated to show the user what he/she needs to do
    #  @param entry The entered password
    #  @param state Tells if we are checking for password matching (for LogIn) or criteria (for Registering)
    def checkPW(self, frame, label, entry, state):
        password = entry.get()
        # If for logging in is true
        if state:
            # Get master password from DB and decrypt it
            mp = Encrypt.cryptDecode(database.GetId(1).HashKey, database.GetId(1).HashVal)
            # Password checking
            response = PWChecking.checkLogIn(password, mp)
        else:
            response = PWChecking.checkMP(password)
            
        # If string is returned, means the user did not satisfy some constraint
        if type(response) == str:
            label.config(text=response) # Updates label with correct resposne
            return
        # If there is no string response and the user is registering, add to database
        elif not state:
            # Call encryption methods
            enK = Encrypt.generKey()
            enV = Encrypt.cryptEncode(enK, password)          
            # Insert to database method
            database.Insert(1, "Master", "Master", "", enV, enK)
        frame.destroy() # Destroy the current frame
        self.showPWPage() # Show the password mangement page
        self.configure(background=BG)
        
    ## @brief Show entry
    #  @details Shows entries that already exists as a button on the left scrolling frame
    #  @param frame The frame that displays button
    #  @param detailFrame The frame that will show further details if button on left frame is clicked
    def showEntry(self, frame, detailFrame):
        i = 1
        # Check if database is empty
        if database.Account.table_exists():
            entries = database.Account.select()
        for entry in entries:
            # Get name of entries
            name = entry.AccName[:6]
            btn = Button(frame, text="\t"+name+"\t", image=self.view, compound="right", fg=FG,bg=BG, font=LARGE, anchor="w", command=lambda i=i: self.viewDetails(i,detailFrame))
            btn.config(height=75, width=60)
            btn.grid(row=7+i,columnspan=2, sticky=N+S+E+W)
            #self.accounts.append(name)
            i+=1
                    
    ## @brief Password Management Screen
    #  @details Where user can add and view account information
    #  @param *args A variable argument list
    def showPWPage(self, *args):

        ## @brief Updates scroll region when all widgets are in canvas
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        # Create beautiful canvas im picasso
        canvas = Canvas(self, bg=BG, width=280) # width=280
        canvas.pack(side=LEFT, fill='y')
        
        # Create scrollbar
        scrollbar = Scrollbar(self, command=canvas.yview, bg=BG)
        scrollbar.pack(side=LEFT, fill='y')

        # Attach scroll bar to canvas
        canvas.configure(yscrollcommand = scrollbar.set)

        # update scroll region
        canvas.bind('<Configure>', on_configure)

        # Add PWPage frame to canvas
        PWPage = Frame(canvas, bg=BG)
        canvas.create_window((0,0), window=PWPage, anchor='nw')

        # Add widgets
        instructions = Label(PWPage, bg=BG, fg=FG, text="Enter relevent information")
        instructions.grid(row=0, columnspan=2)
        nameL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Account Name")
        nameE = ttk.Entry(PWPage, font=LARGE, width=10)
        typeL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Account Type")
        typeE = ttk.Entry(PWPage, font=LARGE, width=10)
        userL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Username")
        userE = ttk.Entry(PWPage, font=LARGE, width=10)
        passL = Label(PWPage, bg=BG, fg=FG, font=LARGE, text="Password")
        passE = ttk.Entry(PWPage, font=LARGE, width=10)
        nameL.grid(row=1, column=0)
        nameE.grid(row=1, column=1)
        typeL.grid(row=2, column=0)
        typeE.grid(row=2, column=1)
        userL.grid(row=3, column=0)
        userE.grid(row=3, column=1)
        passL.grid(row=4, column=0)
        passE.grid(row=4, column=1)

        # Allows submit button to work when the user presses Enter key and calls addEntry method
        passE.bind('<Return>', lambda x: self.addEntry(PWPage, detailFrame, nameE, typeE, userE, passE))
        nameE.focus_set()

        # When clicked, addEntry method gets called with the frame name and relevant entries
        btn = Button(PWPage, text="Submit", bg=BGC, fg=BG, font=LARGE, command=lambda: self.addEntry(PWPage, detailFrame, nameE, typeE, userE, passE))
        btn.grid(row=5, columnspan=2, padx=5, pady=10)

        # Frame for showing details
        detailFrame = Frame(self, bg=BG)
        detailFrame.pack(expand=1)

        # Show existing entries
        self.showEntry(PWPage, detailFrame)


    ## @brief Add entry to database and display in scrollbar frame
    #  @details Adds entry to the database and the display
    #  @param scrollFrame The frame on the left which displays the entries as buttons
    #  @param detailFrame The frame on the right which displays details of each entry
    #  @param *pwd Variable list of entries from the user when he/she adds an entry
    def addEntry(self, scrollFrame, detailFrame, *pwd):
        AccName = pwd[0].get() # The account name
        AccType = pwd[1].get() # The account type
        UserName = pwd[2].get() # The username for the account
        Password = pwd[3].get() # Password for the account
        
        # Hash key as generated by encryption module
        HashKey = "Encrypted!"

        # Add entry to database
        database.Insert(len(database.Account.select())+1, AccName, AccType, UserName, Password, HashKey)

        #self.showEntry(scrollFrame, detailFrame)
        self.destroyF(scrollFrame)
        self.destroyF(detailFrame)
        self.showPWPage()

    ## @brief Displays details of entry
    #  @details Displays details of entry (type, name, username, password), called when button for entry is clicked
    #  @param idnum The id number of the entry that was clicked
    #  @param frame The frame in which to display the details on
    def viewDetails(self, idnum, frame):
        # Get full entry from database
        query = database.GetId(idnum)
        # Delete everything in frame currently
        self.destroyF(frame)
        # Add new details
        for i in range(len(FIELDS)):
            temp = Label(frame, text=FIELDS[i], bg=BG, fg=FG, font=LARGE)
            temp.grid(row=i, column=0, sticky=W)
            
        namelabel = Label(frame, text=query.AccName, font=LARGE)
        namelabel.grid(row=0, column=1)
        typelabel = Label(frame, text=query.AccType, font=LARGE)
        typelabel.grid(row=1, column=1)
        userlabel = Entry(frame, font=LARGE, width=12)
        userlabel.insert(0, query.UserName)
        userlabel.grid(row=2, column=1)
        passlabel = Entry(frame, font=LARGE, width=12)
        passlabel.insert(0, query.HashVal)
        passlabel.grid(row=3, column=1)

        copyU = Button(frame, text="C", bg=BGC, fg=BG, font=LARGE, command=lambda: Copy.copy(userlabel.get()))
        copyP = Button(frame, text="C", bg=BGC, fg=BG, font=LARGE, command=lambda: Copy.copy(passlabel.get()))
        copyU.grid(row=2, column=2)
        copyP.grid(row=3, column=2)

        editU = Button(frame, text="Save", bg=BGC, fg=BG, font=LARGE)
        editP = Button(frame, text="Save", bg=BGC, fg=BG, font=LARGE)
        editU.grid(row=2, column=3)
        editP.grid(row=3, column=3)

        genU = Button(frame, text="Generate", bg=BGC, fg=BG, font=LARGE, command=lambda: [f for f in [userlabel.delete(0, END),userlabel.insert(0, "random")]])
        genP = Button(frame, text="Generate", bg=BGC, fg=BG, font=LARGE, command=lambda: [f for f in [passlabel.delete(0, END),passlabel.insert(0, "random")]])
        genU.grid(row=2, column=4)
        genP.grid(row=3, column=4)

    def destroyF(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
   
# Runs application
app = PPP()
app.mainloop()
