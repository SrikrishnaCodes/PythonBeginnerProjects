from bank_accounts import *

Raj = BankAccount(2000, "Raj")
Sumit = BankAccount(5200, "Sumit")

Raj.getBalance()
Sumit.getBalance()

Raj.deposit(4530)
Sumit.deposit(32000)

Raj.withdraw(600)
Sumit.withdraw(45000)

Raj.transfer(32000, Sumit)
Raj.transfer(2000, Sumit)

Rohit = IntrestRewardsAcc(2000, "Rohit")

Rohit.deposit(3000)
Rohit.transfer(2000, Raj)

Enderman = SavingsAccount(20000, "Enderman")
Enderman.getBalance()
Enderman.deposit(1000)
Enderman.transfer(150000, Raj)
