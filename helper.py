from random import getrandbits


def fast_exponentiation(base: int, exponent: int, mod: int) -> int:
    """Fast exponentiation algorithm.

    :param base: Base number
    :param exponent: Exponent
    :param mod: Modulus
    :return: Result of the fast exponentiation
    """
    
    result = 1
    base = base % mod

    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        exponent >>= 1
        base = (base * base) % mod

    return result


def miller_rabin(p: int, a: int) -> bool:
    """Miller-Rabin primality test.

    :param p: Number to test
    :param a: Witness
    :return: True if p is probably prime, False otherwise
    """

    if p % 2 == 0:
        return False

    d, s = p - 1, 0

    while d % 2 == 0:
        d //= 2
        s += 1

    if fast_exponentiation(a, d, p) == 1:
        return True

    for r in range(s):
        if fast_exponentiation(a, d * (2 ** r), p) == p - 1:
            return True

    return False


def euclidean(a, b, x=[1, 0], y=[0, 1]):
    """Extended Euclidean algorithm.

    :param a: First number
    :param b: Second number
    :param x: Coefficient x
    :param y: Coefficient y
    """

    tmp = a % b

    if tmp == 0:
        n = len(x) - 1
        x, y = x[-1] * (-1) ** n, y[-1] * (-1) ** (n + 1)

        return a, b, x, y
    elif tmp < 0:
        raise "Minus result"

    x.append(a // b * x[-1] + x[-2])
    y.append(a // b * y[-1] + y[-2])

    return euclidean(b, tmp, x, y)


def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclidean algorithm.

    :param a: First number
    :param b: Second number
    :return: Greatest common divisor, x, y where a * x + b * y = gcd(a, b)
    """

    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def chinese_remainder_theorem(p: int, q: int, c: int, d: int) -> int:
    """Chinese remainder theorem.

    :param p: Prime number
    :param q: Prime number
    :param c: Encrypted message
    :param d: Private key
    :return: Decrypted message
    """

    M = p * q
    M1, M2 = M // p, M // q
    C1, C2 = fast_exponentiation(c, d % (p - 1), p), fast_exponentiation(c, d % (q - 1), q)
    _, y1, y2 = extended_euclidean(q, p)

    return (C1 * y1 * M1 + C2 * y2 * M2) % M


def generate_prime(size: int = 256) -> int:
    """Generate prime number.

    :param size: Size of the prime number in bits
    :return: Prime number
    """

    while True:
        p = getrandbits(size)
        if miller_rabin(p, 2):
            return p
