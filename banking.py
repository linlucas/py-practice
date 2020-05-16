class Account:
    def __init__(self, first='', last='', nationality='', balance=0):
        self.first_name = first
        self.last_name = last
        self.nationality = nationality
        self.balance = balance

    def __repr__(self):
        return 'Name: {} {}\nNationality: {}\nBalance: {}'\
            .format(self.first_name, self.last_name, self.nationality, self.balance)

    def get_name(self):
        name = input('please enter your name: ')
        name = name.split()
        self.first_name = name[0]
        self.last_name = name[1]

    def get_nationality(self):
        self.nationality = input('please enter your nationality: ')

    def deposit(self):
        self.balance += input('how much money would you like to deposit?\n')

    def withdraw(self):
        cash = input('how much money would you like to withdraw?\n')
        if int(cash) > self.balance:
            print('you do not have enough money in your account\n')
        else:
            self.balance -= int(cash)
            print('withdrawal successful')


lucas = Account('Lucas', 'Lin', 'American', 100)
lucas.withdraw()
print(lucas)