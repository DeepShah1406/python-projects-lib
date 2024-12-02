class Account:
    def __init__(self):
        self.bal=0
        self.minbal=1000
    def deposiy(self,amt):
        self.bal = self.bal + amt
    def withdraw(self,amt):
        if(self.bal-amt < self.minbal):
            print("Minimum balance is 1000 for savings account, which is not available.")
        else:
            self.bal = self.bal - amt
    def disp (self):
        print("Balance is:",self.bal)