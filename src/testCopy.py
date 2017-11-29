## @file testCopy.py
#  @brief This file unittests the functions used to copy words
#  @author Suhavi Sandhu
#  @date November 28, 2017

import unittest
import Copy
import tkinter as tk

## @brief This class is used to test the functions in Copy.py
class testPWChecking(unittest.TestCase):

    ## @brief This method creates a tkinter window
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw
        self.c1 = "Password"
        
    ## @brief This method is used to test FR-N-5, which tests the copy function
    def test_FRN5(self):
        Copy.copy(self.c1)
        self.assertEqual(self.root.clipboard_get(), self.c1)

        
if __name__ == '__main__':
    unittest.main()
