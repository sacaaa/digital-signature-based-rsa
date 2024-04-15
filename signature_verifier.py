from argparse import ArgumentParser
from signature_generator import signature_verify, get_message_from_signature

if __name__ == "__main__":
    parser = ArgumentParser(description='Verify a digital signature and decrypt the message.')
    parser.add_argument('signature', type=int, help='The signature to verify.')
    parser.add_argument('public_key', type=int, help='The public key used for verification.')
    parser.add_argument('modulus', type=int, help='The modulus used for verification.')
    args = parser.parse_args()

    message = get_message_from_signature(args.signature, args.public_key, args.modulus)

    if message:
        verification = signature_verify(message, args.signature, args.public_key, args.modulus)

        print(f'Verification: {verification}\n'
              f'Decrypted message: {message}')