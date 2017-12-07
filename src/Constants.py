## @file Constants.py
# @author Suhavi Sandhu
# @brief The constants being used in the GUI file (fonts, colours)
# @date November 10, 2017


# Colours
BGC = "#cccccc"
BG = "#383A39"
FG = "#A1DBCD"

#Fonts
LARGE = ("Helvetica", 16)

# Screen size
screen_size = "820x640"

# Dependent files
EYE = "icons/eye.gif"
COPY = "icons/copy.gif"
GENERATE = "icons/flash.gif"
DELETE = "icons/delete.gif"
LOGO = "icons/ppp.gif"
ICON = "icons/ppp.ico"

WELCOME = "Welcome to the Password Protection Program"

# States for Register screen
REGISTER = {
    "prompt": "Create a master password to start using the application. Must have lowercase, uppercase, numbers and at least 8 characters",
    "loggedIn": False }

# States for LogIn screen
LOGIN = {
    "prompt": "Enter your master password",
    "loggedIn": True }

FIELDS = ["Name", "Type", "Username", "Password"]

# Error Time
ERR_TIME = 1000

# Processing Time
PROC_TIME = 1000

USERMANUAL = "..\\Doc\\UserGuide\\UserGuide.pdf"

# User Manual
INSTRUCTIONS = "1) Add entries on the top-left hand corner!\
                2) Generate a username/password using the lightning icon.                             \
                3) View entries by clicking the buttons with an eyeball.                              \
                4) Edit entry by viewing and updating on this side of the screen.                     \
                NOTE: If you are still having trouble, read the user manual by clicking below. "


# Inactivity Period 
INACTIVITY = 30000 # Changed to 30 seconds instead of 1 minute for testing
