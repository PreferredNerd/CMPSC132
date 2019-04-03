import unittest
from LAB4 import encrypt
from LAB4 import decrypt

class EncryptTestCase(unittest.TestCase):
    def test_for_perserving_case(self):
        """Does the Encryption system actually work? Even for Edge cases like Z and A?"""
        self.assertTrue(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz", 6), "GHIJKLMNOPQRSTUVWXYZABCDEF ghijklmnopqrstuvwxyzabcdef")
        self.assertTrue(
            encrypt("Oh no, Lawrence Lee found out I (may have) hard coded return statements into my first lab!", 2)
            , "Qj pq, Ncytgpeg Ngg hqwpf qwv K (oca jcxg) jctf eqfgf tgvwtp uvcvgogpvu kpvq oa hktuv ncd!")

    def test_for_charecter(self):
        '''test all the non alpha numeric keys'''
        self.assertTrue(encrypt("~`!@#$%^&*()_+-={}|[]\:\";'<,>.?/", 7), "~`!@#$%^&*()_+-={}|[]\:\";'<,>.?/")

    def test_for_number_preservation(self):
        self.assertTrue(decrypt("1234567890",19248239011325823402353245325285353453245325481), "1234567890")

    def test_for_negative_key(self):
        self.assertTrue(encrypt("This is futile",-1234),"error")
        self.assertTrue(decrypt("This is futile", -21408248120948129214790127490213749081234798102479801247981204), "error")

    def test_for_large_key(self):
        self.assertTrue(encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz", 257201659241390), "GHIJKLMNOPQRSTUVWXYZABCDEF ghijklmnopqrstuvwxyzabcdef")

    def test_for_decrypt_all(self):
        """Does the Encryption system actually work? Even for Edge cases like Z and A?"""
        self.assertTrue(decrypt("Aopz pz h zljyla tlzzhnlz", 7), "This is a secret messages")
        self.assertTrue(decrypt("TTTtttt UUUuuu ___***(K)%%%", 20), "ZZZzzzz AAAaaa ___***(Q)%%%")
        self.assertTrue(decrypt("Mxpprn", 9), "Doggie")
        self.assertTrue(
            decrypt("Qj pq, Ncytgpeg Ngg hqwpf qwv K (oca jcxg) jctf eqfgf tgvwtp uvcvgogpvu kpvq oa hktuv ncd!", 2)
            , "Oh no, Lawrence Lee found out I (may have) hard coded return statements into my first lab!")
        self.assertTrue(decrypt("GHIJKLMNOPQRSTUVWXYZABCDEF ghijklmnopqrstuvwxyzabcdef", 6),
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz")
if __name__ == '__main__':
    unittest.main()