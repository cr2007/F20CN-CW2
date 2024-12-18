# pylint: disable=missing-module-docstring, missing-function-docstring, missing-class-docstring
# pylint: disable=line-too-long
import importlib
import pytest

task1_g14 = importlib.import_module("task1-g14")

class TestPrimeNumber:
    priv_key = task1_g14.PrivateKey()

    def test_prime_number1(self):
        value = 7
        assert self.priv_key.is_prime(value)

    def test_prime_number2(self):
        value = 11
        assert self.priv_key.is_prime(value)

    def test_prime_number3(self):
        value = 467586793
        assert self.priv_key.is_prime(value)

    def test_prime_number4(self):
        value = 53164652
        assert not self.priv_key.is_prime(value)

    def test_prime_number5(self):
        value = 8768755
        assert not self.priv_key.is_prime(value)

    def test_prime_number6(self):
        value = 2324521457
        assert self.priv_key.is_prime(value)

    def test_prime_number7(self):
        value = 2848637806241
        assert self.priv_key.is_prime(value)

class TestCreateRandomSequence:
    __priv_key = task1_g14.PrivateKey()

    def test_create_random_sequence1(self):
        sequence = self.__priv_key.create_random_sequence(5)
        assert len(sequence) == 5

        for i in range(1, len(sequence)):
            assert sequence[i] > sum(sequence[:i])

    def test_create_random_sequence2(self):
        sequence = self.__priv_key.create_random_sequence(15)
        assert len(sequence) == 15

        for i in range(1, len(sequence)):
            assert sequence[i] > sum(sequence[:i])

    def test_create_random_sequence3(self):
        sequence = self.__priv_key.create_random_sequence()
        assert len(sequence) == 8

        for i in range(1, len(sequence)):
            assert sequence[i] > sum(sequence[:i])

    def test_value_error1(self):
        with pytest.raises(ValueError):
            self.__priv_key.create_random_sequence(-1)

    def test_value_error2(self):
        with pytest.raises(ValueError):
            self.__priv_key.create_random_sequence(-1)

