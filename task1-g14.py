#!/usr/bin/env python3

"""
F20CN CW2 Task 1 - Alternative Method of Public-Key Encryption

This module implements an alternative method of public-key encryption. It includes classes for
generating private and public keys, encryption, and decryption.

Classes:
    - PublicKey: Represents the public key and provides methods to calculate it based on a given
                 private key.
    - PrivateKey: Represents the private key and provides methods to calculate it with a random
                  sequence, a random prime number, and a random integer.
    - Encryption: Handles the encryption process using a public key.
    - Decryption: Manages the decryption process using a private key.

Raises:
    - ValueError: If there are issues with the provided private key or during the
                  encryption/decryption process.

Returns:
    The module does not have a direct return. It includes classes that facilitate public-key
    encryption.

Author:
    - Chandrashekhar Ramaprasad
    - Oluwadolabomi Faith Muraino
"""

# Importing required libraries
import random
import math

class PublicKey:
    def __init__(self, private_key_dict: dict):
        """
        Initializes the PublicKey object with the private key dictionary.

        Parameters:
        - `private_key_dict` (dict): The private key dictionary containing 'e', 'q', and 'w' keys.
        """
        self.e: list = private_key_dict["e"]
        self.q: int  = private_key_dict["q"]
        self.w: int  = private_key_dict["w"]

    def calculate_public_key(self) -> list[int]:
        """
        Calculates the public key based on the provided private key.

        ### Returns:
        - list: The public key calculated as `(w * i) mod q` for each integer `i` in the random
        sequence.

        ### Raises:
        - ValueError: If the random sequence (`e`) is empty or if `q` or `w` are not greater than 0.
        """

        # Check if the random sequence is empty
        if not self.e:
            raise ValueError("Random sequence cannot be empty.")

        # Check if q and w are greater than 0
        if self.q <= 0 or self.w <= 0:
            raise ValueError("q and w must be greater than 0.")

        # Calculates and returns the public key
        return [ (self.w * i) % self.q for i in self.e ]

class PrivateKey:
    def __init__(self):
        """
        Initializes the PrivateKey object.
        """
        self.e: list[int] = []
        self.q: int = 0
        self.w: int = 0
        self.private_key: dict = {}

    def calculate_private_key(self) -> dict:
        """
        Calculates the private key, which includes a random sequence, a random prime number, and a
        random integer.

        Returns:
        - dict: The private key dictionary containing 'e', 'q', and 'w' keys.
        """

        # Create a random sequence of integers
        self.e = self.create_random_sequence()

        # Choose a random prime number that is greater than twice the last number in the sequence
        self.q = (2 * self.e[-1]) + random.randint(1, 1000)
        # If the chosen number is not prime, choose another one
        while not self.is_prime(self.q):
            self.q = (2 * self.e[-1]) + random.randint(1, 1000)

        # Choose a random integer w that is less than q
        self.w = random.randint(1, self.q+250)
        # If w and q are not coprime, choose another w
        while math.gcd(self.w, self.q) != 1:
            self.w = random.randint(1, self.q-1)

        # Store the private key components in a dictionary
        self.private_key = { "e": self.e, "q": self.q, "w": self.w }

        # Return the private key
        return self.private_key

    def create_random_sequence(self, sequence_length: int = 8) -> list[int]:
        """
        Creates a random sequence of integers.

        ### Parameters:
        - `sequence_length` (int): The length of the sequence to be generated. Default is 8.

        ### Returns:
        - list: The generated sequence of integers.

        ### Raises:
        - ValueError: If `sequence_length` is less than or equal to 0.
        """

        if sequence_length <= 0:
            raise ValueError("Sequence length must be greater than 0.")

        # Initialize the sequence with a random integer between 1 and 100
        random_sequence: list[int] = [ random.randint(1,100) ]

        # Generate the rest of the sequence
        while len(random_sequence) < sequence_length:
            # The next element is the sum of all previous elements plus a new random integer
            next_element:int = sum(random_sequence) + random.randint(1, 100)

            # Add the next element to the sequence
            random_sequence.append(next_element)

        # Return the random sequence
        return random_sequence

    # Source: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not
    def is_prime(self, number: int) -> bool:
        """
        Checks if a number is prime or not.

        ### Parameters:
        - `number` (int): The number to be checked. Must be greater than 1.

        ### Returns:
        - bool: True if the number is prime, False otherwise.

        ### Raises:
        - ValueError: If the input number is less than or equal to 1.
        """

        if number <= 1:
            raise ValueError("Number must be greater than 1.")

        if number % 2 == 0:
            return False

        # Check divisibility for all numbers up to the square root of the input number
        for i in range(3, int(math.sqrt(number))+1, 2):
            # If the number is divisible by any number in the range, it's not prime
            if number % i == 0:
                return False

        # If no divisors found, the number is prime
        return True

