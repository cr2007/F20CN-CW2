#import "lib.typ": template

#set document(author: "Chandrashekhar R", title: "F20CN Coursework 2")

#show: template.with()

#image("images/HWU-Logo.png", height: 2.7cm)

#text(
  size: 28pt,
  font: "Segoe UI Variable",
  weight: "extrabold",
  "F20CN Coursework 2"
)

#text(size: 11pt, weight: "bold", [
  Course: #link("https://curriculum.hw.ac.uk/coursedetails/F20CN?termcode=202324")[
    #text(rgb("#0563C1"))[Computer Network Security]
  ]
])

// #v(0.5em)
*Group 14*
#v(0.5em)
*Team Members*:\
*Chandrashekhar Ramaprasad (cr2007)*\
*Oluwadolabomi Faith Muraino (fm2020)*

\

#set align(left)

#outline(indent: 1em)

#pagebreak()

#heading("Task 1: Alternative Method of Public-Key Encryption")
#heading("Pseudo-Code", level: 2)

#grid(
  columns: 2,
  gutter: 0.5cm,
  align: center,
  figure(caption: "Main Method Pseudo-code", image("./images/Task1/Task1-MainMethod-PseudoCode.png", height: 6.26cm)),
  figure(
    caption: "Private Key Class Pseudo-code",
    image("./images/Task1/Task1-PrivateKeyClass-PseudoCode.png", height: 5.31cm),
  ),
  figure(
    caption: "Public Key Class Pseudo-code",
    image("./images/Task1/Task1-PublicKeyClass-PseudoCode.png", height: 4.36cm),
  ),
  figure(
    caption: "Encryption Class Pseudo-code",
    image("./images/Task1/Task1-EncryptionClass-PseudoCode.png", height: 4.41cm),
  ),
  figure(
    caption: "Decryption Class Pseudo-code",
    image("./images/Task1/Task1-DecryptionClass-PseudoCode.png", height: 5.91cm),
  ),
)
\
The program was written via an object-oriented approach, to ensure code modularity and reusability.
The program has four key classes: `PrivateKey`, `PublicKey`, `Encryption`, and `Decryption`.
The main function facilitates user interaction with input of plain text, converting that text into binary, encryption, and subsequent decryption.
Error handling is also incorporated, raising `ValueError` and `TypeError` where appropriate.

#pagebreak()

#heading(level: 2, "Testing")\

#figure(
  caption: "Code Testing on Two Plaintexts",
  image("./images/Task1/Task1-Testing-Screenshot.png", alt: "Screenshot of Task 1 Code Testing"),
)

The testing results print out the sum of the #underline("ciphertext") (a list), and then prints out the #underline("decrypted text"), resulting from decrypting the ciphertext using the Private Key.
As displayed, each specific result will vary with each run due to the random generation of keys and sequences in the cryptographic process.

\

#line(length: 100%)
#pagebreak()

#heading("Task 2: Firewall Rules Application")

Firewalls are security devices that filter incoming and outgoing traffic within a network.
It analyses which traffic should be allowed or restricted based on a set of rules to spot and prevent cyberattacks.
The program has 2 classes: `Firewall`, and `FirewallRules`.
`Firewall` initializes the command while `FirewallRules` sets the command.
The `main` function facilitates user interaction with input of commands.

#heading(level: 2, "Pseudo-code")

#figure(caption: "Task 2 Pseudo-code", image("./images/Task2/Task2-PseudoCode.png", alt: "Pseudo-code of Task 2"))

#pagebreak()

#heading(level: 2, "Testing")

Over here we have three rules: `add`, `remove`, and `list`.

#heading(level: 3, "Adding Rule:")

The `add` rule adds a new rule. It has three values: rule, direction, and IP address.
The rule is a positive number starting from 1, and the lower the number, the higher the priority.
If a rule being added already exists, the rule being added is placed above the existing rule.
If no rule is provided, the rule automatically becomes 1.
The direction is `-in` or `-out`. Where `-in` is the incoming and `-out` is the outgoing traffic direction.
If no direction is given to a rule, then it automatically applies to both directions.
The address is the IPv4 address in dotted decimal.

