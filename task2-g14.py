import sys
import json
from collections import OrderedDict

class FirewallRule:
    def __init__(self, rule_id, direction, address):
        self.rule_id = rule_id
        self.direction = direction  # 'in', 'out', or 'both'
        self.address = address

class Firewall:
    def __init__(self):
        self.rules = OrderedDict()
        self.load_rules()  # Load rules from file on startup

    def add_rule(self, rule_id, direction, address):
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

    def remove_rule(self, rule_id, direction):
        if rule_id not in self.rules:
            return "Error: Rule does not exist."
        else:
            if self.rules[rule_id].direction == 'both' and direction != 'both':
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

def main():
    fw = Firewall()

    while True:
        command_line = input("Enter command: ").split()

        if command_line[0] == 'add':
            if len(command_line) == 2:
                # Only address provided, use defaults for rule_id and direction
                address = command_line[1]
                fw.add_rule(1, "both", address)
                print(f"Rule added with default ID and direction: {json.dumps({'rule_id': 1, 'direction': 'both', 'address': address})}")
                sys.exit()
            elif len(command_line) > 2 and command_line[1].isdigit():
                # Rule ID and possibly direction provided
                rule_id = int(command_line[1])
                direction = command_line[2] if len(command_line) > 3 else "both"
                address = command_line[-1]
                fw.add_rule(rule_id, direction, address)
                print(f"Rule added: {json.dumps({'rule_id': rule_id, 'direction': direction, 'address': address})}")
                sys.exit()
            else:
                print("Error: Invalid arguments for add command.")
                continue

        elif command_line[0] == 'remove':
            rule_id = int(command_line[1]) if len(command_line) > 1 and command_line[1].isdigit() else None
            if rule_id is None:
                print("Error: Rule ID must be a number.")
                continue
            direction = command_line[2] if len(command_line) > 2 else "both"
            result = fw.remove_rule(rule_id, direction)
            if result:
                print(result)
            else:
                print(f"Rule {rule_id} removed for {direction} traffic.")

        elif command_line[0] == 'list':
            rule_id = None
            direction = None
            address = None
            if len(command_line) > 1:
                if command_line[1].isdigit():
                    rule_id = int(command_line[1])
                for arg in command_line:
                    if arg == "-in":
                        direction = 'in'
                    elif arg == "-out":
                        direction = 'out'
                    elif arg.count('.') == 3:  # simple check for an IP address
                        address = arg
            for rule in fw.list_rules(rule_id, direction, address):
                print(f"Rule {rule[0]}: {rule[1]} - {rule[2]}")
            sys.exit()
        else:
            print("Invalid command.")
            continue

if __name__ == "__main__":
    main()
