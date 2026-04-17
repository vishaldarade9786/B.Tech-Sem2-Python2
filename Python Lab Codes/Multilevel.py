class BankAccounts:
    def __init__(self,Acount_number,Bank_Balance):
        self.Acount_number=Acount_number
        self.Bank_Balance=Bank_Balance

    def Check_Balance(self):
        print(f"\nThe present account Balance of account {self.Acount_number} is:{self.Bank_Balance}")

    def Deposit(self,Deposit_Amount):
        self.Bank_Balance=self.Bank_Balance+Deposit_Amount
        print(f"\nAmount {Deposit_Amount} is succesfully Deposited in acount.")

    def Withdraw(self,Withdraw_Amount):
        self.Bank_Balance=self.Bank_Balance-Withdraw_Amount
        print(f"\nAmount {Withdraw_Amount} is succesfully Deposited in acount.")

        

obj1=BankAccounts(35,50000)
obj2=BankAccounts(29,50034)

obj1.Check_Balance()
obj2.Check_Balance()

obj1.Deposit(60000)
obj1.Check_Balance()

obj2.Deposit(100000)
obj2.Check_Balance()

obj1.Withdraw(50)
obj1.Check_Balance()

obj2.Withdraw(7)
obj2.Check_Balance()
