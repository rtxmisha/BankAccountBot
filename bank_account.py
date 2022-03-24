class BankAccount:
    def __init__(self, acct_number, acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.balance = 0.0

    def displayBalance(self):
        return("На вашем счету:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Вы положили", amount)
        print("Теперь на вашем счету:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Вы сняли", amount)
            print("Теперь на вашем счету:", self.balance)
        else:
            print("Вы попытались снять", amount)
            print("На вашем счету:", self.balance)
            print("В операции отказано. Недостаточно средств.")

# myAccount = BankAccount(000000, "Sber")
#
# myAccount.deposit(35.52)
# myAccount.withdraw(15)
#
# print("Название счета:", myAccount.acct_name)
# print("Номер счета:", myAccount.acct_number)
# myAccount.displayBalance()
print("MM")

