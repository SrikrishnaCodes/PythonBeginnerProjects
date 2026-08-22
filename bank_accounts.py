class BalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ₹{self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.name} balance = ₹{self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ₹{amount} succesfully in account '{self.name}'.")
        self.getBalance()

    def vaiableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceError(
                f"\nCannot withdraw! Insufficient Funds in account '{self.name}'")

    def withdraw(self, amount):
        try:
            self.vaiableTransaction(amount)
            self.balance -= amount
            print(
                f"\nWithdrawn ₹{amount} succesfully from account '{self.name}'.")
            self.getBalance()
        except BalanceError as error:
            print(f"\nWithdraw Interupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\nBegining Transaction.... 🚀")
            self.vaiableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer Complete! ✅")
        except BalanceError as error:
            print(f"\nTransfer Interupted: {error}")


class IntrestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit Complete.")
        self.getBalance()


class SavingsAccount(IntrestRewardsAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 1000

    def withdraw(self, amount):
        try:
            self.vaiableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(
                f"\nWithdrawn ₹{amount} succesfully from account '{self.name}'.")
            self.getBalance()
        except BalanceError as error:
            print(f"Withdraw Interupted: {error}")
