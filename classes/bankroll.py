class Bankroll():

    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f'{self.owner.name}: ${self.balance}'

    def bet(self, amount):
        """ Removes bet value from balance """

        if (amount <= 0 or amount > self.balance):
            print('Invalid bet! Try again!')
            raise ValueError

        self.balance -= amount
        return amount

    def add_funds(self, amount):
        """ Adds funds to balance """

        if amount <= 0:
            print('Invalid amount! Try again!')
            return False

        self.balance += amount
        return True

    def make_bet(self):
        """ Asks for user input to make bet """
        player_bet = 0
        while True:
            try:
                player_bet = self.bet(
                    int(input('Enter the amount you want to bet: '))
                )
            except:
                print('Invalid value for a bet. Try again!')
            else:
                break

        return player_bet

    def make_deposit(self):
        """ Asks for user input to add funds """
        while True:
            try:
                deposit = int(
                    input(
                        'Enter the amount you want to deposit: '
                    )
                )
                if deposit <= 0:
                    raise ValueError

                self.add_funds(deposit)
                print(f'Funds added. New balance: ${self.balance}')
                input()
            except:
                print('Invalid value for a deposit. Try again!')
            else:
                break
