# Location-based Cryptography
#### Package published at: [PyPI](https://pypi.org/project/locationcrypto/)
[![Downloads](https://static.pepy.tech/personalized-badge/locationcrypto?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/locationcrypto)

---

Location based cryptography uses location of the device in addition to pass-phrase as encryption/decryption key.

#### Install:
```bash
pip install locationcrypto
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
