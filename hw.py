class Bank_Account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposit = ""
 

    def showDetails(self):
        print("The details of the account are ")
        print("Name:",self.name)
        print("Balance:",self.balance)

    def depositing(self):
        self.deposit = input(">")
        print(f"Deposit Amount: {self.deposit}")

B1 = Bank_Account("Anaadi", 200)
B1.showDetails()
B1.depositing()