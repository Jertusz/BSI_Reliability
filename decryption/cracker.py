"""
Author: Jedrzej Szadejko
pycryptodome: https://pypi.org/project/pycryptodome/
"""

import sys
import random
import argparse
import itertools
from string import ascii_lowercase
from Crypto.Cipher import DES3, DES, AES
from Crypto.Util.Padding import unpad
import multiprocessing.dummy as mp
import time
print(sys.maxsize)

encoded_text = b"M\xe9\x07M\x0c\x1f3\xa0\x88L\x08\xde\x9c[\xac\x97;\xe3\xac\x02z\xde\xc7'\xcdx+\xfc\x9b\x0fcr \xed\x0fX\xab\xe7\xed\xba}\xefP\x90-\x92\xb9\xe4+\xc5\xc0\xc4\xc1\x01\xd1oZ\x1eD*\xc6\xf6Ze\xe1\xc8i\xec\x94\xa9\xf0~\xa3\xf1\r]6M\x97\xc8\x80\xce\x1a\x0f\xc9Ky\xd0\x07c=YL\xc1\xff\xb99b\x08\xda\xce\x93\x05\xfc\xe3\x8c\x11\xf7w\xce\xec$\xceu\xb8\xbf\xd5xI\x97\xe1\xe4\xfaK\x11\xb2z\xaaP,Q\xe7\xb7<\xef7\xff\x862\xd0dz^\xb5\r\x89\x8a\xd2d\x8d\xc8\xe7q\xe7\x1e89\x9aN9\x11\xdaHX\xb6\xb0\xe2\x8b^Z\xd3\x87P\xe7;\x87\xd1z^\xa3!\x12g*f\xb1Fe\xdd\x1a\xeb\xde\xc3\x8d\xfd\x99\x7f\xb7\xc4\xdd\x94\xf6\xdd\xd71\x9b\x0e\x04:\x18-\xee}\x0f\xa8#\x15ff\x9a\x9d\xfb\x8fl"
with open("wulgaryzmy", "r") as f:
    profanities = f.read().split()



i = 1
sol = []
rand = []
for possible_pass in itertools.product(ascii_lowercase, repeat=8):
    z = "".join(possible_pass).encode()
    des = DES.new(z, DES.MODE_ECB)
    decrypted = des.decrypt(encoded_text)
    try:
        unpadded = unpad(decrypted, 32)
        decoded = unpadded.decode()
        print(decoded)
        rand.append(decoded)
        if any(profanity in decoded for profanity in profanities):
            print(possible_pass, decoded)
            sol.append((possible_pass, decoded))
    except ValueError as e:
        pass
    if i%1000000 == 0:
        print("sol", sol)
        print("rand", rand)
    i+=1

print(sol)
print(rand)
