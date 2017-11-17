## @file GenPassword.py
#  @brief This module is used to generate a random password containing alphanumeric characters
#  @author Shabana Dhayananth
#  @date October 27, 2017

import string
import sys
import random

## @brief This function generates a random password consisting of upper case, lower case alphanumeric characters
#  @details default random number generator's sequences can be reproduced, in case SystemRandom() is not available on user system
#  @return random password consisting of 8 characters
def genPass():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8))

## @brief This function generates a random password consisting of upper case, lower case alphanumeric characters
#  @details Same as genPass() but uses SystemRandom() to generate random numbers so sequences are not reproducible
#  @return random password consisting of 8 characters
def genPassCrypt():
   return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8)) 
