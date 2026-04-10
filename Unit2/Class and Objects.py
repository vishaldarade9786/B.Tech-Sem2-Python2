class BankAccounts:
    def __init__(self,Acount_number,Bank_Balance):
        self.Acount_number=Acount_number
        self.Bank_Balance=Bank_Balance

    def Check_Balance(self):
        print(f"The present account Balance is:{self.Bank_Balance}")

    def Deposit(self,Deposit_Amount):
        self.Bank_Balance=self.Bank_Balance+Deposit_Amount
        Check_Balance(self)

    def Withdraw(self,Withdraw_Amount):
        self.Bank_Balance=self.Bank_Balance-Withdraw_Amount
        Check_Balance(self)

obj1=BankAccounts(35,50000)
obj2=BankAccounts(29,50034)

obj1.Check_Balance()