#figure(caption: "Task 2 Test on adding a new rule", image(
  "./images/Task2/Task2-Testing-AddRule.png",
  alt: "Screenshot of a terminal testing the Add rule in Task 2",
  height: 4.89cm,
))

#heading(level: 3, "Removing Rule")

The `remove` command removes an existing rule.
If the rule exists, it is removed. If not, an error will be returned.
The rule number must be given.
If an existing rule was given to both incoming and outgoing traffic, a direction command can be added to remove one of the directions from the existing rule.

#figure(caption: "Task 2 Test on removing a new rule", image(
  "./images/Task2/Task2-Testing-RemoveRule.png",
  alt: "Screenshot of a terminal testing the Remove rule in Task 2",
  height: 8.66cm,
))

#heading(level: 3, "Listing Rule")

Lists the existing firewall rules. If no specific rule is given, then all the rules are displayed.
If a direction of incoming (`-in`) or outgoing (`-out`) packets is given, then that direction is displayed. If not, both (all) will be listed.
Address will list the rules matching the given address.

#figure(caption: "Task 2 Test on listing the existing firewall rules", grid(gutter: 0.5em, image(
  "./images/Task2/Task2-Testing-ListRule1.png",
  alt: "Screenshot of a terminal testing the List rule in Task 2",
  height: 6.22cm,
), image(
  "./images/Task2/Task2-Testing-ListRule2.png",
  alt: "Another Screenshot of a terminal testing the List rule in Task 2",
  height: 1.85cm,
)))

\
#line(length: 100%)
#pagebreak()

#heading("Appendix")

The full code for both tasks can be viewed at #link("https://github.com/cr2007/F20CN-CW2") .

#heading(level: 2, "Task 1: Python Code")

#figure(
  caption: "Main Function Python Code",
  ```py #Importing required libraries
import random
import math

# ... Other code

def main():
    input_text: str = "" # Initialize user input variable

    # Start an infinite loop to continuously get input from the user
    while True:
        # Prompt the user to enter a line of plain text
        line = input("Enter a line of plain text "
                    "(press Enter for a new line, or just press Enter to finish): ")

        # If input line is empty, break the loop
        if line == "":
            break

        # Add the input line to the input_text string, followed by a space
        input_text += line + " "

    input_text = input_text.rstrip() # Remove trailing whitespace and '\n' characters

    # Convert the input text to binary
    input_binary: str = ''.join(format(ord(i), '08b') for i in input_text)

    # Split it into a list of 8-bit chunks
    plain_text: list = [ input_binary[i:i+8] for i in range(0,len(input_binary),8) ]

    priv_key = PrivateKey() # Create a PrivateKey object
    private_key: dict = priv_key.calculate_private_key() # Calculates private key

    pub_key = PublicKey(private_key) # Create a PublicKey object with the private key
    public_key: list = pub_key.calculate_public_key() # Calculate the public key (h)

    # Create Encryption object with public key and plain text
    encrypt = Encryption(public_key, plain_text)
    cipher_text: list = encrypt.encryption()

    print(f"Cipher Text: {sum(cipher_text)}") # Print the cipher text

    # Encrypts plain text and store the cipher text in a list
    decrypt = Decryption(cipher_text, private_key) # Create Decryption object
    decrypted_text: str = decrypt.decryption() # Decrypts the ciphertext

    print(f"Decrypted Text: {decrypted_text}") # Print the decrypted text
```)

#pagebreak()

