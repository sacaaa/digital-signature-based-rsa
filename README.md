# digital-signature-based-rsa

Simple digital signature based on RSA using Python.

## Usage

512: the size of prime numbers stored in bits

```python
if __name__ == '__main__':
    p, q, n, private_key, public_key = key_generate(512)

    message = "Teszt szöveg a digitális aláírás ellenőrzéséhez."
    signature = signature_generate(p, q, message, private_key)

    print(f'Signature: {signature}')
    print(f'Verification: {signature_verify(message, signature, public_key, n)}')
    print(f'Decrypted message: {get_message_from_signature(signature, public_key, n)}')
```
