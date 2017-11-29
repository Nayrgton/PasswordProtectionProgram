## @file setup.py
# @author Suhavi Sandhu
# @brief Builder script to make executable exe
# @date November 28, 2017

import sys
import os
import cx_Freeze
os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python\\tcl\\tk8.6"

include_files = [r"C:\Program Files (x86)\Python\DLLs\tcl86t.dll", \
                r"C:\Program Files (x86)\Python\DLLs\tk86t.dll", "ppp.ico", "icons/", "pppDatabase.db"]
# Dependencies are automatically detected, but it might need fine tuning.
base = None

if sys.platform == "win32":
    base = "Win32GUI"

ex = [cx_Freeze.Executable("PPP.py", base=base, icon="ppp.ico")]
build_exe_options = {"includes": ["os", "peewee"], "include_files": include_files}

# GUI applications require a different base on Windows (the default is for a
# console application).



cx_Freeze.setup(  name = "PasswordProtetionProgram",
        version = "1.0",
        description = "A user-friendly password manager",
        options = {"build_exe": build_exe_options},
        executables = ex)
