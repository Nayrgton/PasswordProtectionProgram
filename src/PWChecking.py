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


def checkLogIn(entered, actual):
    if len(entered) == 0:
        return "Password cannot be empty"
    elif entered != actual:
        return "Incorrect password"
    elif entered == actual:
        return True