#figure(
  caption: "Private Key Class Python Code",
  ```py class PrivateKey:
    def __init__(self):
        self.e: list[int] = []
        self.q: int = 0
        self.w: int = 0
        self.private_key: dict = {}

    def calculate_private_key(self) -> dict:
        self.e = self.create_random_sequence() # Create a random sequence of integers
        self.q = (2 * self.e[-1]) + random.randint(1, 1000)

        while not self.is_prime(self.q): # If number is not prime, choose another one
            self.q = (2 * self.e[-1]) + random.randint(1, 1000)

        self.w = random.randint(1, self.q+250) # Choose a random integer w
        while math.gcd(self.w, self.q) != 1: # If w and q are not coprime, recalculate 'w'
            self.w = random.randint(1, self.q+250)

        # Store the private key components in a dictionary
        self.private_key = { "e": self.e, "q": self.q, "w": self.w }
        return self.private_key # Return the private key

    def create_random_sequence(self, sequence_length: int = 8) -> list[int]:
        if sequence_length <= 0:
            raise ValueError("Sequence length must be greater than 0.")

        # If sequence length is not a multiple of 8, raise a ValueError
        if sequence_length % 8 != 0:
            raise ValueError("Sequence length must be a multiple of 8.")

        random_sequence: list[int] = [ random.randint(1, 100) ] # Initialize random integer sequence

        while len(random_sequence) < sequence_length: # Generate the rest of the sequence
            next_element:int = sum(random_sequence) + random.randint(1, 100)

            random_sequence.append(next_element) # Add the next element to the sequence

        return random_sequence # Return the random sequence

    # Source: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not
    def is_prime(self, number: int) -> bool:
        if number <= 1:
            raise ValueError("Number must be greater than 1.")
        if number % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(number))+1, 2):
            if number % i == 0:
                return False

        return True # If no divisors found, the number is prime
  ```
)

#pagebreak()

#figure(
  caption: "Public Key Class Python Code",
  ```py class PublicKey:
    def __init__(self, private_key_dict: dict):
        self.e: list = private_key_dict["e"]
        self.q: int  = private_key_dict["q"]
        self.w: int  = private_key_dict["w"]

    def calculate_public_key(self) -> list[int]:
        # Check if the random sequence is empty
        if not self.e:
            raise ValueError("Random sequence cannot be empty.")

        # Check if q and w are greater than 0
        if self.q <= 0 or self.w <= 0:
            raise ValueError("q and w must be greater than 0.")

        # Calculates and returns the public key
        return [ (self.w * i) % self.q for i in self.e ]
```
)

#line(length: 100%)

#figure(
  caption: "Encryption Class Python Code",
  ```py class Encryption:
    def __init__(
      self,
      public_key_list: list[int],
      plain_text_list: list[str]
    ) -> None:
      self.public_key: list[int] = public_key_list
      self.plain_text: list[str] = plain_text_list
      self.cipher_text: list[int] = []

    def encryption(self) -> list[int]:
      if not self.plain_text:
          raise ValueError("Plain Text cannot be empty.")
      if not self.public_key:
          raise ValueError("Public Key List cannot be empty.")

      # Loop through every value in the plain text
      for value in self.plain_text:
          cipher_text_sum: int = 0 # Initialize variable for sum of cipher text

          # Loop through every bit in the value
          for i, bit in enumerate(value):
              # If bit is '1', multiply it with corresponding value in the public key
              cipher_text_sum += (int(bit) * self.public_key[i]) if bit == '1' else 0

          # Append cipher text sum to the encrypted text list
          self.cipher_text.append(cipher_text_sum)

      return self.cipher_text # Return the encrypted text
```
)

#line(length: 100%)
#pagebreak()

#figure(
  caption: "Decryption Class Python Code",
  ```py class Decryption:
  def __init__(self, cipher_text_list: list[int], private_key_dict: dict):
      self.cipher_text: list[int] = cipher_text_list
      self.private_key: dict = private_key_dict
      self.e: list[int] = private_key_dict["e"]
      self.q: int = private_key_dict["q"]
      self.w: int = private_key_dict["w"]
      self.decrypted_text: str = ""

  def decryption(self) -> str:
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

          plain_text_bits += bits # Appending the bits to the plain text bits

      # Converting the binary string to text
      self.decrypted_text: str = ''.join(chr(int(plain_text_bits[i:i+8], 2))
                                for i in range(0, len(plain_text_bits), 8))

      # Returning the plain text
      return self.decrypted_text
```
)

#line(length: 100%)
#pagebreak()

#heading(level: 2, "Task 1: Testing")

#heading(level: 3, "Example 1: Plaintext")

