## @file testResponseTime.py
#  @brief To test that the application responds within the appropriate time
#  @author Suhavi Sandhu
#  @date December 6, 2017

import unittest
import PPP
import Constants
import PWChecking
import time
from tkinter import *

## @brief This class is used to test that performance requirements are met
class testResponseTime(unittest.TestCase):

    ## @brief Test processing time of reset timer
    #  @details If ran for too long, inactivity method throws error. Note in test report.
    def test_NFR_PER_1(self):       
        gui = PPP.PPP()
        gui.withdraw
        start = time.time()
        PPP.reset_timer()
        end = time.time()
        self.assertTrue((end-start) <= Constants.PROC_TIME)
        
    ## @brief Test error time
    def test_NFR_PER_2(self):
        start = time.time()
        PWChecking.checkMP("Password")
        end = time.time()
        self.assertTrue((end-start) <= Constants.ERR_TIME)

if __name__ == '__main__':
    unittest.main()
