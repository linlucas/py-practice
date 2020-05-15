class Account:
    def __init__(self, first='', last='', nationality='', balance=0):
        self.first_name = first
        self.last_name = last
        self.nationality = nationality
        self.balance = balance

    def __repr__(self):
        return 'Name: {} {}\nNationality: {}\nBalance: {}'\
            .format(self.first_name, self.last_name, self.nationality, self.balance)


lucas = Account()
print(lucas)