class Encryption:
    def __init__(self, public_key_list: list[int], plain_text_list: list[str]) -> None:
        """
        Initializes the Encryption object.

        ### Parameters:
        - `public_key_list` (list): The public key used for encryption. Each key should be an integer.
        - `plain_text_list` (list): The plain text values to be encrypted. Each value should be a string
        of binary digits.
        """
        self.public_key: list[int] = public_key_list
        self.plain_text: list[str] = plain_text_list
        self.cipher_text: list[int] = []

    def encryption(self) -> list[int]:
        """
        Encrypts a list of binary plain text values using a public key.

        ### Returns:
        - list: The encrypted text, represented as a list of integers.

        ### Raises:
        - ValueError: If the plain text list or the public key list is empty.
        """

        if not self.plain_text:
            raise ValueError("Plain Text cannot be empty.")
        elif not self.public_key:
            raise ValueError("Public Key List cannot be empty.")

        # Initialize an empty list to hold the encrypted text
        encrypted_text: list[int] = []

        # Loop through every value in the plain text
        for value in self.plain_text:
            # Initialize a variable to hold the sum of the cipher text
            cipher_text_sum: int = 0

            # Loop through every bit in the value
            for i, bit in enumerate(value):
                # If the bit is '1', multiply it with the corresponding value in the public key
                cipher_text_sum += (int(bit) * self.public_key[i]) if bit == '1' else 0

            # Append the sum of the cipher text to the encrypted text list
            encrypted_text.append(cipher_text_sum)

        # Return the encrypted text
        return encrypted_text

class Decryption:
    def __init__(self, cipher_text_list: list[int], private_key_dict: dict):
        """
        Initializes the Decryption object.

        ### Parameters:
        - `cipher_text_list` (list): The ciphertext to be decrypted. Each value should be an integer.
        - `private_key_dict` (dict): The private key dictionary containing 'e', 'q', and 'w' keys
        """
        self.cipher_text: list[int] = cipher_text_list
        self.private_key: dict = private_key_dict
        self.e: list[int] = private_key_dict["e"]
        self.q: int = private_key_dict["q"]
        self.w: int = private_key_dict["w"]
        self.decrypted_text: str = ""

    def decryption(self) -> str:
        """
        Decrypts a given ciphertext using a private key dictionary.

        ### Returns:
        - str: The decrypted plaintext.

        ### Raises:
        - ValueError: If the ciphertext is empty or if the private key dictionary does not contain
        the keys 'e', 'q', and 'w'.
        """

        # Check if the ciphertext list is empty
        if not self.cipher_text:
            # If it is, raise a ValueError with a suitable message
            raise ValueError("Ciphertext cannot be empty")

        # Check if the private_key_dict contains all the necessary keys: 'e', 'q', and 'w'
        if not all(key in self.private_key for key in ("e", "q", "w")):
            # If it doesn't, raise a ValueError with a suitable message
            raise ValueError("private_key_dict must contain the keys 'e', 'q', and 'w'")

        # Calculating the multiplicative inverse of w modulo q
        w_inv: int = pow(self.w, -1, self.q)

        # Initializing an empty string to hold the plain text bits
        plain_text_bits: str = ""

        # Looping through every value in the cipher text
        for c in self.cipher_text:
            # Calculating c' which is the product of c and w_inv modulo q
            c_prime: int = (c * w_inv) % self.q

            # Initializing an empty string to hold the bits
            bits: str = ""

            # Looping through every value in the random sequence in reverse order
            for e_n in reversed(self.e):
                # If c' is greater than or equal to the value in the random sequence
                if c_prime >= e_n:
                    bits = '1' + bits  # append '1' to the bits
                    c_prime -= e_n     # subtract the value from c'
                else:
                    bits = '0' + bits # append '0' to the bits

            # Appending the bits to the plain text bits
            plain_text_bits += bits

        # Converting the binary string to text
        self.decrypted_text: str = ''.join(chr(int(plain_text_bits[i:i+8], 2))
                                for i in range(0, len(plain_text_bits), 8))

        # Returning the plain text
        return self.decrypted_text


# Main function
if __name__ == "__main__":

    try:

        # Initialize an empty string to store the user's input
        input_text: str = ""

        # Start an infinite loop to continuously get input from the user
        while True:
            # Prompt the user to enter a line of plain text
            # The user can press Enter for a new line, or just press Enter to finish
            line = input("Enter a line of plain text "
                         "(press Enter for a new line, or just press Enter to finish): ")

            # If the user just presses Enter (i.e., the input line is empty), break the loop
            if line == "":
                break

            # Add the input line to the input_text string, followed by a space
            input_text += line + " "

        # Remove trailing whitespace and '\n' characters
        input_text = input_text.rstrip()

        # Convert the input text to binary
        input_binary: str = ''.join(format(ord(i), '08b') for i in input_text)

        # Split it into a list of 8-bit chunks
        plain_text: list = [ input_binary[i:i+8] for i in range(0,len(input_binary),8) ]

        # Create a PrivateKey object
        priv_key = PrivateKey()
        # Dictionary to store private key: (e,q,w)
        private_key: dict = priv_key.calculate_private_key()

        # Create a PublicKey object with the private key
        pub_key = PublicKey(private_key)
        # Calculate the public key (h)
        public_key: list = pub_key.calculate_public_key()

        # Create an Encryption object with the public key and plain text
        encrypt = Encryption(public_key, plain_text)
        # Encrypt the plain text and store the cipher text in a list
        cipher_text: list = encrypt.encryption()

        # Print the cipher text
        print(f"Cipher Text: {sum(cipher_text)}")

        # Create a Decryption object with the cipher text and private key
        decrypt = Decryption(cipher_text, private_key)
        # Decrypt the cipher text and store the decrypted text in a string
        decrypted_text: str = decrypt.decryption()

        # Print the decrypted text
        print(f"Decrypted Text: {decrypted_text}")
    except ValueError as ve:
        print(f"ValueError occurred: {ve}") # Print the error message if a ValueError occurs
    except TypeError as te:
        print(f"TypeError occurred: {te}") # Print the error message if a ValueError occurs
    finally:
        print("Exiting...") # Print a message when the program is exiting
