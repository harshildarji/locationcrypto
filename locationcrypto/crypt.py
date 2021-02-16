# Location Based Cryptography

import geocoder, hashlib

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plain_text: str, key: str):
    location = "".join(map(str, geocoder.ip("me").latlng))
    key = hashlib.md5((key + location).encode("utf-8")).hexdigest()
    return translateMessage(key, plain_text, "encrypt")


def decrypt(encrypted_text: str, key: str):
    location = "".join(map(str, geocoder.ip("me").latlng))
    key = hashlib.md5((key + location).encode("utf-8")).hexdigest()
    return translateMessage(key, encrypted_text, "decrypt")


def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == "encrypt":
                num += LETTERS.find(key[keyIndex])
            elif mode == "decrypt":
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return "".join(translated)
