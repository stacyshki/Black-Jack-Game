class Wallet:
    def __init__(self, money, credit, debt, total_win):
        self.money = money
        self.credit = credit
        self.debt = debt
        self.total_win = total_win

    def __str__(self):
        return f'Money left:{self.money}\tCredit left:{self.credit}\tYour debt:{self.debt}\tTotal win:{self.total_win}'

    def credit_system(self, stake):
        answer_credit = input('You have no money, do you want to take a credit?(yes/no) ')
        if answer_credit == 'yes':
            try:
                sum_credit = int(input(f'How much would it be?(max {self.credit}) '))
            except ValueError:
                sum_credit = stake - self.money
                print(f'\nSomething went wrong, therefore your stake has been set to {sum_credit}')
            if sum_credit < stake - self.money:
                print('That is not enough. Try again.')
                while sum_credit < stake - self.money:
                    try:
                        sum_credit = int(input(f'How much would it be?(max {self.credit}) '))
                    except ValueError:
                        sum_credit = stake - self.money
                        print(f'\nSomething went wrong, therefore your stake has been set to {sum_credit}')

            if sum_credit > self.credit:
                print('Error...')
                while sum_credit > self.credit:
                    sum_credit = int(input('Try again: '))

            self.credit -= sum_credit
            self.debt += sum_credit
            self.money += sum_credit

        else:
            raise SystemExit
