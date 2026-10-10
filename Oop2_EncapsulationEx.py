class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

acc1 = BankAccount(1000)
print(acc1.get_balance())

#__balance is private variable and cannot be accessed directly
# print(acc1.__balance)  # This will raise an AttributeError