def deposit(balance: float):
    return balance + amount
def withdraw(balance: float,  amount: float) -> float:
    if amount > balance:
        print ("Xatolik: Yetarli mablag' yo'q.")
        return balance 
    return balance - amount 
def check_balance(balance: float):
    print(f"Balansizngiz: {balance} som")