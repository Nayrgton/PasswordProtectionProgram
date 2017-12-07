## @file Copy.py
# @author Suhavi Sandhu
# @brief Copies the text after the user clicks a button
# @date November 10, 2017

import pyperclip

## @brief Copies the text
#  @param text The text to be copied
def copy(text):
    pyperclip.copy(text)