class TestEncryptionDecryption:

    def test_encryption_decryption1(self):
        priv_key = task1_g14.PrivateKey()
        private_key = priv_key.calculate_private_key()

        pub_key = task1_g14.PublicKey(private_key)
        public_key = pub_key.calculate_public_key()

        # 'Group 14' in binary
        plain_text = ['01000111', '01110010', '01101111', '01110101', '01110000', '00100000',
                      '00110001', '00110100']

        encrypt = task1_g14.Encryption(public_key, plain_text)
        cipher_text = encrypt.encryption()

        decrypt = task1_g14.Decryption(cipher_text, private_key)
        decrypted_text = decrypt.decryption()

        assert decrypted_text == 'Group 14'

    def test_encryption_decryption2(self):
        priv_key = task1_g14.PrivateKey()
        private_key = priv_key.calculate_private_key()

        pub_key = task1_g14.PublicKey(private_key)
        public_key = pub_key.calculate_public_key()

        # 'Group 14' in binary
        plain_text = ['01010100', '01101000', '01100101', '00100000', '01100010', '01110010',
                      '01101111', '01110111', '01101110', '00100000', '01100110', '01101111',
                      '01111000', '00100000', '01101010', '01110101', '01101101', '01110000',
                      '01110011', '00100000', '01101111', '01110110', '01100101', '01110010',
                      '00100000', '01110100', '01101000', '01100101', '00100000', '01101100',
                      '01100001', '01111010', '01111001', '00100000', '01100100', '01101111',
                      '01100111', '00101110']

        encrypt = task1_g14.Encryption(public_key, plain_text)
        cipher_text = encrypt.encryption()

        decrypt = task1_g14.Decryption(cipher_text, private_key)
        decrypted_text = decrypt.decryption()

        assert decrypted_text == 'The brown fox jumps over the lazy dog.'

    def test_encryption_decryption3(self):
        priv_key = task1_g14.PrivateKey()
        private_key = priv_key.calculate_private_key()

        pub_key = task1_g14.PublicKey(private_key)
        public_key = pub_key.calculate_public_key()

        # 'Group 14' in binary
        plain_text = ['01011001', '01101111', '01110101', '00100000', '01100011', '01100001',
                      '01101110', '01101110', '01101111', '01110100', '00100000', '01110111',
                      '01101111', '01110010', '01110010', '01111001', '00100000', '01100001',
                      '01100010', '01101111', '01110101', '01110100', '00100000', '01110101',
                      '01110000', '01110011', '01100101', '01110100', '01110100', '01101001',
                      '01101110', '01100111', '00100000', '01100101', '01110110', '01100101',
                      '01110010', '01111001', '00100000', '01110000', '01100101', '01110010',
                      '01110011', '01101111', '01101110', '00100000', '01111001', '01101111',
                      '01110101', '00100000', '01100011', '01101111', '01101101', '01100101',
                      '00100000', '01100001', '01100011', '01110010', '01101111', '01110011',
                      '01110011', '00101100', '00100000', '01100010', '01110101', '01110100',
                      '00100000', '01111001', '01101111', '01110101', '00100000', '01101101',
                      '01110101', '01110011', '01110100', '00100000', '01100010', '01100101',
                      '00100000', '01110011', '01100101', '01101100', '01100101', '01100011',
                      '01110100', '01101001', '01110110', '01100101', '01101100', '01111001',
                      '00100000', '01100011', '01110010', '01110101', '01100101', '01101100',
                      '00101110', '00100000', '01001001', '01100110', '00100000', '01111001',
                      '01101111', '01110101', '01110010', '00100000', '01110011', '01110101',
                      '01110000', '01100101', '01110010', '01101001', '01101111', '01110010',
                      '00100000', '01101001', '01110011', '00100000', '01100001', '00100000',
                      '01100110', '01100001', '01101100', '01101100', '01101001', '01101110',
                      '01100111', '00100000', '01110011', '01110100', '01100001', '01110010',
                      '00101100', '00100000', '01110100', '01101000', '01100101', '01110010',
                      '01100101', '00100000', '01101001', '01110011', '00100000', '01101110',
                      '01101111', '01110100', '01101000', '01101001', '01101110', '01100111',
                      '00100000', '01110100', '01101111', '00100000', '01100110', '01100101',
                      '01100001', '01110010', '00100000', '01100110', '01110010', '01101111',
                      '01101101', '00100000', '01101111', '01110101', '01110100', '01110011',
                      '01101000', '01101001', '01101110', '01101001', '01101110', '01100111',
                      '00100000', '01101000', '01101001', '01101101', '00101110', '00100000',
                      '01000100', '01101111', '00100000', '01101110', '01101111', '01110100',
                      '00100000', '01100010', '01100101', '00100000', '01101101', '01100101',
                      '01110010', '01100011', '01101001', '01100110', '01110101', '01101100',
                      '00101101', '00101101', '01111001', '01101111', '01110101', '01110010',
                      '00100000', '01101101', '01100001', '01110011', '01110100', '01100101',
                      '01110010', '00100000', '01101000', '01100001', '01100100', '00100000',
                      '01101110', '01101111', '00100000', '01110011', '01110101', '01100011',
                      '01101000', '00100000', '01110011', '01100011', '01110010', '01110101',
                      '01110000', '01101100', '01100101', '01110011', '00100000', '01101001',
                      '01101110', '00100000', '01101000', '01101001', '01110011', '00100000',
                      '01101111', '01110111', '01101110', '00100000', '01100011', '01101111',
                      '01101100', '01100100', '00101101', '01100010', '01101100', '01101111',
                      '01101111', '01100100', '01100101', '01100100', '00100000', '01100011',
                      '01101100', '01101001', '01101101', '01100010', '00100000', '01110100',
                      '01101111', '00100000', '01110100', '01101000', '01100101', '00100000',
                      '01110100', '01101111', '01110000', '00101110', '00100000', '01000111',
                      '01100001', '01110101', '01100111', '01100101', '00100000', '01101000',
                      '01101001', '01110011', '00100000', '01110011', '01110100', '01110010',
                      '01100101', '01101110', '01100111', '01110100', '01101000', '00101110',
                      '00100000', '01001001', '01100110', '00100000', '01101000', '01100101',
                      '00100000', '01101001', '01110011', '00100000', '01110111', '01100101',
                      '01100001', '01101011', '00101100', '00100000', '01100100', '01101001',
                      '01110011', '01100011', '01110010', '01100101', '01100101', '01110100',
                      '01101100', '01111001', '00100000', '01101000', '01100001', '01110011',
                      '01110100', '01100101', '01101110', '00100000', '01101000', '01101001',
                      '01110011', '00100000', '01100100', '01101111', '01110111', '01101110',
                      '01100110', '01100001', '01101100', '01101100', '00111010', '00100000',
                      '01001111', '01110101', '01110100', '01100100', '01101111', '00101100',
                      '00100000', '01101111', '01110101', '01110100', '01100011', '01101000',
                      '01100001', '01110010', '01101101', '00101100', '00100000', '01101111',
                      '01110101', '01110100', '01110011', '01101101', '01100001', '01110010',
                      '01110100', '00100000', '01101000', '01101001', '01101101', '00100000',
                      '01100001', '01110100', '00100000', '01101011', '01100101', '01111001',
                      '00100000', '01101101', '01101111', '01101101', '01100101', '01101110',
                      '01110100', '01110011', '00101110', '00100000', '01001001', '01100110',
                      '00100000', '01101000', '01100101', '00100000', '01101001', '01110011',
                      '00100000', '01110110', '01100101', '01110010', '01111001', '00100000',
                      '01110111', '01100101', '01100001', '01101011', '00100000', '01100001',
                      '01101110', '01100100', '00100000', '01110010', '01100101', '01100001',
                      '01100100', '01111001', '00100000', '01110100', '01101111', '00100000',
                      '01100110', '01100001', '01101100', '01101100', '00101100', '00100000',
                      '01101100', '01100101', '01110100', '00100000', '01101110', '01100001',
                      '01110100', '01110101', '01110010', '01100101', '00100000', '01110100',
                      '01100001', '01101011', '01100101', '00100000', '01101001', '01110100',
                      '01110011', '00100000', '01100011', '01101111', '01110101', '01110010',
                      '01110011', '01100101', '00101110', '00100000', '01000100', '01101111',
                      '00100000', '01101110', '01101111', '01110100', '00100000', '01110010',
                      '01101001', '01110011', '01101011', '00100000', '01101111', '01110101',
                      '01110100', '01110011', '01101000', '01101001', '01101110', '01101001',
                      '01101110', '01100111', '00100000', '01100001', '00100000', '01100110',
                      '01100101', '01100101', '01100010', '01101100', '01100101', '00100000',
                      '01110011', '01110101', '01110000', '01100101', '01110010', '01101001',
                      '01101111', '01110010', '00101101', '00101101', '01101001', '01110100',
                      '00100000', '01101101', '01101001', '01100111', '01101000', '01110100',
                      '00100000', '01100001', '01110000', '01110000', '01100101', '01100001',
                      '01110010', '00100000', '01100011', '01110010', '01110101', '01100101',
                      '01101100', '00100000', '01101111', '01110010', '00100000', '01110011',
                      '01110000', '01101001', '01110100', '01100101', '01100110', '01110101',
                      '01101100', '00101110', '00100000', '01000010', '01110101', '01110100',
                      '00100000', '01101001', '01100110', '00100000', '01111001', '01101111',
                      '01110101', '01110010', '00100000', '01101101', '01100001', '01110011',
                      '01110100', '01100101', '01110010', '00100000', '01101001', '01110011',
                      '00100000', '01100110', '01101001', '01110010', '01101101', '00100000',
                      '01101001', '01101110', '00100000', '01101000', '01101001', '01110011',
                      '00100000', '01110000', '01101111', '01110011', '01101001', '01110100',
                      '01101001', '01101111', '01101110', '00101100', '00100000', '01111001',
                      '01100101', '01110100', '00100000', '01111001', '01101111', '01110101',
                      '00100000', '01101011', '01101110', '01101111', '01110111', '00100000',
                      '01111001', '01101111', '01110101', '01110010', '01110011', '01100101',
                      '01101100', '01100110', '00100000', '01110100', '01101111', '00100000',
                      '01100010', '01100101', '00100000', '01110100', '01101000', '01100101',
                      '00100000', '01101101', '01101111', '01110010', '01100101', '00100000',
                      '01100011', '01100001', '01110000', '01100001', '01100010', '01101100',
                      '01100101', '00101100', '00100000', '01101000', '01101001', '01100100',
                      '01100101', '00100000', '01111001', '01101111', '01110101', '01110010',
                      '00100000', '01110100', '01101001', '01101101', '01100101', '00100000',
                      '01100001', '01101110', '01100100', '00100000', '01100010', '01100101',
                      '00100000', '01110000', '01100001', '01110100', '01101001', '01100101',
                      '01101110', '01110100', '00101110', '00100000', '01001001', '01110100',
                      '00100000', '01101001', '01110011', '00100000', '01110100', '01101000',
                      '01100101', '00100000', '01101110', '01100001', '01110100', '01110101',
                      '01110010', '01100001', '01101100', '00100000', '01100011', '01101111',
                      '01110101', '01110010', '01110011', '01100101', '00100000', '01101111',
                      '01100110', '00100000', '01110100', '01101000', '01101001', '01101110',
                      '01100111', '01110011', '00100000', '01110100', '01101000', '01100001',
                      '01110100', '00100000', '01110000', '01101111', '01110111', '01100101',
                      '01110010', '00100000', '01100101', '01110110', '01100101', '01101110',
                      '01110100', '01110101', '01100001', '01101100', '01101100', '01111001',
                      '00100000', '01100110', '01100001', '01100100', '01100101', '01110011',
                      '00100000', '01100001', '01101110', '01100100', '00100000', '01110111',
                      '01100101', '01100001', '01101011', '01100101', '01101110', '01110011',
                      '00101110', '00100000', '01011001', '01101111', '01110101', '01110010',
                      '00100000', '01101101', '01100001', '01110011', '01110100', '01100101',
                      '01110010', '00100000', '01110111', '01101001', '01101100', '01101100',
                      '00100000', '01100110', '01100001', '01101100', '01101100', '00100000',
                      '01110011', '01101111', '01101101', '01100101', '01100100', '01100001',
                      '01111001', '00101100', '00100000', '01100001', '01101110', '01100100',
                      '00100000', '01101001', '01100110', '00100000', '01111001', '01101111',
                      '01110101', '00100000', '01110000', '01101100', '01100001', '01111001',
                      '00100000', '01101001', '01110100', '00100000', '01110010', '01101001',
                      '01100111', '01101000', '01110100', '00101100', '00100000', '01111001',
                      '01101111', '01110101', '00100000', '01110111', '01101001', '01101100',
                      '01101100', '00100000', '01101111', '01110101', '01110100', '01101100',
                      '01101001', '01110110', '01100101', '00100000', '01100001', '01101110',
                      '01100100', '00100000', '01110011', '01101111', '01101101', '01100101',
                      '01100100', '01100001', '01111001', '00100000', '01101111', '01110101',
                      '01110100', '01110011', '01101000', '01101001', '01101110', '01100101',
                      '00100000', '01101000', '01101001', '01101101', '00101110']

        encrypt = task1_g14.Encryption(public_key, plain_text)
        cipher_text = encrypt.encryption()

        decrypt = task1_g14.Decryption(cipher_text, private_key)
        decrypted_text = decrypt.decryption()

        assert decrypted_text == 'You cannot worry about upsetting every person you come across, but you must be selectively cruel. If your superior is a falling star, there is nothing to fear from outshining him. Do not be merciful--your master had no such scruples in his own cold-blooded climb to the top. Gauge his strength. If he is weak, discreetly hasten his downfall: Outdo, outcharm, outsmart him at key moments. If he is very weak and ready to fall, let nature take its course. Do not risk outshining a feeble superior--it might appear cruel or spiteful. But if your master is firm in his position, yet you know yourself to be the more capable, hide your time and be patient. It is the natural course of things that power eventually fades and weakens. Your master will fall someday, and if you play it right, you will outlive and someday outshine him.'

    def test_encryption_decryption4(self):
        priv_key = task1_g14.PrivateKey()
        private_key = priv_key.calculate_private_key()

        pub_key = task1_g14.PublicKey(private_key)
        public_key = pub_key.calculate_public_key()

        # 'Group 14' in binary
        plain_text = ['01000100', '01101111', '00100000', '01101110', '01101111',
                      '01110100', '00100000', '01100010', '01100101', '00100000',
                      '01101111', '01101110', '01100101', '00100000', '01101111',
                      '01100110', '00100000', '01110100', '01101000', '01100101',
                      '00100000', '01101101', '01100001', '01101110', '01111001',
                      '00100000', '01110111', '01101000', '01101111', '00100000',
                      '01101101', '01101001', '01110011', '01110100', '01100001',
                      '01101011', '01100101', '01101110', '01101100', '01111001',
                      '00100000', '01100010', '01100101', '01101100', '01101001',
                      '01100101', '01110110', '01100101', '00100000', '01110100',
                      '01101000', '01100001', '01110100', '00100000', '01110100',
                      '01101000', '01100101', '00100000', '01110101', '01101100',
                      '01110100', '01101001', '01101101', '01100001', '01110100',
                      '01100101', '00100000', '01100110', '01101111', '01110010',
                      '01101101', '00100000', '01101111', '01100110', '00100000',
                      '01110000', '01101111', '01110111', '01100101', '01110010',
                      '00100000', '01101001', '01110011', '00100000', '01101001',
                      '01101110', '01100100', '01100101', '01110000', '01100101',
                      '01101110', '01100100', '01100101', '01101110', '01100011',
                      '01100101', '00101110', '00100000', '01010000', '01101111',
                      '01110111', '01100101', '01110010', '00100000', '01101001',
                      '01101110', '01110110', '01101111', '01101100', '01110110',
                      '01100101', '01110011', '00100000', '01100001', '00100000',
                      '01110010', '01100101', '01101100', '01100001', '01110100',
                      '01101001', '01101111', '01101110', '01110011', '01101000',
                      '01101001', '01110000', '00100000', '01100010', '01100101',
                      '01110100', '01110111', '01100101', '01100101', '01101110',
                      '00100000', '01110000', '01100101', '01101111', '01110000',
                      '01101100', '01100101', '00111011', '00100000', '01111001',
                      '01101111', '01110101', '00100000', '01110111', '01101001',
                      '01101100', '01101100', '00100000', '01100001', '01101100',
                      '01110111', '01100001', '01111001', '01110011', '00100000',
                      '01101110', '01100101', '01100101', '01100100', '00100000',
                      '01101111', '01110100', '01101000', '01100101', '01110010',
                      '01110011', '00100000', '01100001', '01110011', '00100000',
                      '01100001', '01101100', '01101100', '01101001', '01100101',
                      '01110011', '00101100', '00100000', '01110000', '01100001',
                      '01110111', '01101110', '01110011', '00101100', '00100000',
                      '01101111', '01110010', '00100000', '01100101', '01110110',
                      '01100101', '01101110', '00100000', '01100001', '01110011',
                      '00100000', '01110111', '01100101', '01100001', '01101011',
                      '00100000', '01101101', '01100001', '01110011', '01110100',
                      '01100101', '01110010', '01110011', '00100000', '01110111',
                      '01101000', '01101111', '00100000', '01110011', '01100101',
                      '01110010', '01110110', '01100101', '00100000', '01100001',
                      '01110011', '00100000', '01111001', '01101111', '01110101',
                      '01110010', '00100000', '01100110', '01110010', '01101111',
                      '01101110', '01110100', '00101110', '00100000', '01010100',
                      '01101000', '01100101', '00100000', '01100011', '01101111',
                      '01101101', '01110000', '01101100', '01100101', '01110100',
                      '01100101', '01101100', '01111001', '00100000', '01101001',
                      '01101110', '01100100', '01100101', '01110000', '01100101',
                      '01101110', '01100100', '01100101', '01101110', '01110100',
                      '00100000', '01101101', '01100001', '01101110', '00100000',
                      '01110111', '01101111', '01110101', '01101100', '01100100',
                      '00100000', '01101100', '01101001', '01110110', '01100101',
                      '00100000', '01101001', '01101110', '00100000', '01100001',
                      '00100000', '01100011', '01100001', '01100010', '01101001',
                      '01101110', '00100000', '01101001', '01101110', '00100000',
                      '01110100', '01101000', '01100101', '00100000', '01110111',
                      '01101111', '01101111', '01100100', '01110011', '00101101',
                      '00101101', '01101000', '01100101', '00100000', '01110111',
                      '01101111', '01110101', '01101100', '01100100', '00100000',
                      '01101000', '01100001', '01110110', '01100101', '00100000',
                      '01110100', '01101000', '01100101', '00100000', '01100110',
                      '01110010', '01100101', '01100101', '01100100', '01101111',
                      '01101101', '00100000', '01110100', '01101111', '00100000',
                      '01100011', '01101111', '01101101', '01100101', '00100000',
                      '01100001', '01101110', '01100100', '00100000', '01100111',
                      '01101111', '00100000', '01100001', '01110011', '00100000',
                      '01101000', '01100101', '00100000', '01110000', '01101100',
                      '01100101', '01100001', '01110011', '01100101', '01100100',
                      '00101100', '00100000', '01100010', '01110101', '01110100',
                      '00100000', '01101000', '01100101', '00100000', '01110111',
                      '01101111', '01110101', '01101100', '01100100', '00100000',
                      '01101000', '01100001', '01110110', '01100101', '00100000',
                      '01101110', '01101111', '00100000', '01110000', '01101111',
                      '01110111', '01100101', '01110010', '00101110', '00100000',
                      '01010100', '01101000', '01100101', '00100000', '01100010',
                      '01100101', '01110011', '01110100', '00100000', '01111001',
                      '01101111', '01110101', '00100000', '01100011', '01100001',
                      '01101110', '00100000', '01101000', '01101111', '01110000',
                      '01100101', '00100000', '01100110', '01101111', '01110010',
                      '00100000', '01101001', '01110011', '00100000', '01110100',
                      '01101000', '01100001', '01110100', '00100000', '01101111',
                      '01110100', '01101000', '01100101', '01110010', '01110011',
                      '00100000', '01110111', '01101001', '01101100', '01101100',
                      '00100000', '01100111', '01110010', '01101111', '01110111',
                      '00100000', '01110011', '01101111', '00100000', '01100100',
                      '01100101', '01110000', '01100101', '01101110', '01100100',
                      '01100101', '01101110', '01110100', '00100000', '01101111',
                      '01101110', '00100000', '01111001', '01101111', '01110101',
                      '00100000', '01110100', '01101000', '01100001', '01110100',
                      '00100000', '01111001', '01101111', '01110101', '00100000',
                      '01100101', '01101110', '01101010', '01101111', '01111001',
                      '00100000', '01100001', '00100000', '01101011', '01101001',
                      '01101110', '01100100', '00100000', '01101111', '01100110',
                      '00100000', '01110010', '01100101', '01110110', '01100101',
                      '01110010', '01110011', '01100101', '00100000', '01101001',
                      '01101110', '01100100', '01100101', '01110000', '01100101',
                      '01101110', '01100100', '01100101', '01101110', '01100011',
                      '01100101', '00111010', '00100000', '01010100', '01101000',
                      '01100101', '01101001', '01110010', '00100000', '01101110',
                      '01100101', '01100101', '01100100', '00100000', '01100110',
                      '01101111', '01110010', '00100000', '01111001', '01101111',
                      '01110101', '00100000', '01100110', '01110010', '01100101',
                      '01100101', '01110011', '00100000', '01111001', '01101111',
                      '01110101', '00101110']

        encrypt = task1_g14.Encryption(public_key, plain_text)
        cipher_text = encrypt.encryption()

        decrypt = task1_g14.Decryption(cipher_text, private_key)
        decrypted_text = decrypt.decryption()

        assert decrypted_text == 'Do not be one of the many who mistakenly believe that the ultimate form of power is independence. Power involves a relationship between people; you will always need others as allies, pawns, or even as weak masters who serve as your front. The completely independent man would live in a cabin in the woods--he would have the freedom to come and go as he pleased, but he would have no power. The best you can hope for is that others will grow so dependent on you that you enjoy a kind of reverse independence: Their need for you frees you.'
