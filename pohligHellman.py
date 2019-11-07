# Author: Ryan Habershaw
# Date: 7 November, 2019
#
# This program is for the famous Pohlig-Hellman exponentiation cipher.
# The user will input the message they wish to be encrypted, the exponent 'e',
# and the prime 'p'. Output will be given in the form of the encrypted integer.


### Libraries ###
import math
#################

secret = int(input('Enter message: '))  # Message to be encrypted
e = int(input('Enter exponent: '))  # Exponent used in formula
p = int(input('Enter prime: '))  # Prime used in formula

superSecret = secret ** e % p

print(superSecret)

# End
