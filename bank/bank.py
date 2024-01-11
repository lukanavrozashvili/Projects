class bank_account():
    def __init__(self):
        self.amount=0
    def deposit(self,Amount):
        self.amount+=Amount
        print("Amount Sucessfully Deposited")
    def withdraw(self,Amount):
        if(self.amount-Amount>=500):
            self.amount-=Amount
            print("Amount Sucessfully Withdrawn")
        else:
            print("Insufficient Balance. You have to keep at least 500$ in your Account")
    def display(self):
        print("Your Bank Balance is:", self.amount)

a = bank_account()
for i in range (0,50):
    print("1)Deposit 2)Withdraw 3)Balance 4)Exit")
    p = int(input("Enter Your Choice:"))
    if(p==1):
        Amount=float(input("Enter Amount to Deposit:"))
        a.deposit(Amount)
    elif(p==2):
        Amount=float(input("Enter Amount to Withdraw:"))
        a.withdraw(Amount)
    elif(p==3):
        a.display()
    elif(p==4):
        exit()
    else:
        print("You have Enter a Wrong Amount")