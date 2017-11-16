## @file inactivity.py
# @author Suhavi Sandhu
# @brief Tracks how long user is inactive
# @date November 10, 2017

from tkinter import *

## @briefs Does something when user is inactive
def inactive():
    print("do something")

## @brief resets the timer
#  @param app The GUI
#  @param event optional
def reset_timer(app, event=None):
    app.after_cancel(timer)
    timer = app.after(100, inactive)

## @brief resets the timer
#  @param app The GUI
def config_reset(app):
    app.bind_all('<Any-KeyPress>', reset_timer)
    app.bind_all('<Any-ButtonPress>', reset_timer)


