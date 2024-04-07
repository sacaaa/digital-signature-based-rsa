# digital-signature-based-rsa

This repository contains a Python script that implements a digital signature system and provides functionality for decoding the signature. The script uses RSA-like encryption and decryption methods, along with simple mathematical algorithms for efficient computation.

## Features

- Key generation
- Signature generation
- Signature verification
- Message decryption from signature

## Requirements

- Python 3.6 or higher

## Encrypt

You can run the `encrypter.py` script from the command line with the following command:

```bash
python encrypter.py <bit_size> "<message>"
```

Replace <bit_size> with the desired bit size for key generation and <message> with the message you want to sign.

For example:
```bash
python encrypter.py 512 "Hello, World!"
```

## Decrypt
You can run the `decrypter.py` script from the command line with the following command:

```bash
python decrypter.py <signature> <public_key> <modulus>
```

Replace <signature>, <public_key>, and <modulus> with the signature to verify, the public key used for verification, and the modulus used for verification, respectively.

For example:
```bash
python decrypter.py 855924288 683203879 1548022963
```

## Important
The larger the number of bits you specify when calling the program from the command line, the longer the program takes to calculate!

If the length of the message to be encrypted exceeds the length of the modulus, then the RSA algorithm will not properly encrypt the message, and you will encounter a `ValueError`. In this case, increase the bit size of the prime numbers when calling the program from the command line.
