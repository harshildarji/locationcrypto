# Location-based Cryptography
#### Package published at: [PyPI](https://pypi.org/project/locationcrypto/)
[![Downloads](https://pepy.tech/badge/locationcrypto)](https://pepy.tech/project/locationcrypto)

---

Location based cryptography uses location of the device in addition to pass-phrase as encryption/decryption key.

#### Install:
```bash
pip install locationcrypto
```

#### Use:
Create a python script, for example **`example.py`**:
```python
from locationcrypto import crypt

# To encrypt:
encryption = crypt.encrypt(plain_text='Harshil', key='test')
print(f'Encryption: {encryption}')

# To decrypt:
decryption = crypt.decrypt(encrypted_text=encryption, key='test')
print(f'Decryption: {decryption}')
```
Save and run:
```bash
❯❯❯ python3 example.py
Encryption: Jevujhk
Decryption: Harshil
```

---
#### Author: [Harshil Darji](https://github.com/harshildarji)

Thanks to [Atharv Attri](https://github.com/Atharv-Attri) for helping me publish this repository as a package.
