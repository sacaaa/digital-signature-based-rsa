# digital-signature-based-rsa

Digital signature based on RSA using Python and simple mathematical algorithms.

## Features

- Key generation
- Signature generation
- Signature verification
- Message decryption from signature

## Requirements

- Python 3.6 or higher

## Usage

You can run the main script from the command line with the following command:

```bash
python main.py <bit_size> "<message>"
```

Replace <bit_size> with the desired bit size for key generation and <message> with the message you want to sign.

For example:
```bash
python main.py 512 "Hello, World!"
```

## Important
The larger the number of bits you specify when calling the program from the command line, the longer the program takes to calculate!

If the length of the message to be encrypted exceeds the length of the modulus, then the RSA algorithm will not properly encrypt the message, and you will encounter a ```ValueError```. In this case, increase the bit size of the prime numbers when calling the program from the command line.
