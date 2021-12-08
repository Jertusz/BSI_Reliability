"""
Author: Jedrzej Szadejko
pycryptodome: https://pypi.org/project/pycryptodome/
"""

import random
import argparse
from Crypto.Cipher import DES3, DES, AES

AES_KEY = b'Sixteen_byte_key'
DES3_KEY = b'Sixteen_byte_key'
DES_KEY = b'-8B_key-'

#Simulate random files to encrypt
targets = set()
while len(targets) < 10:
    targets.update((random.randint(1,20),))


def log(algorithm_name, file_number):
    """
    Logs details of encryption to console

    Parameters:
    algorithm_name (str): Algorithm used to encrypt
    file_number (int): Number of file which was encrypted
    """
    print(
        f"Report:\n\
        Encrypted: ./disc_sim/text{file_number}.txt\n\
        Key file: ./disc_sim/{algorithm_name}_key_text{file_number}.txt\n\
        Output: ./disc_sim/{algorithm_name}_encrypted_text{file_number}.txt\n"
    )

def encrypt(algorithm_name, algorithm, key):
    """
    Function responsible for encrypting files with provided algorithm

    Parameters:
    algorithm_name (str): Name of the algorithm to use
    algorithm: Correct algorithm class imported from pycryptodome
    key (bin): Key used to encrypt files
    """
    for target in targets:
        cipher = algorithm.new(key, algorithm.MODE_EAX)
        nonce = cipher.nonce
        with open(f"disc_sim/text{target}.txt", "rb") as opened_file:
            data = opened_file.read()
        with open(f"disc_sim/{algorithm_name}_encrypted_text{target}.txt", "wb") as opened_file:
            ciphertext, tag = cipher.encrypt_and_digest(data)
            opened_file.write(ciphertext)
        with open(f"disc_sim/{algorithm_name}_key_text{target}.txt", "wb") as opened_file:
            byte_string = key + b"\n" + nonce + b"\n" + tag
            opened_file.write(byte_string)
        log(algorithm_name, target)

def decrypt(algorithm_name, algorithm, files):
    """
    Function responsible for decrypting files with provided algorithm

    Parameters:
    algorithm_name (str): Name of the algorithm to use
    algorithm: Correct algorithm class imported from pycryptodome
    files (list): List of files to decrypt
    """
    for file in files:
        try:
            with open(f"disc_sim/{algorithm_name}_key_{file}", "rb") as opened_file:
                key, nonce, _ = opened_file.readlines()
                key = key[:-1]
                nonce = nonce[:-1]
        except FileNotFoundError:
            print(f"./disc_sim/{file} does not have a suitable key to decrypt")
            continue
        cipher = algorithm.new(key, algorithm.MODE_EAX, nonce=nonce)
        with open(f"disc_sim/{algorithm_name}_encrypted_{file}", "rb") as opened_file:
            data = opened_file.read()
            plaintext = cipher.decrypt(data)
        with open(f"disc_sim/decrypted_{file}", "wb") as opened_file:
            opened_file.write(plaintext)
        print(f"Decrypted: ./disc_sim/{file}")

def main():
    """
    Driver function responsible for parsing CLI arguments and choosing correct algorithm
    """
    algorithms = {
            "AES": {
                "algorithm_name": "aes",
                "algorithm": AES,
                "key": AES_KEY
                },
            "DES": {
                "algorithm_name": "des",
                "algorithm": DES,
                "key": DES_KEY
                },
            "DES3": {
                "algorithm_name": "des3",
                "algorithm": DES3,
                "key": DES3_KEY
                },
            }

    parser = argparse.ArgumentParser()
    parser.add_argument('-encrypt', help='Encrypt random files', action='store_true')
    parser.add_argument('-decrypt', help='Decrypt provided files', action='store_true')
    parser.add_argument(
            '-a', '--algorithm',
            choices=["AES", "DES", "DES3"], help='Specify which algorithm to use [AES, DES, DES3]'
            )
    parser.add_argument('-f', '--files', nargs='+', help='Specify which files to decrypt')
    args = parser.parse_args()

    if args.encrypt:
        if args.algorithm:
            encrypt(**algorithms[args.algorithm])
        else:
            print("No algorithm specified, using AES")
            encrypt(**algorithms["AES"])
    elif args.decrypt:
        if args.algorithm and args.files:
            algorithm_name, algorithm, _ = algorithms[args.algorithm].values()
            decrypt(algorithm_name, algorithm, args.files)


main()
