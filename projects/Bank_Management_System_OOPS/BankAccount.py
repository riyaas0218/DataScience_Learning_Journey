import json 

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, name, acc_number):
        self.name = name
        self.acc_number = acc_number
        self.__balance = 0
        self.transactions = []

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount
    
    def deposit(self,amount):
        
        if(amount>0):
            self.__balance+=amount
            print("Deposit successful!")
            self.transactions.append({"type":"Deposit","amount":amount,"balance":self.__balance})
        else:
            print("Deposit amount must be greater than zero.")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        elif amount > self.__balance:
            raise InsufficientBalanceError("Insufficient account balance")

        else:
            self.__balance -= amount
            print("Withdrawal successful")

            self.transactions.append({
                "type": "Withdraw",
                "amount": amount,
                "balance": self.__balance
            })
    def transfer(self, receiver, amount):
        if(amount<=0):
            print("Transfer amount must be greater than zero.")
            return
        if(self.__balance<amount):
            print("Insufficient balance.")
            return
        self.__balance -= amount
        receiver.__balance += amount
        print("Transfer Succesfully")
        self.transactions.append({"type": "Transfer sent", "amount": amount,"balance": self.__balance})
        receiver.transactions.append({"type": "Transfer received", "amount": amount,"balance": receiver.__balance})

        

         



    def display_transaction_history(self):
        print("\n========== TRANSACTION HISTORY ==========")

        if not self.transactions:
            print("No transactions available.")
            return

        for index, transaction in enumerate(self.transactions, start=1):
            print(f"\nTransaction {index}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: ₹{transaction['amount']}")
            print(f"Available Balance: ₹{transaction['balance']}")

        print("=========================================")
    def display_details(self):
        print("Account Holder :",self.name)
        print("Account Number :",self.acc_number)
        print("Account Balance :",self.__balance)



class SavingsAccount(BankAccount):
    def __init__(self,name,acc_number,interest_rate):
        super().__init__(name, acc_number)
        self.interest_rate=interest_rate

    def withdraw(self, amount):
        balance = self.get_balance()
        check_valid_amount = balance - amount
        if(check_valid_amount>=1000 and amount > 0 and balance>=amount):
            super().withdraw(amount)   
        else:
           print("Withdrawal rejected")
                
           
        
class CurrentAccount(BankAccount):
    def __init__(self, name, acc_number,overdraft_limit):
        super().__init__(name, acc_number)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        balance=self.get_balance()
        max_withdraw = self.overdraft_limit + balance
        if(amount>0 and amount<=max_withdraw):
            self._update_balance(-amount)
            self.transactions.append({"type": "Withdraw", "amount": amount,"balance":self.get_balance()})
        else:
            raise InsufficientBalanceError("Overdraft limit exceeded")
        
        


try:
    with open("bank.json", "r") as file:
        loaded_accounts = json.load(file)

except FileNotFoundError:
    print("Bank data file not found.")
    loaded_accounts = []

except json.JSONDecodeError:
    print("Bank data file is corrupted.")
    loaded_accounts = []



bank_objects = []

for data in loaded_accounts:
    account = BankAccount(
        data["name"],
        data["account_number"]
    )
    account._update_balance(data["balance"])
    account.transactions = data["transactions"]
    bank_objects.append(account)



def Save_account():
    account_data=[]
    for account in bank_objects:
        acc_data={
            "name":account.name,
            "account_number": account.acc_number,
            "balance": account.get_balance(),
            "transactions": account.transactions
        }
        account_data.append(acc_data)

    with open("bank.json", "w") as file:
        json.dump(account_data, file, indent=4)


while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Save Account")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name=input("Enter a Name")
        acc_number=int(input("Enter a Account number"))
        account_exists = False
        for account in bank_objects:
            if account.acc_number == acc_number:
                account_exists = True
                break
        if account_exists:
            print("Account number already exists!")
        else:
            account = BankAccount(name,acc_number)
            bank_objects.append(account)
            print("Account created successfully!")
    elif choice == "2":
        acc_number = int(input("Enter account number: "))

        found_account = None

        for account in bank_objects:
            if account.acc_number == acc_number:
                found_account = account
                break

        if found_account:
            found_account.display_details()
        else:
            print("Account not found!")
    elif choice == "3":
        acc_number = int(input("Enter account number: "))

        found_account = None

        for account in bank_objects:
            if account.acc_number == acc_number:
                found_account = account
                break

        if found_account:
            amount = int(input("Enter deposit amount: "))
            found_account.deposit(amount)
            
        else:
            print("Account not found!")

    elif choice == "4":
        acc_number = int(input("Enter account number: "))

        found_account = None

        for account in bank_objects:
            if account.acc_number == acc_number:
                found_account = account
                break

        if found_account:
            amount = int(input("Enter withdrawal amount: "))

            try:
                found_account.withdraw(amount)
            except (ValueError, InsufficientBalanceError) as e:
                print("Withdrawal failed:", e)

        else:
            print("Account not found!")

    elif choice == "5":
        sender_acc = int(input("Enter a Sender Account number"))
        found_send_account = None
        for account in bank_objects:
            if account.acc_number == sender_acc:
                found_send_account = account
                break

        if found_send_account:
            receiver_acc = int(input("Enter a Reciver Account Number"))
            found_receiv_account = None
            for account in bank_objects:
                if account.acc_number == receiver_acc:
                    found_receiv_account = account
                    break
            if found_send_account != found_receiv_account:
                if found_receiv_account:
                    transfer_amount=int(input("Enter a Transfer Amount"))
                    found_send_account.transfer(found_receiv_account,transfer_amount)

                else:
                    print("Receiver Account Not Found")
            else:
                print("Sender And Reciver Account is Same Please Check")
                
                
        else:
            print("Sender Account Not Found")

    elif choice == "6":
        acc_number = int(input("Enter a Account Number"))
        account_found=None
        for account in bank_objects:
            if account.acc_number == acc_number:
                account_found = account
                break
            
        if account_found:
            account_found.display_transaction_history()
        else:
            print("Account Not Found")
        

    elif choice == "7":
        Save_account()
        print("Bank data saved successfully!")
        print("Thank you for using our bank!")

    elif choice == "8":
        Save_account()
        print("Thank you for using our bank!")
        break
  
    else:
        print("Invalid choice. Please try again.")












