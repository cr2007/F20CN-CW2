# F20CN CW2

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cr2007/F20CN-CW2)

## [Computer Network Security (F20CN)](https://curriculum.hw.ac.uk/coursedetails/F20CN?termcode=202425&programmeCode=F291-COS)

### Asymmetric Cryptography, Firewall Rules Maintenance

Team Members:
- Chandrashekhar Ramaprasad (cr2007)
- Oluwadolabomi Faith Muraino (fm2020)

---

1. **Task 1 - Alternative Method of Public-Key Encryption**
Develops an asymmetric cryptography system with custom methods for generating public and private keys, encryption, and decryption of messages.

2. **Task 2 - Firewall Rules Application**
Implements tools to validate and process IP addresses and ranges, ensuring compliance with firewall rules and configurations.

---

## Requirements

- Python 3.8+
- Dependencies
  - [`ipaddress`](https://docs.python.org/3/library/ipaddress.html) (Standard library module for IP validation)
  - (Optional) [`pytest`](https://docs.pytest.org/en/stable) for running Task 1 tests

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/cr2007/F20CN-CW2
cd F20CN-CW2
```

### Run the Scripts

#### Task 1: Public-Key Encryption

```bash
python task1-g14.py
```

This script includes:
- Key generation (private and public keys)
- Encryption and decryption functionalities

#### Task 2: Firewall Rules Maintenance

```bash
# Add new rule to the list of firewall rules
python task2-g14.py add [rule] [-in | -out] addr

# Remove existing rule from the list of firewall rules
python task2-g14.py remove [rule] [-in | -out]

# Lists existing firewall rules
python task2-g14.py list [rule] [-in | -out] [affr]
```

This script includes:
- Validating IP addresses
- Checking if an IP falls within a given range
- JSON-based input for easy testing of rules

---

## Project Contributors

This project was completed as part of the [F20CN: Computer Network Security](https://curriculum.hw.ac.uk/coursedetails/F20CN?termcode=202425&programmeCode=F291-COS) module at Heriot-Watt University.<br>Contributions were made by [@cr2007](https://github.com/cr2007) and [@faithm2020](https://github.com/faithm2020).
