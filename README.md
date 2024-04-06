# digital-signature-based-rsa

Digital signature based on RSA using Python and simple mathematical algorithms.

## Usage

512: the size of prime numbers stored in bits

```python
if __name__ == '__main__':
    p, q, n, private_key, public_key = key_generate(512)

    message = "Your text."
    signature = signature_generate(p, q, message, private_key)

    print(f'Signature: {signature}')
    print(f'Verification: {signature_verify(message, signature, public_key, n)}')
    print(f'Decrypted message: {get_message_from_signature(signature, public_key, n)}')
```

## Important

The larger the number of bits you specify in the ```key_generation(bit_size)``` function, the longer the program takes to run!