```
To CSK: You cannot worry about upsetting every person you come across, but you must be selectively cruel. If your superior is a falling star, there is nothing to fear from outshining him. Do not be merciful--your master had no such scruples in his own cold-blooded climb to the top. Gauge his strength. If he is weak, discreetly hasten his downfall: Outdo, outcharm, outsmart him at key moments. If he is very weak and ready to fall, let nature take its course. Do not risk outshining a feeble superior--it might appear cruel or spiteful. But if your master is firm in his position, yet you know yourself to be the more capable, hide your time and be patient. It is the natural course of things that power eventually fades and weakens. Your master will fall someday, and if you play it right, you will outlive and someday outshine him.
```

#heading(level: 3, "Example 1: Ciphertext")

#read("./Task1-Examples/Example1/cipher_text1.txt")

#heading(level: 3, "Example 1: Key Generation")
#v(1em)

#figure(caption: "Private and Public Key generated for Example 1 Plaintext", grid(
  gutter: 1em,
  [*Private Key:* #raw(lang: "json", read("./Task1-Examples/Example1/private_key1.txt"))],
  [*Public Key:* #raw(lang: "json", read("./Task1-Examples/Example1/public_key1.txt"))],
))

\
#line(length: 100%)
#pagebreak()

#heading(level: 3, "Example 2: Plaintext")

```
To Chandrashekhar: Do not be one of the many who mistakenly believe that the ultimate form of power is independence. Power involves a relationship between people; you will always need others as allies, pawns, or even as weak masters who serve as your front. The completely independent man would live in a cabin in the woods--he would have the freedom to come and go as he pleased, but he would have no power. The best you can hope for is that others will grow so dependent on you that you enjoy a kind of reverse independence: Their need for you frees you.
```

#heading(level: 3, "Example 2: Ciphertext")

#read("./Task1-Examples/Example2/cipher_text2.txt")

#heading(level: 3, "Example 2: Key Generation")

#figure(caption: "Private and Public Key generated for Example 2 Plaintext", grid(
  gutter: 1em,
  [*Private Key:* #raw(lang: "json", read("./Task1-Examples/Example2/private_key2.txt"))],
  [*Public Key:* #raw(lang: "json", read("./Task1-Examples/Example2/public_key2.txt"))],
))

\
#line(length: 100%)

#heading(level: 2, "Task 2: Python Code")

#figure(
  caption: "Address function and Firewall Rule Class Python Code",
  ```py import sys
import json
from collections import OrderedDict
import ipaddress  # For IP address validation

def address_in_range(check_address, range_address):
  try:
    if '-' in range_address:  # Checks if a range is specified (the hyphen exists)
        # Splits range addresses into start and end addresses
        # and converts them to IP addresses objects.
        start_address, end_address = map(
                                      ipaddress.ip_address,
                                      range_address.split('-')
                                    )
          #check if the ip address is within the specified range.
        return start_address <= ipaddress.ip_address(check_address) <= end_address
      else:
        #checks if the check address matches the IP address
        return ipaddress.ip_address(check_address) ==
                                ipaddress.ip_address(range_address)
  except ValueError:
    return False  # Invalid IP address or range

class FirewallRule:
  def __init__(self, rule_id, direction, address):
    self.rule_id = rule_id     # stores rule in order
    self.direction = direction # 'in', 'out', or 'both'
    self.address = address     # Can be a single IP or range like "0.0.0.0-0.0.0.255"
```
)

#line(length: 100%)
#pagebreak()

