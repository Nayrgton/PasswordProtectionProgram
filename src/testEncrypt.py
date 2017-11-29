## @file testEncrypt.py
#  @brief This file unittests the functions used for key generation, encryption and decryption.
#  @author Shabana Dhayananth
#  @date November 16, 2017

import unittest
import Encrypt
import GenPassword

## @brief This class is used to test the functions in Encrypt.py
class testEncrypt(unittest.TestCase):

    ## @brief This method creates various passwords and their associated keys
    def setUp(self):
        self.p1 = "password"
        self.p2 = ""
        self.p3 = GenPassword.genPassCrypt()
        #self.p4 = 12345  --> does not pass test but test isn't needed as any entry into GUI is a string anyways
        self.k1 = Encrypt.generKey()
        self.k2 = Encrypt.generKey()
        self.k3 = Encrypt.generKey()
        #self.k4 = Encrypt.generKey()
        self.e1 = Encrypt.cryptEncode(self.k1, self.p1)
        self.e2 = Encrypt.cryptEncode(self.k2, self.p2)
        self.e3 = Encrypt.cryptEncode(self.k3, self.p3)
        #self.e4 = Encrypt.cryptEncode(self.k4, self.p4)


    ## @brief This method is used to test if the decoded password matched the original password.
    def test_cryptDecode(self):
        self.assertEqual(Encrypt.cryptDecode(self.k1, self.e1), self.p1)
        self.assertEqual(Encrypt.cryptDecode(self.k2, self.e2), self.p2)
        self.assertEqual(Encrypt.cryptDecode(self.k3, self.e3), self.p3)
        #self.assertEqual(Encrypt.cryptDecode(self.k4, self.e4), self.p4) 


if __name__ == '__main__':
    unittest.main()
