from aes import *

def main():
    key = b'0123456789abcdef'
    iv = b'abcdef9876543210'
    plaintext = b'Hello World!'

    my_ciphertext = aes_cbc_encrypt(key, iv, plaintext)

    validation_ciphertext = validate_aes_cbc_encrypt(key, iv, plaintext)

    print(my_ciphertext == validation_ciphertext)

if __name__ == "__main__":
    main()
