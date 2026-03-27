def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Mablag' yetarli emas!")
        return balance

def check_balance(balance):
    print(f"Joriy balans: {balance} so'm")

def main():
    balance = 1000
    print("--- Bankomat ---")
    
    check_balance(balance)
    
    dep_amount = int(input("Pul kiriting: "))
    balance = deposit(balance, dep_amount)
    check_balance(balance)
    
    wit_amount = int(input("Pul yeching: "))
    balance = withdraw(balance, wit_amount)
    check_balance(balance)

if __name__ == "__main__":
    main()