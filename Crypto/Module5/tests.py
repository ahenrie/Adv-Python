import unittest

class testEncryption(unittest.TestCase):
    def setUp(self) -> None:
        self.key1 = b'0123456789abcdef'
        self.iv1 = b'abcdef9876543210'
        self.plantext1 = b'What the ef am I doing?'
        self.plantext2 = b'Test with different length'
        self.key2 = b'fedcba9876543210'
        self.iv2 = b'0123456789abcdef'

    def test_encryption(self):
        self.assertEqual(
            encrypt.aes_cbc_encrypt(self.key1, self.iv1, self.plantext1),
            encrypt.validate_aes_cbc_encrypt(self.key1, self.iv1, self.plantext1)
        )

    def test_encryption_with_different_key_and_iv(self):
        self.assertEqual(
            encrypt.aes_cbc_encrypt(self.key2, self.iv2, self.plantext1),
            encrypt.validate_aes_cbc_encrypt(self.key2, self.iv2, self.plantext1)
        )

    def test_encryption_with_different_plaintext(self):
        self.assertEqual(
            encrypt.aes_cbc_encrypt(self.key1, self.iv1, self.plantext2),
            encrypt.validate_aes_cbc_encrypt(self.key1, self.iv1, self.plantext2)
        )

    def test_encryption_with_swapped_key_and_iv(self):
        self.assertEqual(
            encrypt.aes_cbc_encrypt(self.iv1, self.key1, self.plantext1),
            encrypt.validate_aes_cbc_encrypt(self.iv1, self.key1, self.plantext1)
        )

if __name__ == '__main__':
    unittest.main()
