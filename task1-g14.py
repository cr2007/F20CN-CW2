#!/usr/bin/env python3
"""F20CN CW2 Task 1
   Nov 2023

   @author: Chandrashekhar Ramaprasad - cr2007
"""

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

def is_prime(number: int) -> bool:
    """
    Checks if a number is prime or not.

    Parameters:
    number (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # 1 and 2 are not considered prime numbers in this implementation
    if number in [1,2]:
        return False

    # Check divisibility for all numbers up to the square root of the input number
    for i in range(2, int(math.sqrt(number))+1):
        # If the number is divisible by any number in the range, it's not prime
        if number % i == 0:
            return False

    # If no divisors found, the number is prime
    return True


if __name__ == "__main__":
    # Create a random sequence of integers
    e: list = create_random_sequence()

    # Choose a random prime number
    q: int = 2 * e[-1] + random.randint(1,random.randint(100,1000) )
    while not is_prime(q): # check if q is prime
        # if not, choose another random prime number
        q = 2 * e[-1] + random.randint(1,random.randint(100,1000) )

    print(f"Random sequence 'e': {e}")
    print(f"q: {q}")
