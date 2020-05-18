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
        full_name = input('please enter your name: ')
        full_name = full_name.split()
        self.first_name = full_name[0]
        self.last_name = full_name[1]

    def get_nationality(self):
        self.nationality = input('please enter your nationality: ')

    def deposit(self):
        cash = input('how much money would you like to deposit?\n')
        self.balance += int(cash)

    def withdraw(self):
        cash = input('how much money would you like to withdraw?\n')
        if int(cash) > self.balance:
            print('you do not have enough money in your account\n')
        else:
            self.balance -= int(cash)
            print('withdrawal successful')


bank = []
while True:
    print('Hi, welcome to the bank!\nPlease choose from the following options:')
    print('1: Create an account')
    print('2: Deposit money')
    print('3: Withdraw money')
    print('4: Close account')
    response = input()
    response = int(response)

    if response == 1:
        this = Account()
        this.get_name()
        this.get_nationality()
        print('Account created!')
        bank.append(this)
        this.deposit()
    if 2 <= response <= 4:
        name = input('What is your last name?\n')
        for account in bank:
            if account.last_name == name:
                if response == 2:
                    account.deposit()
                if response == 3:
                    account.withdraw()
                if response == 4:
                    bank.remove(account)

    response = input('Would you like to leave? y/n\n')
    if response == 'y':
        break
