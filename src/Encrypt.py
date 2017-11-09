## @file Encrypt.py
#  @title Password Encryption
#  @author Shabana Dhayananth
#  @date October 15, 2017

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

## @brief This function generates a unique) key (for encoding user passwords) using Python's Fernet library
#  @details key is a  
#  @return 
def generKey():
    password = b"passprotprog" #what you want to encode with
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
     )
    key = base64.urlsafe_b64encode(kdf.derive(password)) #need to store this somewhere (in database) to be able to decrypt  
    print (key)
    #f = Fernet(key)
    return key

## @brief This function uses a key to encrypt an input string
#  @details 
#  @param key, passw refer to the key to be used to encypt and the password to be encrypted
#  @return encrypted password (string of Unicode characters)
def cryptEncode(key, passw):
    f = Fernet(key)
    inp = passw.encode(encoding= 'utf-8')
    encrypted = f.encrypt(inp)
    return encrypted

def cryptDecode(key, encrypted):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    return decrypted

'''
IDLE
key = generKey()
x = cryptEncode(key, "hellooo")
a = cryptDecode(key, x)
'''

#infile = open("Passwords.txt","r").read().strip().split("\n")
#for i in infile:
#    print(token(i))