#figure(
  caption: "Firewall Class Python Code",
  ```py class Firewall:
    def __init__(self):
        self.rules = OrderedDict()  #Stores the rules in order.
        self.load_rules()  # Load rules from file on startup

    def add_rule(self, rule_id, direction, address):  #add new rule to firewall
        # Validate IP address or range
        if not self.validate_ip_address(address):
            print("Invalid IP address or range.")
            return

        # Update existing rules if needed
        if rule_id in self.rules:
            new_rules = OrderedDict()
            for key, value in self.rules.items():
                if key >= rule_id:
                    new_rules[key + 1] = value #move the old rule down for the new rule
                else:
                    new_rules[key] = value
            self.rules = new_rules

        self.rules[rule_id] = FirewallRule(rule_id, direction, address) #add new rule to list
        self.save_rules() #save the new set of rules

    def remove_rule(self, rule_id, direction=None): # Remove rule from firewall
        if rule_id not in self.rules:
            return "Error: Rule does not exist."
        else:
            if self.rules[rule_id].direction == 'both' and direction:
                self.rules[rule_id].direction = 'in' if direction == 'out' else 'out'
            else:
                del self.rules[rule_id]
            self.save_rules()  # Save rules after removing

    def list_rules(self, rule_id=None, direction=None, address=None):
        listed_rules = []
        for key, value in sorted(self.rules.items()):
             #Skip this rule if it doesn't have the rule ID we're looking for.
            if rule_id is not None and key != rule_id:
                continue
            # Skip this rule if it doesn't go in the direction we're looking for.
            if direction is not None and not (value.direction == direction or value.direction == 'both'):
                continue
             # If the rule passes all checks, add it to our list.
            if address is not None and not address_in_range(address, value.address):
                continue
            listed_rules.append((key, value.direction, value.address))
        return listed_rules

    def save_rules(self):
        with open('firewall_rules.json', 'w') as file:
            # Turn the rules into text that a computer can read (JSON) and save it in a file.
            json.dump({k: v.__dict__ for k, v in self.rules.items()}, file, indent=4)

    def load_rules(self):
        try:
            with open('firewall_rules.json', 'r') as file:
                # Read the rules from the file and turn them back into a format our program can use.
                rules_data = json.load(file)
                self.rules = OrderedDict({int(k): FirewallRule(**v) for k, v in rules_data.items()})
        except FileNotFoundError:
            pass  # If there's no file with rules in it, just do nothing.

    def validate_ip_address(self, address):
        try:
            if '-' in address:
            # If the address is a range (like 0.0.0.0 - 0.0.0.255), check both start and end are okay.
                start_ip, end_ip = address.split('-')
                ipaddress.ip_address(start_ip)  # Validate start IP
                ipaddress.ip_address(end_ip)    # Validate end IP
            else:
                # If it's just one address, check it's okay.
                ipaddress.ip_address(address)  # Validate single IP
            return True  # If the address(es) are okay, say so.
        except ValueError:
            return False # If the address(es) are not okay, say so.
  ```
)

#line(length: 100%)

