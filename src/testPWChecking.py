## @file testPWChecking.py
#  @brief This file unittests the functions used to test password checking at registration and login
#  @author Suhavi Sandhu
#  @date November 28, 2017

import unittest
import PWChecking

## @brief This class is used to test the functions in PWChecking.py
class testPWChecking(unittest.TestCase):

    ## @brief This method creates various passwords for creation as well as checking upon login
    def setUp(self):
        self.mp1 = "Passw0rd" # mp1
        self.mp2 = "Passworddd" #mp2
        self.mp3 = "pword" #mp3
        self.mp4 = "password123" #mp4
        self.mp5 = "" #mp5

        self.actual = "Passw0rd" # for tests below
        self.mp6 = "" # mp6
        self.mp7 = "Passw0rd" #mp7
        self.mp8 = "pword" #mp8
        
    ## @brief This method is used to test FR-MP-1, which checks that a password with at least 8 characters, at least 1 uppercase and at least one number returns True
    def test_FRMP1(self):
        self.assertEqual(PWChecking.checkMP(self.mp1), True)

    ## @brief This method is used to test FR-MP-2, which checks that a password without any numbers gives the appropriate message
    def test_FRMP2(self):
        self.assertEqual(PWChecking.checkMP(self.mp2), "Password must have at least 1 number")

    ## @brief This method is used to test FR-MP-3, which checks that a password with less than 8 characters gives the appropriate message
    def test_FRMP3(self):
        self.assertEqual(PWChecking.checkMP(self.mp3), "Password must be at least 8 characters")

    ## @brief This method is used to test FR-MP-4, which checks that a password without uppercase gives the appropriate message
    def test_FRMP4(self):
        self.assertEqual(PWChecking.checkMP(self.mp4), "Password must have uppercase and lowercase")

    ## @brief This method is used to test FR-MP-5, which checks that an empty password gives the appropriate message
    def test_FRMP5(self):
        self.assertEqual(PWChecking.checkMP(self.mp5), "Password cannot be empty")

    ## @brief This method is used to test FR-MP-6, which checks that an empty password upon login gives the appropriate message
    #def test_FRMP6(self):
     #   self.assertEqual(PWChecking.checkLogIn(self.mp6, self.actual), "Password cannot be empty")

    ## @brief This method is used to test FR-MP-7, which checks that a password upon login that is same as actual returns True
    def test_FRMP7(self):
        self.assertEqual(PWChecking.checkLogIn(self.mp7, self.actual), True)
        
    ## @brief This method is used to test FR-MP-8, which checks that a password upon login that is not the same as actual gives the appropriate message
    def test_FRMP8(self):
        self.assertEqual(PWChecking.checkLogIn(self.mp8, self.actual), "Incorrect password")
      
        
if __name__ == '__main__':
    unittest.main()
