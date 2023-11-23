import sys
import json
import ipaddress  # For IP address validation
from collections import OrderedDict 

def address_in_range(check_address, range_address):
    try:
        if '-' in range_address:
            start_address, end_address = map(ipaddress.ip_address, range_address.split('-'))
            return start_address <= ipaddress.ip_address(check_address) <= end_address
        else:
            return ipaddress.ip_address(check_address) == ipaddress.ip_address(range_address)
    except ValueError:
        return False  # Invalid IP address or range

class FirewallRule:
    def __init__(self, rule_id, direction, address):
        self.rule_id: int = rule_id
        self.direction: str = direction  # 'in', 'out', or 'both'
        self.address: str = address

class Firewall:
    def __init__(self):
        self.rules = OrderedDict()
        self.load_rules()  # Load rules from file on startup

    def add_rule(self, rule_id, direction: None, address):
        if direction is None:
            direction = 'both'

        if rule_id in self.rules:
            new_rules = OrderedDict()
            for key, value in self.rules.items():
                if key >= rule_id:
                    new_rules[key + 1] = value
                else:
                    new_rules[key] = value
            self.rules = new_rules
        self.rules[rule_id] = FirewallRule(rule_id, direction, address)
        self.save_rules()  # Save rules after adding

    def remove_rule(self, rule_id: int, direction: None):
        if direction is None:
            direction = 'both'
        if rule_id not in self.rules:
            return "Error! Rule Does Not Exist."
            sys.exit(1)
        else:
            if direction != "both":
                del self.rules[rule_id]
            elif self.rules[rule_id].direction == 'both':
                self.rules[rule_id].direction = 'in' if direction == 'out' else 'out'
            else:
                del self.rules[rule_id]
            self.save_rules()  # Save rules after removing

    def list_rules(self, rule_id=None, direction=None, address=None):
        listed_rules = []
        for key, value in self.rules.items():
            if rule_id is not None and rule_id != key:
                continue
            if direction is not None and value.direction != direction and value.direction != 'both':
                continue
            if address is not None and address != value.address:
                continue
            listed_rules.append((key, value.direction, value.address))
        return listed_rules

    def save_rules(self):
        with open('firewall_rules.json', 'w') as file:
            json.dump({k: v.__dict__ for k, v in self.rules.items()}, file, indent=4)

    def load_rules(self):
        try:
            with open('firewall_rules.json', 'r') as file:
                rules_data = json.load(file)
                self.rules = OrderedDict({int(k): FirewallRule(**v) for k, v in rules_data.items()})
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty rules set
    
    def validate_ip_address(self, address):
        try:
            if '-' in address:
                start_ip, end_ip = address.split('-')
                ipaddress.ip_address(start_ip)  # Validate start IP
                ipaddress.ip_address(end_ip)    # Validate end IP
            else:
                ipaddress.ip_address(address)  # Validate single IP
            return True
        except ValueError:
            return False

def main():
    fw = Firewall()

    try:
        if len(sys.argv) > 1:
            command = sys.argv[1]
            # Can use os.argv to get command line arguments instead of input()
            # command_line = input("Enter command: ").split()

            # sys.argv = ['task2-g14.py', 'add', '1', '-in', '10.1.3.1']
            if command == "add":
                if len(sys.argv) == 2:
                    # Only address provided, use defaults for rule_id and direction
                    address = sys.argv[1]
                    fw.add_rule(1, address)
                    print(f"Rule added with default ID and direction: {json.dumps({'rule_id': 1, 'direction': 'both', 'address': address})}")
                    sys.exit(0)
                elif len(sys.argv) > 2 and str(sys.argv[2]).isdigit():
                    # Rule ID and possibly direction provided
                    rule_id = int(sys.argv[2])
                    direction = sys.argv[3] if len(sys.argv) > 3 else "both"
                    address = sys.argv[-1]
                    fw.add_rule(rule_id, direction, address)
                    print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': direction, 'address': address})}")
                    sys.exit(0)
                else:
                    print("Error: Invalid arguments for add command.")
                    sys.exit(1)

            #remove [rule] [-in/-out]
            # If an existing rule was given to both incoming and outgoing traffic, a direction command can be added to remove one of the directions from the existing rule.

            elif command == 'remove':
                if len(sys.argv) >= 3:  # remove [rule] and remove [rule] [-in/-out]
                    rule_id = int(sys.argv[2])
                    direction = sys.argv[3] if len(sys.argv) > 3 else "both"
                if direction.startswith('-'):
                    direction = direction[1:]  # Remove the '-' prefix
                result = fw.remove_rule(rule_id, direction)
                if result:
                    print(result)
                else:
                    print(f"Rule {rule_id} removed for {direction} traffic.")

            elif command == 'list':
                rule_id = None
                direction = None
                address = None

                if len(sys.argv) > 1:
                    if sys.argv[1].isdigit():
                        rule_id = int(sys.argv[1])
                    for arg in sys.argv:
                        if arg == "-in":
                            direction = 'in'
                        elif arg == "-out":
                            direction = 'out'
                        elif arg.count('.') == 3:  # simple check for an IP address
                            address = arg

                for rule in fw.list_rules(rule_id, direction, address):
                    print(f"Rule {rule[0]}: Direction: [{rule[1]}], Address: [{rule[2]}]")

            else:
                print("Invalid command.")

        else:
            print("Error: Invalid arguments.\nUsage: python task2-g14.py add [rule_id> [-in | -out] <address>\n\nExample: python task2-g14.py add 1 -in 10.0.0.1")
    except IndexError:
        sys.exit(1)

if __name__ == "__main__":
    main()
