import sys
from collections import OrderedDict

class FirewallRule:
    def __init__(self, rule_id, direction, address):
        self.rule_id = rule_id
        self.direction = direction  # 'in', 'out', or 'both'
        self.address = address

class Firewall:
    def __init__(self):
        self.rules = OrderedDict() #

    def add_rule(self, rule_id, direction, address):
        # Check if rule_id already exists
        if rule_id in self.rules:
            # Shift the rule IDs of existing rules
            new_rules = OrderedDict()
            for key, value in self.rules.items():
                if key >= rule_id:
                    new_rules[key + 1] = value
                else:
                    new_rules[key] = value
            self.rules = new_rules

        # Insert the new rule
        self.rules[rule_id] = FirewallRule(rule_id, direction, address)

    def remove_rule(self, rule_id, direction):
        if rule_id not in self.rules:
            return "Error! Rule Does Not Exist."
        else:
            if self.rules[rule_id].direction == 'both' and direction != 'both':
                self.rules[rule_id].direction = 'in' if direction == 'out' else 'out'
            else:
                del self.rules[rule_id]

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

def main():
    fw = Firewall()

    while True:
        command_line = input("Enter command: ").split()
         # Split command line input on spaces

         # Parse command and execute corresponding Firewall method
        if command_line[0] == 'add':
            rule_id = int(command_line[1]) if len(command_line) > 1 and command_line[1].isdigit() else 1
            direction = command_line[command_line.index("-in") if "-in" in command_line else command_line.index("-out") if "-out" in command_line else -1].replace("-", "") if "-in" in command_line or "-out" in command_line else "both"
            address = command_line[-1]
            fw.add_rule(rule_id, direction, address)
            print(f"Rule {rule_id} added for {direction} traffic to address {address}.")

        elif command_line[0] == 'remove':
            rule_id = int(command_line[1])
            direction = 'both'
            if "-in" in command_line:
                direction = 'in'
            elif "-out" in command_line:
                direction = 'out'
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

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

