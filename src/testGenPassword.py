## @file testGenPassword.py
#  @brief This file unittests the the function used to generate random strings for username and password.
#  @details The randomness of the values cannot be tested but the requirements for the string can be tested.
#  @author Shabana Dhayananth
#  @date November 28, 2017

import unittest
import GenPassword

## @brief This class is used to test the functions in GenPassword.py
class testGenPassword(unittest.TestCase):

    ## @brief This method creates various passwords and their associated keys
    def setUp(self):
        self.p1 = GenPassword.genPassCrypt()
        self.p2 = GenPassword.genPassCrypt()
        self.p3 = GenPassword.genPassCrypt() 

    ## @brief These methods are used to test if the generated string is 8 characters long and contains the necessary security features.
    def test_GenPass1(self):
        self.assertEqual(len(self.p1), 8)  #checks if length is 8
        self.assertTrue(any (i.isdigit() for i in self.p1))  #checks if contains a number
        self.assertTrue(any (i.islower() for i in self.p1))  #checks if contains a lower case
        self.assertTrue(any (i.isupper() for i in self.p1))  #checks if contains an upper case

    def test_GenPass2(self):
        self.assertEqual(len(self.p2), 8)
        self.assertTrue(any (i.isdigit() for i in self.p2))
        self.assertTrue(any (i.islower() for i in self.p2))  
        self.assertTrue(any (i.isupper() for i in self.p2)) 

    def test_GenPass3(self):
        self.assertEqual(len(self.p3), 8)
        self.assertTrue(any (i.isdigit() for i in self.p3))
        self.assertTrue(any (i.islower() for i in self.p3))  
        self.assertTrue(any (i.isupper() for i in self.p3)) 


if __name__ == '__main__':
    unittest.main()
