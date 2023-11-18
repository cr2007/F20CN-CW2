import pytest

from task1_g14 import PrivateKey, PublicKey, Encryption, Decryption

class TestPrimeNumber:
    priv_key = PrivateKey()

    def testPrimeNumber1(self):
        value = 7
        assert self.priv_key.is_prime(value)

    def testPrimeNumber2(self):
        value = 11
        assert self.priv_key.is_prime(value)

    def testPrimeNumber3(self):
        value = 467586793
        assert self.priv_key.is_prime(value)

    def testPrimeNumber4(self):
        value = 53164652
        assert not self.priv_key.is_prime(value)

    def testPrimeNumber5(self):
        value = 8768755
        assert not self.priv_key.is_prime(value)

    def testPrimeNumber6(self):
        value = 2324521457
        assert self.priv_key.is_prime(value)

    def testPrimeNumber7(self):
        value = 2848637806241
        assert self.priv_key.is_prime(value)
