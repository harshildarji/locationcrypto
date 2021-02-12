### Location-based Cryptography
[![PyPI version](https://badge.fury.io/py/locationcrypto.svg)](https://badge.fury.io/py/locationcrypto)

Location based cryptography uses location of the device in addition to pass-phrase as encryption/decryption key.

#### Install:
```bash
pip install locationcrypto==1.0.1
```

#### Use:
Create a python script, for example **`example.py`**:
```python
import locationcrypto.crypt

crypt
```
Save and run:
```bash
❯❯❯ python3 example.py
Waiting for location...
Password: test
Data: Harshil
Encrypt/Decrypt [e/d]: e
Jevujhk
```
```bash
❯❯❯ python3 example.py
Waiting for location...
Password: test
Data: Jevujhk
Encrypt/Decrypt [e/d]: d
Harshil
```

---
#### Author: [Harshil Darji](https://github.com/harshildarji)

Thanks to [Atharv Attri](https://github.com/Atharv-Attri) for helping me publish this repository as a package.
