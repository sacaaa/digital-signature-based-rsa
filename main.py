from argparse import ArgumentParser
from helper import generate_prime, extended_euclidean, chinese_remainder_theorem, fast_exponentiation
from random import randrange


def key_generate(bit_size: int = 256) -> tuple[int, int, int, int, int]:
    """Generate public and private keys.

    :return: p, q, n, d, e where p, q are prime numbers, n = p * q, d is the private key, e is the public key
    """

    p, q = generate_prime(bit_size), generate_prime(bit_size)

    while p == q:
        q = generate_prime()

    n, pn = p * q, (p - 1) * (q - 1)
    e = randrange(2, pn)
    lnko, x, d = extended_euclidean(pn, e)

    while lnko != 1:
        e = randrange(2, pn)
        lnko, x, d = extended_euclidean(pn, e)

    if d < 0:
        d = d + pn

    return p, q, n, d, e


def signature_generate(p: int, q: int, message: str, private_key: int) -> int:
    """Generate signature for the message.

    :param p: Prime number
    :param q: Prime number
    :param message: Message to sign
    :param private_key: Private key
    :return: Signature
    """

    message = int.from_bytes(message.encode(), 'big')

    n = p * q
    if n < message:
        raise ValueError('Modulus is smaller than the message! Increase the bit size of the prime numbers '
                         'in the key_generation(bit_size) function.')

    return chinese_remainder_theorem(p, q, message, private_key)


def signature_verify(message: str, signature: int, public_key: int, n: int) -> bool:
    """Verify the signature.

    :param message: Message to verify
    :param signature: Signature
    :param public_key: Public key
    :param n: Modulus
    :return: True if the signature is valid, False otherwise
    """

    message = int.from_bytes(message.encode(), 'big')

    return message == fast_exponentiation(signature, public_key, n)


def get_message_from_signature(signature: int, public_key: int, n: int) -> str:
    """Get the message from the signature.

    :param signature: Signature
    :param public_key: Public key
    :param n: Modulus
    :return: Message
    """

    message = fast_exponentiation(signature, public_key, n)
    return message.to_bytes((message.bit_length() + 7) // 8, 'big').decode()


if __name__ == '__main__':
    parser = ArgumentParser(description='Generate a digital signature for a message.')
    parser.add_argument('bit_size', type=int, help='Bit size for key generation.')
    parser.add_argument('message', type=str, help='The message to sign.')
    args = parser.parse_args()

    p, q, n, private_key, public_key = key_generate(args.bit_size)
    message = args.message
    signature = signature_generate(p, q, message, private_key)

    print(f'Signature: {signature}\n'
          f'Public key: {public_key}\nModulus: {n}\n'
          f'Verification: {signature_verify(message, signature, public_key, n)}\n'
          f'Decrypted message: {get_message_from_signature(signature, public_key, n)}')
