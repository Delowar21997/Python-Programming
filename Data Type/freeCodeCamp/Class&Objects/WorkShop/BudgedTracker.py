class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination.name}')
        destination.deposit(amount, f'Transfer from {self.name}')
        return True

    def __str__(self):
        title = self.name.center(30, '*')
        lines = []
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:.2f}"[:7].rjust(7)
            lines.append(desc + amt)
        return '\n'.join([title] + lines + [f"Total: {self.get_balance():.2f}"])


def create_spend_chart(categories):
    spent = [
        abs(sum(e['amount'] for e in c.ledger if e['amount'] < 0))
        for c in categories
    ]
    total = sum(spent)
    percentages = [
        (int((s / total) * 10) * 10) if total else 0
        for s in spent
    ]

    lines = ['Percentage spent by category']

    for level in range(100, -1, -10):
        row = str(level).rjust(3) + '| '
        row += ''.join('o  ' if p >= level else '   ' for p in percentages)
        lines.append(row)

    lines.append('    ' + '-' * (len(categories) * 3 + 1))

    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        row = '     '
        row += ''.join(
            (c.name[i] if i < len(c.name) else ' ') + '  '
            for c in categories
        )
        lines.append(row)

    return '\n'.join(lines)

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {destination.name}')
        destination.deposit(amount, f'Transfer from {self.name}')
        return True

    def __str__(self):
        title = self.name.center(30, '*')
        lines = []
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:.2f}"[:7].rjust(7)
            lines.append(desc + amt)
        return '\n'.join([title] + lines + [f"Total: {self.get_balance():.2f}"])


def create_spend_chart(categories):
    spent = [
        abs(sum(e['amount'] for e in c.ledger if e['amount'] < 0))
        for c in categories
    ]
    total = sum(spent)
    percentages = [
        (int((s / total) * 10) * 10) if total else 0
        for s in spent
    ]

    lines = ['Percentage spent by category']

    for level in range(100, -1, -10):
        row = str(level).rjust(3) + '| '
        row += ''.join('o  ' if p >= level else '   ' for p in percentages)
        lines.append(row)

    lines.append('    ' + '-' * (len(categories) * 3 + 1))

    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        row = '     '
        row += ''.join(
            (c.name[i] if i < len(c.name) else ' ') + '  '
            for c in categories
        )
        lines.append(row)

    return '\n'.join(lines)

if __name__ == '__main__':
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')

    clothing = Category('Clothing')
    food.transfer(50, clothing)
    clothing.withdraw(28.50, 'shirt')

    auto = Category('Auto')
    auto.deposit(300, 'deposit')
    auto.withdraw(45, 'gas')

    print(food)
    print()
    print(clothing)
    print()
    print(auto)
    print()
    print(create_spend_chart([food, clothing, auto]))