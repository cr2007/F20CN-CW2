#!/usr/bin/env python3
"""F20CN CW2 Task 1
   Nov 2023

   @author: Chandrashekhar Ramaprasad - cr2007
"""

import random

######## Creating a Public Key ########

def create_random_sequence(sequence_length: int = 8) -> list:
    """Creates a random sequence of n bits, each being subseqently
    """

    # Create a random sequence of n bits
    random_sequence: list = [ random.randint(1,100) ]

    # Add random bits to the sequence until it reaches the desired length
    while len(random_sequence) < sequence_length:
        # The next element is the sum of the previous element and a random number between 1 and 100
        next_element:int = sum(random_sequence) + random.randint(1,100)

        # Add the next element to the sequence
        random_sequence.append(next_element)

    # Return the random sequence
    return random_sequence
