## @file PWChecking.py
#  @title Check Passwords
#  @author Suhavi Sandhu
#  @date November 10, 2017

import re

## @brief Checks master password at creation
#  @details Verifies that the password meets criteria
#  @param password The password that is being checked
def checkMP(password):
    if len(password) == 0:
        return "Password cannot be empty"

    elif len(password) < 8:
        return "Password must be at least 8 characters"

    elif not(re.search("[0-9]", password)):
        return "Password must have at least 1 number"
            
    elif not(re.search("[a-z]", password) and re.search("[A-Z]", password)):
        return "Password must have uppercase and lowercase"

    else:
        return True

## @brief Checks master password at login
#  @details Verifies that the entered password matches the actual
#  @param entered The password entered by the user
#  @param actual The real master password
def checkLogIn(entered, actual):
    #if len(entered) == 0:
    #    return "Password cannot be empty"
    if entered != actual:
        return "Incorrect password"
    elif entered == actual:
        return True
