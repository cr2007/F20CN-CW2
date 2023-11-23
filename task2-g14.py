import sys
import json
from collections import OrderedDict
import ipaddress  # For IP address validation

def address_in_range(check_address, range_address):
    try:
        if '-' in range_address: #check if a range is specified (the hyphen exists)
            #split the range addresses into start and end addresses and converts them to ip addresses objects.
            start_address, end_address = map(ipaddress.ip_address, range_address.split('-'))
            #check if the ip address is within the specified range.
            return start_address <= ipaddress.ip_address(check_address) <= end_address
        else:
            #checks if the check address matches the IP address
            return ipaddress.ip_address(check_address) == ipaddress.ip_address(range_address)
    except ValueError:
        return False  # Invalid IP address or range

class FirewallRule:
    def __init__(self, rule_id, direction, address):
        self.rule_id = rule_id
        self.direction = direction  #'in', 'out', or 'both'
        self.address = address      #Can be a single IP or a range from "0.0.0.0-255.255.255.255"

class Firewall:
    def __init__(self):
        self.rules = OrderedDict()
        self.load_rules()  # Load rules from file on startup

    def add_rule(self, rule_id, direction: None | str, address):
        # Validate IP address or range
    
        # Update existing rules if needed
        if rule_id in self.rules:
            new_rules = OrderedDict()
            for key, value in self.rules.items():
                if key >= rule_id:
                    new_rules[key + 1] = value
                else:
                    new_rules[key] = value
            self.rules = new_rules

        self.rules[rule_id] = FirewallRule(rule_id, direction, address)
        self.save_rules()

    def remove_rule(self, rule_id: int, direction: None | str = None):
        if rule_id not in self.rules:
            print("Error: Rule does not exist.")
            return
        else:
            if self.rules[rule_id].direction == 'both' and direction != 'both':
                self.rules[rule_id].direction = 'in' if direction == 'out' else 'out'
            else:
                del self.rules[rule_id]
            self.save_rules()  # Save rules after removing

    def list_rules(self, rule_id=None, direction=None, address=None):
        listed_rules = []
        for key, value in sorted(self.rules.items()):
            if rule_id is not None and key != rule_id:
                continue
            if direction is not None and not (value.direction == direction or value.direction == 'both'):
                continue
            if address is not None and not address_in_range(address, value.address):
                continue
            listed_rules.append((key, value.direction, value.address))
        return listed_rules

    def save_rules(self):
        with open('firewall_rules.json', 'w') as file: #open firewall_rules.json in write mode
            #convert 
            json.dump({k: v.__dict__ for k, v in self.rules.items()}, file, indent=4) 

    def load_rules(self):
        try:
            with open('firewall_rules.json', 'r') as file:
                rules_data = json.load(file)
                self.rules = OrderedDict({int(k): FirewallRule(**v) for k, v in rules_data.items()})
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty rules set
        except json.decoder.JSONDecodeError:
            print("There are no rules to list.\nExiting...") # If the file is empty, exit
            sys.exit(0)

    def validate_ip_address(self, address):
        try:
            # Define the allowed range
            allowed_start = ipaddress.ip_address("0.0.0.0")
            allowed_end = ipaddress.ip_address("0.0.0.255")

            if '-' in address:
                start_ip, end_ip = address.split('-')
                start_ip = ipaddress.ip_address(start_ip)  # Validate start IP
                end_ip = ipaddress.ip_address(end_ip)      # Validate end IP

                # Check if the provided range is within the allowed range
                return allowed_start <= start_ip and end_ip <= allowed_end
            else:
                ip = ipaddress.ip_address(address)  # Validate single IP
                return allowed_start <= ip <= allowed_end
        except ValueError:
            return False

def main():
    fw = Firewall()

 
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "add":
            if len(sys.argv) == 3:  # add [addr]
                address = sys.argv[2]
                fw.add_rule(1, "both", address)
                print(f"Rule added with default ID and direction: {json.dumps({'rule_id': 1, 'direction': 'both', 'address': address})}")
            elif len(sys.argv) == 4:  # add [rule] [addr]
                rule_id = int(sys.argv[2])
                address = sys.argv[3]
                fw.add_rule(rule_id, "both", address)
                print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': 'both', 'address': address})}")
            elif len(sys.argv) == 5:  # add [rule] [direction] [addr]
                rule_id = int(sys.argv[2])
                direction = sys.argv[3]
                address = sys.argv[4]
                fw.add_rule(rule_id, direction, address)
                print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': direction, 'address': address})}")
            else:
                print("Error: Invalid arguments for add command.")
                sys.exit(1)

        elif command == 'list':
            rule_id = None
            direction = None
            address = None

        for arg in sys.argv[2:]:
            if arg.isdigit():
                rule_id = int(arg)
            elif arg in ['-in', '-out']:
                direction = 'in' if arg == '-in' else 'out'
            elif arg.count('.') == 3:
                address = arg
            else:
                print("Invalid command.")
                return

        for rule in fw.list_rules(rule_id, direction, address):
            print(f"Rule {rule[0]}: Direction: [{rule[1]}], Address: [{rule[2]}]")

    else:
        print("Error: Invalid arguments.\nUsage: python task2-g14.py add [rule_id> [-in | -out] <address>\n\nExample: python task2-g14.py add 1 -in 10.0.0.1")

if __name__ == "__main__":
    main()
