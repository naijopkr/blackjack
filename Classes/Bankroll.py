class Bankroll():

    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f'{self.owner.name}: ${self.balance}'

    def bet(self, amount):
        if (amount <= 0 or amount > self.balance):
            print('Invalid bet! Try again!')
            raise ValueError

        self.balance -= amount
        print(f'Bet placed for ${amount}.\nUpdated balance: ${self.balance}')
        return amount

    def add_funds(self, amount):
        if (amount <= 0):
            print('Invalid amount! Try again!')
            return False

        self.balance += amount
        print(f'Deposit made for ${amount}.\nUpdated balance: ${self.balance}')
        return True