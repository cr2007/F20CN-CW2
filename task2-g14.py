import sys
import json
from collections import OrderedDict
import ipaddress  # For IP address validation

def address_in_range(check_address, range_address):
    try:
        if '-' in range_address:#check if a range is specified (the hyphen exists)
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
        self.rule_id = rule_id      #stores rule in order
        self.direction = direction  # 'in', 'out', or 'both'
        self.address = address      # Can be a single IP or a range like "0.0.0.0-0.0.0.255"

class Firewall:
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
         #add new rule to list
        self.rules[rule_id] = FirewallRule(rule_id, direction, address)
        self.save_rules() #save the new set of rules

    def remove_rule(self, rule_id, direction=None):#remove rule from firewall
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
         # If the rule passes all checks, add it to our list.

    def save_rules(self):
        with open('firewall_rules.json', 'w') as file:
            # Turn the rules into text that a computer can read (JSON) and save it in a file.
            json.dump({k: v.__dict__ for k, v in self.rules.items()}, file, indent=4)
             # This function saves our rules so we can use them later.

    def load_rules(self):
        try:
            with open('firewall_rules.json', 'r') as file:
                # Read the rules from the file and turn them back into a format our program can use.
                rules_data = json.load(file)
                self.rules = OrderedDict({int(k): FirewallRule(**v) for k, v in rules_data.items()})
        except FileNotFoundError:
            pass  # If there's no file with rules in it, just do nothing.
    # This function gets our saved rules ready to use when we start the program.

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
    # Checks if the address or range of addresses is written in the right way.


def main():
    fw = Firewall()

    try:
        if len(sys.argv) > 1:
            command = sys.argv[1]

            #check if instructions have been given when the prgram starts.
            if command == "add":
                if len(sys.argv) == 3:  # add [addr]
                    address = sys.argv[2]
                    if not fw.validate_ip_address(address):
                        print("Invalid IP address or range.")
                        sys.exit(1)
                    fw.add_rule(1, "both", address)
                    print(f"Rule added with default ID and direction: {json.dumps({'rule_id': 1, 'direction': 'both', 'address': address})}")

                elif len(sys.argv) == 4:  # add [rule] [addr]
                    rule_id = int(sys.argv[2])
                    address = sys.argv[3]
                    if not fw.validate_ip_address(address):
                        print("Invalid IP address or range.")
                        sys.exit(1)
                    fw.add_rule(rule_id, "both", address)
                    print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': 'both', 'address': address})}")

                elif len(sys.argv) == 5:  # add [rule] [direction] [addr]
                    rule_id = int(sys.argv[2])
                    direction = sys.argv[3]
                    address = sys.argv[4]
                    if not fw.validate_ip_address(address):
                        print("Invalid IP address or range.")
                        sys.exit(1)
                    fw.add_rule(rule_id, direction, address)
                    print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': direction, 'address': address})}")

                else:
                    print("Error: Invalid arguments for add command.")
                    sys.exit(1)

            elif command == 'remove':
                if len(sys.argv) >= 3:
                    rule_id = int(sys.argv[2])
                    direction = sys.argv[3][1:] if len(sys.argv) > 3 and sys.argv[3].startswith('-') else None
                    result = fw.remove_rule(rule_id, direction)
                    if result:
                        print(result)
                    else:
                        print(f"Rule {rule_id} {'direction adjusted' if direction else 'removed'}.")
                else:
                    print("Invalid command or insufficient arguments.")
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
                    elif arg.count('.') == 3 or '-' in arg:  # Check for an IP address or range
                        address = arg
                    else:
                        print(f"Invalid argument for list command: {arg}")
                        sys.exit(1)

                    for rule in fw.list_rules(rule_id, direction, address):
                        print(f"Rule {rule[0]}: Direction: [{rule[1]}], Address: [{rule[2]}]")

                else:
                    print("Error: Invalid command. Usage: python script.py [command] [arguments]")
                    sys.exit(1)

        else:
            print("Error: Invalid arguments.\nUsage: python task2-g14.py add [rule_id> [-in | -out] <address>\n\nExample: python task2-g14.py add 1 -in 10.0.0.1")
        sys.exit(1)
    except IndexError:
        sys.exit(1)

if __name__ == "__main__":
    main()
