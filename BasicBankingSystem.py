class BankAccount:
    def __init__(self, accountNumber, accountHolder, pin, balance=0):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__pin = pin
        self.__balance = balance

    def get_Details(self):
        print("\n Account Details: ")
        print(f" Account Holder : {self.__accountHolder}")
        print(f" Account Number : {self.__accountNumber}")
        print(f" Balance Rs : {self.__balance}")

    def Deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs : {amount} | New Balance = {self.__balance}")
        else:
            print("Invalid Deposit Amount! ")

    def withDraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance!")
        elif amount <= 0:
            print("Invalid Withdraw Amount!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount} | Remaining Balance = {self.__balance}")


print("Welcome to Kazi Bank")
acc_num = input("Enter Account Number: ")
acc_name = input("Enter Account Holder Name: ")
pin = input("Set Pin (4 Digits): ")

account = BankAccount(acc_num, acc_name, pin)

while True:
    print("\nChoose an Option: ")
    print("1: Show Account Details")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("0: Exit! ")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        account.get_Details()

    elif choice == "2":
        amount = float(input("Enter Amount to Deposit: "))
        account.Deposit(amount)

    elif choice == "3":
        amount = float(input("Enter Amount to Withdraw: "))
        account.withDraw(amount)

    elif choice == "0":
        print("Thank you For Using this Bank!")
        break

    else:
        print("Invalid choice! Try again.")
