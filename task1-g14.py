#!/usr/bin/env python3
"""F20CN CW2 Task 1
   Nov 2023

   @author: Chandrashekhar Ramaprasad - cr2007
"""

import random

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

if __name__ == "__main__":
    # Create a random sequence of integers
    e: list = create_random_sequence()
