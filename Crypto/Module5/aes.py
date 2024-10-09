from Crypto.Cipher import AES

def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

# AES CBC encryption
def aes_cbc_encrypt(key, iv, plaintext):
    # Make sure plaintext is padded to a multiple of 16 bytes (AES block size)
    if len(plaintext) % 16 != 0:
        plaintext += b'\x00' * (16 - len(plaintext) % 16)

    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = b''
    prev_cipher_block = iv  # initial IV

    # Process the plaintext block by block
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i + 16]  # Get the next 16-byte block from plaintext
        block = xor_bytes(block, prev_cipher_block)  # XOR with the previous ciphertext block (or IV)
        encrypted_block = cipher.encrypt(block)  # Encrypt the XOR result
        ciphertext += encrypted_block  # Append to the ciphertext result
        prev_cipher_block = encrypted_block  # Update the previous block for the next iteration
    return ciphertext

# Checker function
def validate_aes_cbc_encrypt(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    if len(plaintext) % 16 != 0:
        plaintext += b'\x00' * (16 - len(plaintext) % 16)
    return cipher.encrypt(plaintext)
