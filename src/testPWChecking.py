## @title testPWChecking.py
#  @brief This file unittests the functions used to test password checking at registration and login
#  @author Suhavi Sandhu
#  @date November 28, 2017

import unittest
import PWChecking
import GenPassword

## @brief This class is used to test the functions in Encrypt.py
class testEncrypt(unittest.TestCase):

    ## @brief This method creates various passwords and their associated keys
    def setUp(self):
        self.p1 = "Password123"
        self.p2 = "password"
        self.p3 = "
        self.p2 = ""
        self.p3 = GenPassword.genPassCrypt()
        
      

    '''
    ## @brief This method deletes all password objects
    def tearDown(self):
        self.p1 = None   
        self.p2 = None
        self.p3 = None
        self.p4 = None
    '''

    ## @brief This method is used to test if the decoded password matched the original password.
    def test_cryptDecode(self):
        self.assertEqual(Encrypt.cryptDecode(self.k1, self.e1), self.p1)
        self.assertEqual(Encrypt.cryptDecode(self.k2, self.e2), self.p2)
        self.assertEqual(Encrypt.cryptDecode(self.k3, self.e3), self.p3)
        #self.assertEqual(Encrypt.cryptDecode(self.k4, self.e4), self.p4) 


if __name__ == '__main__':
    unittest.main()
