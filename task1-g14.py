#!/usr/bin/env python3
"""
This script is part of the F20CN CW2 Task 1. It includes a function to create a random sequence of
integers, where each subsequent integer is the sum of all previous integers in the sequence plus a
new random integer.
This sequence can be used as a public key in cryptographic operations.

@author: CHANDRASHEKHAR RAMAPRASAD (cr2007)
@date: November 11, 2023
"""

# Importing required libraries
import random
import math

######## Creating a Public Key ########

def create_random_sequence(sequence_length: int = 8) -> list:
    """
    Creates a random sequence of integers where each subsequent integer is the sum of all previous
    integers in the sequence plus a new random integer.

    Parameters:
    sequence_length (int): The length of the sequence to be generated. Default is 8.

    Returns:
    list: The generated sequence of integers.
    """
    # Initialize the sequence with a random integer between 1 and 100
    random_sequence: list = [ random.randint(1,100) ]

    # Generate the rest of the sequence
    while len(random_sequence) < sequence_length:
        # The next element is the sum of all previous elements plus a new random integer
        next_element:int = sum(random_sequence) + random.randint(1,100)

        # Add the next element to the sequence
        random_sequence.append(next_element)

    # Return the random sequence
    return random_sequence

# Source: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def is_prime(number: int) -> bool:
    """
    Checks if a number is prime or not.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """

    if number % 2 == 0:
        return False

    # Check divisibility for all numbers up to the square root of the input number
    for i in range(3, int(math.sqrt(number))+1, 2):
        # If the number is divisible by any number in the range, it's not prime
        if number % i == 0:
            return False

    # If no divisors found, the number is prime
    return True

def calculate_public_key(e_list: list, q_int: int, w_int: int) -> list:
    """
    Calculates the public key from the given parameters.

    Parameters:
    - e (list): The random sequence of integers.
    - q (int): The random prime number.
    - w (int): The random integer.

    Returns:
    - list: The public key.
    """
    # Calculate the public key
    h: list = [ (w_int * i) % q_int for i in e_list ]

    # Return the public key
    return h

def encryption(plain_text_list: list, public_key_list: list) -> list:
    """
    This function encrypts a list of plain text values using a public key.

    Args:
        plain_text_list (list): The plain text values to be encrypted.
        public_key_list (list): The public key used for encryption.

    Returns:
        list: The encrypted text.
    """
    # Initialize an empty list to hold the encrypted text
    encrypted_text: list = []

    # Loop through every value in the plain text
    for value in plain_text_list:
        # Initialize a variable to hold the sum of the cipher text
        cipher_text_sum: int = 0

        # Loop through every bit in the value
        for i, bit in enumerate(value):
            # If the bit is '1', multiply it with the corresponding value in the public key
            cipher_text_sum += (int(bit) * public_key_list[i]) if bit == '1' else 0

        # Append the sum of the cipher text to the encrypted text list
        encrypted_text.append(cipher_text_sum)

    # Return the encrypted text
    return encrypted_text

def decryption(ciphertext: list, private_key_dict: dict) -> str:
    """
    This function decrypts a given ciphertext using a private key dictionary.

    Parameters:
    ciphertext (list): The ciphertext to be decrypted.
    private_key_dict (dict): The private key dictionary containing 'e', 'q', and 'w' keys.

    Returns:
    str: The decrypted plaintext.
    """

    # Extracting the values from the private key dictionary
    e_list: list = private_key_dict["e"]
    q_int: int   = private_key_dict["q"]
    w_int: int   = private_key_dict["w"]

    # Calculating the multiplicative inverse of w modulo q
    w_inv: int = pow(w_int, -1, q_int)

    # Initializing an empty string to hold the plain text bits
    plain_text_bits: str = ""

    # Looping through every value in the cipher text
    for c in ciphertext:
        # Calculating c' which is the product of c and w_inv modulo q
        c_prime: int = (c * w_inv) % q_int

        # Initializing an empty string to hold the bits
        bits: str = ""

        # Looping through every value in the random sequence in reverse order
        for e_n in reversed(e_list):
            # If c' is greater than or equal to the value in the random sequence
            if c_prime >= e_n:
                bits = '1' + bits # append '1' to the bits
                c_prime -= e_n    # subtract the value from c'
            else:
                bits = '0' + bits # append '0' to the bits

        # Appending the bits to the plain text bits
        plain_text_bits += bits

    # Converting the binary string to text
    plain_text_str: str = ''.join(chr(int(plain_text_bits[i:i+8], 2))
                              for i in range(0, len(plain_text_bits), 8))

    # Returning the plain text
    return plain_text_str


# Main function
if __name__ == "__main__":

    # Get the input text from the user
    input_text: str = ""
    while True:
        line = input("Enter a line of plain text (press Enter for a new line, or just press Enter to finish): ")
        if line == "":
            break
        input_text += line + " "

    # Remove trailing whitespace and '\n' characters
    input_text = input_text.rstrip()

    # Convert the input text to binary
    input_binary: str = ''.join(format(ord(i), '08b') for i in input_text)

    # Split it into a list of 8-bit chunks
    plain_text: list = [ input_binary[i:i+8] for i in range(0,len(input_binary),8) ]

    # Create a random sequence of integers
    e: list = create_random_sequence()

    # Choose a random prime number
    q: int = (2 * e[-1]) + random.randint(1,1000)
    while not is_prime(q): # check if q is prime
        # if not, choose another random prime number
        q = (2 * e[-1]) + random.randint(1,1000)

    w: int = random.randint(1,q+250) # choose a random integer w between 1 and q-1
    while math.gcd(w,q) != 1:
        # if w and q are not coprime, choose another random integer w
        w = random.randint(1,q-1)

    # Calculate the public key (h)
    public_key: list = calculate_public_key(e,q,w)

    # Dictionary to store private key: (e,q,w)
    private_key: dict = { "e": e, "q": q, "w": w }

    # Encrypt the plain text
    cipher_text: list = encryption(plain_text, public_key)

    print(f"Cipher Text: {sum(cipher_text)}")

    # Decrypt the cipher text
    decrypted_text: str = decryption(cipher_text, private_key)
    print(f"Decrypted Text: {decrypted_text}")
