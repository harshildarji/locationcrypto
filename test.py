from locationcrypto import crypt

encryption = crypt.encrypt(plain_text='Harshil', key='test')
print(f'Encryption: {encryption}')

decryption = crypt.decrypt(encrypted_text=encryption, key='test')
print(f'Decryption: {decryption}')