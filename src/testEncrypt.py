import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generKey():
    password = b"passprotprog" #what you want to encode with?
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
     )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key) #need to store this somewhere to be able to decrypt 
    return f
    #token = f.encrypt(inp)
    #return token
    #print(token)
    #print(f.decrypt(token))

#diff key per password or all same key?

def cryptEncode(f, passw):
    inp = passw.encode(encoding= 'utf-8')
    token = f.encrypt(inp)
    #print(f.decrypt(token)) = g.decrypt(cryptEncode(g, "plswork"))
    return token


#infile = open("Passwords.txt","r").read().strip().split("\n")
#for i in infile:
#    print(token(i))
