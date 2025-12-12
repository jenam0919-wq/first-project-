class Account :
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
#debit
    def debit(self,amount):
        self.balance =-amount
        print("rs" ,amount,"was debit")
        print("total balance=", self. get_balance())

#creadit
    def creadit(self,amount):
        self.balance-=amount
        print("rs",amount,"was creadit")
        print("total balance=", self. get_balance())
#balance display
    def get_balance(self):
        return self.balance

    

acc1 =Account(100000,78569658)
acc1.debit(451528696)
acc1.creadit(4525)
print(acc1.balance)
print(acc1.account_no)
print(acc1.get_balance)