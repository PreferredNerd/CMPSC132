class Account:

    def __init__(self, name):
        self.holder=name
        self.balance=0
        self.successfulTransactionsList = []

    def deposit(self, amount):
        self.balance += amount
        appendingTransaction = Transaction("deposit", amount)
        self.successfulTransactionsList.append(appendingTransaction)
        return self.balance

    def withdraw(self, amount):
        if amount>self.balance:
            return 'Not enough money'
        self.balance-=amount
        appendingTransaction = Transaction("withdraw", amount)
        self.successfulTransactionsList.append(appendingTransaction)
        return self.balance

    @property
    def transactions (self):
        return self.successfulTransactionsList


#So I kinda got carreid away and was thinking that I should just returna string representaiton without the ""
#So I decided to write an additional class.. I know it was superfluous, but imagine the power it holds!
class Transaction:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        return "('"+ self.type +"', "+str(self.amount)+")"

    __repr__ = __str__
