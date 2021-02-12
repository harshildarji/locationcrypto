# Location Based Cryptography

import geocoder, hashlib

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('Waiting for location...')
    location = ''.join(map(str, geocoder.ip('me').latlng))
    key = hashlib.md5((input('Password: ')+location).encode('utf-8')).hexdigest()
    message = input('Data: ')
    mode = input('Encrypt/Decrypt [e/d]: ')

    if mode.lower().startswith('e'):
        mode = 'encrypt'
        translated = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
        mode = 'decrypt'
        translated = decryptMessage(key, message)
    print(translated)
    exit()

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
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
    return ''.join(translated)

#if __name__ == '__main__':
main()
