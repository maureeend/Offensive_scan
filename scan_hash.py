#!/usr/bin/python3
#-*- coding:utf-8 -*-

import hashlib

# Dico hash
hash_algorithms = {
    'sha256': hashlib.sha256,
    'md5': hashlib.md5,
    'sha1': hashlib.sha1
}


# Hash wordlist
def hash_message(algorithm, password):
    password_bytes = password.encode('utf-8')
    hash_function = hash_algorithms[algorithm]()
    hash_function.update(password_bytes)
    return hash_function.hexdigest()


# Crack hash
def crack_hash(user_hash, algorithm, wordlist):
    try:
        with open("rockyou.txt", 'r', encoding="latin-1") as wordlist:
            for word in wordlist:
                word = word.strip()
                if hash_message(algorithm, word) == user_hash:
                    return word
        return None
    except FileNotFoundError:
        print("Wordlist not found")
        return None

if __name__ == "__main__":
    user_hash = input("Hash to crack: ")
    algorithm = input("Hash algorithm (sha256/md5/sha1): ")
    wordlist = "rockyou.txt"

    if algorithm not in hash_algorithms:
        print("Unsupported algorithm!")
    else:
        result = crack_hash(user_hash, algorithm, wordlist)
        if result:
            print(f"Hash cracked! Password: {result}")

            



