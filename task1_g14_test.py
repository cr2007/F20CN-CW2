import pytest

from task1_g14 import is_prime

class TestPrimeNumber:
    value = 0

    def testPrimeNumber1(self):
        self.value = 7
        assert is_prime(self.value) == True

    def testPrimeNumber2(self):
        self.value = 11
        assert is_prime(self.value) == True

    def testPrimeNumber3(self):
        self.value = 467586793
        assert is_prime(self.value) == True

    def testPrimeNumber4(self):
        self.value = 53164652
        assert is_prime(self.value) == False

    def testPrimeNumber5(self):
        self.value = 8768755
        assert is_prime(self.value) == False