#figure(
  caption: "Main Function Python Code",
  ```py def main():
  fw = Firewall()

  try:
      # Check if any command-line arguments are provided.
      if len(sys.argv) > 1:
          command = sys.argv[1]  # Get the command from the first argument.
          # Check if the command is 'add' to add a new rule.
          if command == "add":
              # If only an address is provided, add a rule with default ID and direction.
              if len(sys.argv) == 3:   # Check for command format 'add [addr]'
                  address = sys.argv[2] # Get the address from the arguments.
              # Validate the given IP address.
                  if not fw.validate_ip_address(address):
                      print("Invalid IP address or range.")
                      sys.exit(1) # Exit if the address is invalid.
                    # Add the rule with the default ID and direction.
                  fw.add_rule(1, "both", address)
                  # Print confirmation of the added rule.
                  print(f"Rule added with default ID and direction: {json.dumps({'rule_id': 1, 'direction': 'both', 'address': address})}")

              # If a rule ID and an address are provided, add a rule with the given ID and default direction.
              elif len(sys.argv) == 4: # Check for command format 'add [rule] [addr]'
                  rule_id = int(sys.argv[2]) # Get the rule ID from the arguments.
                  address = sys.argv[3] # Get the address from the arguments.
                  # Validate the given IP address.
                  if not fw.validate_ip_address(address):
                      print("Invalid IP address or range.")
                      sys.exit(1) # Exit if the address is invalid.
                      # Add the rule with the given ID and default direction.
                  fw.add_rule(rule_id, "both", address)
                    # Print confirmation of the added rule.
                  print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': 'both', 'address': address})}")

                # If a rule ID, direction, and address are provided, add a rule with the given details.
              elif len(sys.argv) == 5:  # Check for command format 'add [rule] [direction] [addr]'
                  rule_id = int(sys.argv[2]) # Get the rule ID from the arguments.
                  direction = sys.argv[3] # Get the direction from the arguments.
                  address = sys.argv[4] # Get the address from the arguments.
                  # Validate the given IP address.

                  if not fw.validate_ip_address(address):
                      print("Invalid IP address or range.")
                      sys.exit(1) # Exit if the address is invalid.

                  # Add the rule with the given details.
                  fw.add_rule(rule_id, direction, address)
                  # Print confirmation of the added rule.
                  print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': direction, 'address': address})}")

              else:
                  # Print an error message if the command format is incorrect.
                  print("Error: Invalid arguments for add command.")
                  sys.exit(1)   # Exit the program.

          # Check if the command is 'remove' to remove a rule.
          elif command == 'remove':
              # Check if at least a rule ID is provided.
              if len(sys.argv) >= 3:
                  rule_id = int(sys.argv[2]) # Get the rule ID from the arguments.
                  # Get the direction if provided, otherwise set it to None.
                  direction = sys.argv[3][1:] if len(sys.argv) > 3 and sys.argv[3].startswith('-') else None
                  # Remove the rule with the given ID and direction.
                  result = fw.remove_rule(rule_id, direction)
                  # Print the result of the removal operation.
                  if result:
                      print(result)
                  else:
                      print(f"Rule {rule_id} {'direction adjusted' if direction else 'removed'}.")
              else:
                  # Print an error message if the command format is incorrect.
                  print("Invalid command or insufficient arguments.")
                  sys.exit(1) # Exit the program.


          # Check if the command is 'list' to list rules.
          elif command == 'list':
              rule_id = None
              direction = None
              address = None

              # Iterate through additional arguments to set the filter criteria.
              for arg in sys.argv[2:]:
                  if arg.isdigit():  # Check if the argument is a digit (for rule ID).
                      rule_id = int(arg) # Set the rule ID for filtering.
                  elif arg in ['-in', '-out']:  # Check if argument is '-in' or '-out'.
                      direction = 'in' if arg == '-in' else 'out' # Set the direction for filtering.
                  elif arg.count('.') == 3 or '-' in arg: # Check if the argument is an IP address or range.
                      address = arg # Set the address for filtering.
                  else:
                      # Print an error message for invalid arguments.
                      print(f"Invalid argument for list command: {arg}")
                      sys.exit(1) # Exit the program.


              # List the rules based on the given filter criteria.
              for rule in fw.list_rules(rule_id, direction, address):
                  print(f"Rule {rule[0]}: Direction: [{rule[1]}], Address: [{rule[2]}]")

          else:
              # Print an error message for invalid commands.
              print("Error: Invalid command. Usage: python script.py [command] [arguments]")
              sys.exit(1) # Exit the program.

        else:
            # Print an error message if no arguments are provided.
            print("Error: Invalid arguments.\nUsage: python task2-g14.py add [rule_id> [-in | -out] <address>\n\nExample: python task2-g14.py add 1 -in 10.0.0.1")
        sys.exit(1) # Exit the program.
    except IndexError:
        sys.exit(1) # Exit the program if an IndexError occurs.

if __name__ == "__main__":
    main()
  ```
)

#heading(level: 2, "Task 2: Testing")

#figure(
  caption: "List Addresses",
  image("./images/Task2/Appendix-Task2-Testing-ListAddresses.png", alt: "Screenshot of Task 2 - Listing Addresses"),
)

#figure(
  caption: "Adding and List Addresses",
  image("./images/Task2/Appendix-Task2-Testing-AddingAndListAddresses.png", alt: "Screenshot of Task 2 - Adding and Listing Addresses"),
)

#figure(
  caption: "Address Ranges",
  image("./images/Task2/Appendix-Task2-Testing-AddressRanges.png", alt: "Screenshot of Task 2 - Address Ranges"),
)

#figure(
  caption: "Error Handling",
  grid(
    gutter: 0.5em,
    image("./images/Task2/Appendix-Task2-Testing-ErrorHandling_1.png", alt: "Screenshot of Task 2 - Error Handling (1)"),
    image("./images/Task2/Appendix-Task2-Testing-ErrorHandling_2.png", alt: "Screenshot of Task 2 - Error Handling (2)"),
  ),
)

#line(length: 100%)
