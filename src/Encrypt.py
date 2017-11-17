## @file Encrypt.py
#  @brief This module handles the key generation for and encryption/decryption of passwords
#  @author Shabana Dhayananth
#  @date October 15, 2017

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

## @brief This function generates a unique) key (for encoding user passwords) using Python's Fernet library
#  @details key derived from a string that is run through the kdf (key derivation function)
#  @return key that will be used to encode the user passwords (32 bytes)
def generKey():
    password = b"passprotprog" #what you want to encode with
    salt = os.urandom(16)
    #PBKDF2HMAC derives cryptographic key from password by key stretching
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
     )
    key = base64.urlsafe_b64encode(kdf.derive(password)) #need to store this somewhere (in database) to be able to decrypt  
    return key

## @brief This function uses a key to encrypt an input string
#  @details Fernet uses symmetric encryption on the input key
#  @param key, passw refer to the key to be used to encypt and the password to be encrypted
#  @return encrypted password in byte format
def cryptEncode(key, passw):
    f = Fernet(key)
    inp = passw.encode(encoding= 'utf-8')
    encrypted = f.encrypt(inp)
    return encrypted


## @brief This function uses the saved key to decrypt the encrypted user password stored in the database
#  @param key, encrypted refer to the key that was used to encrpt the password and the encrypted password
#  @return decrypted password in string format
def cryptDecode(key, encrypted):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    decrypted = str(decrypted, 'utf-8')
    return decrypted

'''
Function Call Syntax (for reference)
key = generKey()
encryptedPassword = cryptEncode(key, "hellooo")
decryptedPassword = cryptDecode(key, x)
'''


